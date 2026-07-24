import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "collect_x.py"
SPEC = importlib.util.spec_from_file_location("collect_x", MODULE_PATH)
collect_x = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = collect_x
SPEC.loader.exec_module(collect_x)


class CollectorTests(unittest.TestCase):
    def test_extracts_verbatim_prompt(self):
        status, prompt = collect_x.extract_prompt(
            "Made with FLUX.3\nPrompt: cinematic tracking shot of a silver robot crossing a flooded city"
        )
        self.assertEqual(status, "verbatim_in_post")
        self.assertIn("cinematic tracking shot", prompt)

    def test_does_not_invent_prompt(self):
        status, prompt = collect_x.extract_prompt("FLUX.3 video test. Prompt in replies.")
        self.assertEqual(status, "mentioned_not_in_post")
        self.assertIsNone(prompt)

    def test_requires_explicit_model_and_video(self):
        payload = {
            "data": [
                {
                    "id": "1",
                    "author_id": "u1",
                    "text": "FLUX.3 Prompt: an intricate cinematic sequence with dramatic lighting",
                    "created_at": "2026-07-24T00:00:00Z",
                    "attachments": {"media_keys": ["m1"]},
                    "public_metrics": {"like_count": 100, "retweet_count": 10},
                },
                {
                    "id": "2",
                    "author_id": "u1",
                    "text": "Amazing AI video without model attribution",
                    "created_at": "2026-07-24T00:00:00Z",
                    "attachments": {"media_keys": ["m1"]},
                    "public_metrics": {"like_count": 1000},
                },
            ],
            "includes": {
                "users": [{"id": "u1", "username": "creator", "name": "Creator", "verified": True}],
                "media": [{"media_key": "m1", "type": "video", "preview_image_url": "https://example.test/p.jpg"}],
            },
        }
        entries = collect_x.collect_entries(payload, min_score=0, collected_at="2026-07-24T01:00:00Z")
        self.assertEqual([entry["id"] for entry in entries], ["1"])

    def test_merge_is_idempotent(self):
        entry = {"id": "1", "quality_score": 9, "created_at": "2026-07-24T00:00:00Z"}
        merged, added = collect_x.merge_entries([entry], [dict(entry)])
        self.assertEqual(len(merged), 1)
        self.assertEqual(added, 0)


if __name__ == "__main__":
    unittest.main()
