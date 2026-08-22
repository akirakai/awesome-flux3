# Awesome FLUX.3

A source-first collection of outstanding **FLUX.3 videos**, maintained by a ChatGPT scheduled task that searches X/Twitter and the public web once per hour.

The repository is deliberately content-only: **no crawler scripts, no GitHub Actions, and no API token setup**. Every accepted discovery is written directly into this README.

> Prompts are included only when they are visibly present in the original source. A prompt is never reconstructed from the video and presented as the creator's original prompt.

## Collection policy

An item is accepted only when it:

1. is explicitly attributed to `FLUX.3`, `Flux 3`, or `#FLUX3` by the original creator or another traceable primary source;
2. contains or directly links to a video;
3. points to the original source rather than a repost-only page;
4. demonstrates strong visual quality, originality, technique, or reusable prompting value;
5. is not already listed below.

### Prompt provenance

| Status | Meaning |
|---|---|
| `verbatim_in_post` | The prompt is copied from an explicit prompt section in the original source. |
| `mentioned_not_in_post` | The creator refers to a prompt, but it is not visible in the verified source. |
| `not_provided` | No prompt was found or claimed. |

## Curated videos

_Last updated: 2026-08-22 · Entries: 155_

### 155. Meerkat-detail 4K upscaler benchmark vs. Topaz and Flash VSR — Dennis Schöneberg

- **Creator:** [Dennis Schöneberg](https://www.linkedin.com/in/dennis-sch%C3%B6neberg-3420a2221/)
- **Published:** 2026-08-21 (based on the secondary verification page’s relative “1 day ago” timestamp at verification).
- **Original source:** Dennis Schöneberg’s LinkedIn creator post; the direct activity URL is not exposed by the accessible public index.
- **Verification source:** [Secondary LinkedIn profile page directly embedding and quoting Schöneberg’s original creator post](https://nz.linkedin.com/in/zhenjie-zhao-b27907275/zh-cn)
- **Model attribution:** Schöneberg explicitly identifies the tested model as “FLUX 3 Video Upscale,” tags `#FLUX3`, and compares its Creative result against Topaz Astra 2, Topaz Starlight Precise 2, and Flash VSR.
- **Summary:** A 400% zoom on a tiny meerkat in a garden compares how four video upscalers reconstruct fine subject detail. Schöneberg reports that FLUX 3 Creative recovers a recognizable head and posture while the competing upscalers mostly produce distorted mutations.
- **Workflow/details:** Schöneberg built ComfyUI nodes for the new BFL upscaling API and ran a four-way comparison. He records 480p+ input support, 1.5×/2×/3× scaling up to 4K, Precise mode at 4 steps for faster identity-preserving output, and Creative mode at 8 steps for stronger repair/detail synthesis. LinkedIn’s resolution limits are why he presents a 400% crop of the small subject.
- **Prompt provenance:** `not_provided` — this is a video-super-resolution benchmark and the creator does not publish an exact prompt for the tested clip; none has been inferred.
- **Why included:** Fresh traceable creator-side `#FLUX3` attribution, attached video-comparison context, a concrete ComfyUI/API workflow, and a difficult small-subject reconstruction benchmark against three named competing upscalers. The preserved source also shows 71 reactions, indicating meaningful public interest.

## How updates work

The hourly ChatGPT task checks this README first, searches for newer qualifying sources, rejects duplicates and ambiguous attribution, then appends verified entries here. It reports only when at least one new entry has been successfully committed.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Repository text and curation structure are licensed under the [MIT License](LICENSE). Linked post text, prompts, media, creator names, and other third-party material remain the property of their respective authors.