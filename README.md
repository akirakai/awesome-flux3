# Awesome FLUX.3

A continuously updated, source-first collection of outstanding **FLUX.3 videos published on X/Twitter**.

Every entry aims to preserve:

- the original X post and creator
- engagement signals at collection time
- the creator's prompt when it is actually present
- clear prompt provenance (`verbatim_in_post`, `mentioned_not_in_post`, or `not_provided`)
- a lightweight quality score for sorting, not as a claim of objective quality

> This project never invents or reverse-engineers a prompt and presents it as the creator's original prompt.

## Browse

See **[CATALOG.md](CATALOG.md)** for the human-readable collection, or **[data/videos.json](data/videos.json)** for structured data.

## Collection policy

A post is eligible only when it:

1. explicitly names `FLUX.3`, `Flux 3`, or `#FLUX3` in the post text;
2. contains attached video media;
3. is an original post rather than a repost;
4. passes the configured quality threshold;
5. has not already been collected.

Prompt provenance:

| Status | Meaning |
|---|---|
| `verbatim_in_post` | Prompt text was copied from an explicit prompt section in the original post. |
| `mentioned_not_in_post` | The creator says a prompt exists elsewhere, but it is not present in the collected post text. |
| `not_provided` | No prompt was found or claimed. |

## Hourly automation

The workflow runs at minute 17 of every hour and can also be launched manually. It uses X API v2 recent search and commits newly accepted entries back to the repository.

### Required setup

1. Create an X developer app and obtain a Bearer Token.
2. In this repository, open **Settings → Secrets and variables → Actions**.
3. Add a repository secret named `X_BEARER_TOKEN`.
4. Run **Actions → Collect FLUX.3 videos → Run workflow** once to verify it.

Optional repository variables:

| Variable | Default | Purpose |
|---|---:|---|
| `FLUX3_QUERY` | `("FLUX.3" OR "Flux 3" OR #FLUX3) has:videos -is:retweet` | X recent-search query |
| `FLUX3_MIN_SCORE` | `8` | Minimum quality score |
| `FLUX3_MAX_RESULTS` | `100` | Results requested per run, 10–100 |

The scheduled workflow exits cleanly without changing files when `X_BEARER_TOKEN` is absent.

## Run locally

```bash
export X_BEARER_TOKEN='...'
python scripts/collect_x.py
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Data notes

- Metrics are snapshots from collection time and may later change on X.
- X recent search covers a limited recent window; this project is designed for continuous collection rather than historical completeness.
- Video files are not mirrored. The catalog links to the original creator's post and stores only metadata and preview URLs returned by the API.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code is licensed under the [MIT License](LICENSE). Post text, prompts, media, and creator names remain the property of their respective authors and are included only as attributed metadata and links.
