# Awesome FLUX.3

A continuously updated, source-first collection of outstanding **FLUX.3 videos published on X/Twitter**.

Every entry aims to preserve:

- the original X post and creator
- the original source link
- the creator's prompt when it is actually present
- clear prompt provenance (`verbatim_in_post`, `mentioned_not_in_post`, or `not_provided`)
- a short quality rationale

> This project never invents or reverse-engineers a prompt and presents it as the creator's original prompt.

## Browse

See **[CATALOG.md](CATALOG.md)** for the human-readable collection, or **[data/videos.json](data/videos.json)** for structured data.

## Collection policy

A post is eligible only when it:

1. is explicitly attributed to `FLUX.3`, `Flux 3`, or `#FLUX3` by the original creator or another traceable primary source;
2. contains or directly links to a video;
3. is an original source rather than a repost-only page;
4. demonstrates strong visual quality, originality, technique, or reusable prompting value;
5. has not already been collected.

Prompt provenance:

| Status | Meaning |
|---|---|
| `verbatim_in_post` | Prompt text was copied from an explicit prompt section in the original post. |
| `mentioned_not_in_post` | The creator says a prompt exists elsewhere, but it is not present in the collected source. |
| `not_provided` | No prompt was found or claimed. |

## Hourly curation

The collection is maintained by a ChatGPT scheduled task that searches X/Twitter and the public web once per hour, verifies model attribution and source provenance, removes duplicates, and writes accepted entries directly to this repository.

This repository does **not** use GitHub Actions and does not require an `X_BEARER_TOKEN`.

The task only reports when new verified entries are successfully added.

## Optional local tools

The repository retains a small X API collector and tests for optional manual use:

```bash
export X_BEARER_TOKEN='...'
python scripts/collect_x.py
python -m unittest discover -s tests -v
```

These scripts are not used by the hourly ChatGPT curation task.

## Data notes

- Engagement metrics, when available, are snapshots and may later change.
- Video files are not mirrored. The catalog links to the original source and stores metadata only.
- Attribution must be explicit; visual style or publication date alone is not enough to identify a model.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code is licensed under the [MIT License](LICENSE). Post text, prompts, media, and creator names remain the property of their respective authors and are included only as attributed metadata and links.
