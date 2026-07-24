#!/usr/bin/env python3
"""Collect high-quality FLUX.3 video posts from X API v2 recent search.

The collector is intentionally source-first:
- requires explicit FLUX.3 attribution in the post text;
- requires attached video media;
- never fabricates or reconstructs a creator prompt;
- deduplicates by X post ID;
- writes deterministic JSON and Markdown output.
"""

from __future__ import annotations

import json
import math
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "videos.json"
STATE_FILE = ROOT / "data" / "state.json"
CATALOG_FILE = ROOT / "CATALOG.md"
API_URL = "https://api.x.com/2/tweets/search/recent"
DEFAULT_QUERY = '("FLUX.3" OR "Flux 3" OR #FLUX3) has:videos -is:retweet'
MODEL_RE = re.compile(r"(?i)(?:\bflux\s*[.-]?\s*3\b|#flux3\b)")
PROMPT_MARKER_RE = re.compile(
    r"(?im)(?:^|[\n\r])\s*(?:full\s+prompt|video\s+prompt|prompt|提示词|提示語)\s*[:：\-–—]\s*"
)
PROMPT_REFERENCE_RE = re.compile(
    r"(?i)\b(prompt\s+(?:below|in\s+(?:repl(?:y|ies)|comments?|thread|bio|link))|see\s+(?:the\s+)?prompt)\b|"
    r"提示词(?:在|见)(?:评论|回复|链接|主页)"
)


class CollectorError(RuntimeError):
    pass


@dataclass(frozen=True)
class Config:
    token: str
    query: str
    min_score: float
    max_results: int

    @classmethod
    def from_env(cls) -> "Config":
        token = os.getenv("X_BEARER_TOKEN", "").strip()
        query = os.getenv("FLUX3_QUERY", DEFAULT_QUERY).strip() or DEFAULT_QUERY
        try:
            min_score = float(os.getenv("FLUX3_MIN_SCORE", "").strip() or "8")
        except ValueError as exc:
            raise CollectorError("FLUX3_MIN_SCORE must be numeric") from exc
        try:
            max_results = int(os.getenv("FLUX3_MAX_RESULTS", "").strip() or "100")
        except ValueError as exc:
            raise CollectorError("FLUX3_MAX_RESULTS must be an integer") from exc
        max_results = max(10, min(100, max_results))
        return cls(token=token, query=query, min_score=min_score, max_results=max_results)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CollectorError(f"Cannot read valid JSON from {path}") from exc
    if not isinstance(value, dict):
        raise CollectorError(f"Expected a JSON object in {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def api_request(config: Config, since_id: str | None) -> dict[str, Any]:
    params: dict[str, str] = {
        "query": config.query,
        "max_results": str(config.max_results),
        "sort_order": "recency",
        "tweet.fields": "id,text,author_id,created_at,lang,public_metrics,entities,attachments",
        "expansions": "author_id,attachments.media_keys",
        "user.fields": "id,name,username,verified,public_metrics",
        "media.fields": "media_key,type,preview_image_url,url,variants,duration_ms,height,width",
    }
    if since_id:
        params["since_id"] = since_id

    request = urllib.request.Request(
        f"{API_URL}?{urllib.parse.urlencode(params)}",
        headers={
            "Authorization": f"Bearer {config.token}",
            "User-Agent": "awesome-flux3-collector/1.0",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:1000]
        raise CollectorError(f"X API returned HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise CollectorError(f"X API request failed: {exc.reason}") from exc

    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise CollectorError("X API returned invalid JSON") from exc
    if not isinstance(payload, dict):
        raise CollectorError("X API returned an unexpected response")
    return payload


def media_by_key(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    media = payload.get("includes", {}).get("media", [])
    return {
        item["media_key"]: item
        for item in media
        if isinstance(item, dict) and isinstance(item.get("media_key"), str)
    }


def users_by_id(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    users = payload.get("includes", {}).get("users", [])
    return {
        item["id"]: item
        for item in users
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


def attached_videos(tweet: dict[str, Any], media_map: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    keys = tweet.get("attachments", {}).get("media_keys", [])
    videos: list[dict[str, Any]] = []
    for key in keys:
        item = media_map.get(key)
        if item and item.get("type") in {"video", "animated_gif"}:
            videos.append(item)
    return videos


def engagement(metrics: dict[str, Any]) -> int:
    weights = {
        "like_count": 1,
        "retweet_count": 3,
        "quote_count": 3,
        "reply_count": 1,
        "bookmark_count": 2,
    }
    total = 0
    for key, weight in weights.items():
        value = metrics.get(key, 0)
        if isinstance(value, int) and value > 0:
            total += value * weight
    return total


def quality_score(tweet: dict[str, Any], author: dict[str, Any], prompt_status: str) -> float:
    metrics = tweet.get("public_metrics", {})
    score = 4.0
    score += min(8.0, math.log10(engagement(metrics) + 1) * 3.2)
    if prompt_status == "verbatim_in_post":
        score += 4.0
    elif prompt_status == "mentioned_not_in_post":
        score += 1.0
    if author.get("verified") is True:
        score += 1.0
    text = str(tweet.get("text", ""))
    if any(token in text.lower() for token in ("workflow", "settings", "seed", "steps", "behind the scenes")):
        score += 1.0
    return round(score, 2)


def clean_prompt(value: str) -> str:
    value = value.strip()
    value = re.sub(r"\n{3,}", "\n\n", value)
    value = re.sub(r"\s+https?://t\.co/\w+\s*$", "", value).strip()
    return value[:4000]


def extract_prompt(text: str) -> tuple[str, str | None]:
    match = PROMPT_MARKER_RE.search(text)
    if match:
        candidate = clean_prompt(text[match.end() :])
        if len(candidate) >= 20:
            return "verbatim_in_post", candidate
    if PROMPT_REFERENCE_RE.search(text):
        return "mentioned_not_in_post", None
    return "not_provided", None


def best_preview(videos: Iterable[dict[str, Any]]) -> str | None:
    for video in videos:
        url = video.get("preview_image_url") or video.get("url")
        if isinstance(url, str) and url.startswith("http"):
            return url
    return None


def normalize_entry(
    tweet: dict[str, Any],
    author: dict[str, Any],
    videos: list[dict[str, Any]],
    collected_at: str,
) -> dict[str, Any]:
    text = str(tweet.get("text", "")).strip()
    prompt_status, prompt = extract_prompt(text)
    username = str(author.get("username") or tweet.get("author_id") or "unknown")
    tweet_id = str(tweet["id"])
    metrics = tweet.get("public_metrics", {})
    entry = {
        "id": tweet_id,
        "url": f"https://x.com/{username}/status/{tweet_id}",
        "author": {
            "id": str(author.get("id") or tweet.get("author_id") or ""),
            "username": username,
            "name": author.get("name"),
            "verified": bool(author.get("verified", False)),
        },
        "created_at": tweet.get("created_at"),
        "collected_at": collected_at,
        "text": text,
        "prompt_status": prompt_status,
        "prompt": prompt,
        "metrics": {
            "likes": int(metrics.get("like_count", 0) or 0),
            "reposts": int(metrics.get("retweet_count", 0) or 0),
            "quotes": int(metrics.get("quote_count", 0) or 0),
            "replies": int(metrics.get("reply_count", 0) or 0),
            "bookmarks": int(metrics.get("bookmark_count", 0) or 0),
        },
        "media": {
            "type": "video",
            "count": len(videos),
            "preview_image_url": best_preview(videos),
        },
    }
    entry["quality_score"] = quality_score(tweet, author, prompt_status)
    return entry


def collect_entries(payload: dict[str, Any], min_score: float, collected_at: str) -> list[dict[str, Any]]:
    users = users_by_id(payload)
    media = media_by_key(payload)
    accepted: list[dict[str, Any]] = []
    for tweet in payload.get("data", []) or []:
        if not isinstance(tweet, dict) or not isinstance(tweet.get("id"), str):
            continue
        text = str(tweet.get("text", ""))
        if not MODEL_RE.search(text):
            continue
        videos = attached_videos(tweet, media)
        if not videos:
            continue
        author = users.get(str(tweet.get("author_id")), {})
        entry = normalize_entry(tweet, author, videos, collected_at)
        if entry["quality_score"] >= min_score:
            accepted.append(entry)
    return accepted


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render_catalog(entries: list[dict[str, Any]], updated_at: str | None) -> str:
    lines = [
        "# FLUX.3 Video Catalog",
        "",
        f"Last updated: `{updated_at or 'not yet'}` · Entries: **{len(entries)}**",
        "",
        "Entries are sorted by quality score, then publication time. Metrics are snapshots from collection time.",
        "",
    ]
    if not entries:
        lines.extend(["_No qualifying entries have been collected yet._", ""])
        return "\n".join(lines)

    lines.extend(
        [
            "| Score | Creator | Published | Prompt | Metrics | Source |",
            "|---:|---|---|---|---:|---|",
        ]
    )
    for entry in entries:
        author = entry["author"]
        metrics = entry["metrics"]
        metric_text = f"♥ {metrics['likes']} · ↻ {metrics['reposts']} · ◇ {metrics['quotes']}"
        prompt_label = {
            "verbatim_in_post": "✅ in post",
            "mentioned_not_in_post": "↗ referenced",
            "not_provided": "—",
        }.get(entry.get("prompt_status"), "—")
        published = str(entry.get("created_at") or "")[:10]
        lines.append(
            "| {score:.2f} | [@{user}](https://x.com/{user}) | {date} | {prompt} | {metrics} | [post]({url}) |".format(
                score=float(entry["quality_score"]),
                user=markdown_escape(str(author["username"])),
                date=published,
                prompt=prompt_label,
                metrics=metric_text,
                url=entry["url"],
            )
        )

    lines.extend(["", "## Prompts available in original posts", ""])
    prompt_entries = [e for e in entries if e.get("prompt_status") == "verbatim_in_post" and e.get("prompt")]
    if not prompt_entries:
        lines.extend(["_No verbatim prompts collected yet._", ""])
    else:
        for entry in prompt_entries:
            user = entry["author"]["username"]
            lines.extend(
                [
                    f"### [@{user} · {entry['id']}]({entry['url']})",
                    "",
                    "```text",
                    str(entry["prompt"]).replace("```", "` ` `"),
                    "```",
                    "",
                ]
            )
    return "\n".join(lines)


def merge_entries(existing: list[dict[str, Any]], incoming: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    by_id = {str(item.get("id")): item for item in existing if item.get("id")}
    before = len(by_id)
    for item in incoming:
        by_id.setdefault(str(item["id"]), item)
    merged = list(by_id.values())
    merged.sort(
        key=lambda item: (float(item.get("quality_score", 0)), str(item.get("created_at") or "")),
        reverse=True,
    )
    return merged, len(by_id) - before


def main() -> int:
    config = Config.from_env()
    if not config.token:
        print("X_BEARER_TOKEN is not configured; nothing to collect.")
        return 0

    state = read_json(STATE_FILE, {"since_id": None, "last_run_at": None})
    store = read_json(DATA_FILE, {"schema_version": 1, "updated_at": None, "entries": []})
    existing = store.get("entries", [])
    if not isinstance(existing, list):
        raise CollectorError("data/videos.json entries must be a list")

    payload = api_request(config, state.get("since_id"))
    now = utc_now()
    incoming = collect_entries(payload, config.min_score, now)
    merged, added = merge_entries(existing, incoming)

    newest_id = payload.get("meta", {}).get("newest_id")
    if isinstance(newest_id, str):
        state["since_id"] = newest_id
    state["last_run_at"] = now
    write_json(STATE_FILE, state)

    if added:
        store = {"schema_version": 1, "updated_at": now, "entries": merged}
        write_json(DATA_FILE, store)
        CATALOG_FILE.write_text(render_catalog(merged, now), encoding="utf-8")
    else:
        CATALOG_FILE.write_text(render_catalog(existing, store.get("updated_at")), encoding="utf-8")

    print(f"Fetched {len(payload.get('data', []) or [])} posts; accepted {len(incoming)}; added {added}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except CollectorError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
