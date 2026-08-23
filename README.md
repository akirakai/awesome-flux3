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

<!--

## Curated videos

_Last updated: 2026-07-25 · Entries: 2_

-->

## Curated videos

_Last updated: 2026-08-23 · Entries: 161_

### 1. Multi-shot realism favorites — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/venturetwins/status/2080318877154852912)
- **Model attribution:** Explicitly identified by the creator as FLUX 3
- **Summary:** An early-access tester shares a thread of favorite FLUX 3 generations, highlighting realistic small details and multi-shot clips lasting up to 20 seconds from a single prompt.
- **Workflow/details:** Text-to-video; the creator reports one-prompt generation across multiple shots, with clips up to 20 seconds.
- **Prompt provenance:** `not_provided` — the creator mentions a single-prompt workflow, but the actual prompt is not visible in the verified top-level post and has not been inferred.
- **Why included:** Original creator/tester post with attached video examples, explicit model attribution, convincing realism, and a strong demonstration of multi-shot continuity.

### 2. Official FLUX 3 Video early-access showcase — Black Forest Labs

- **Creator:** [Black Forest Labs (@bfl_ai)](https://x.com/bfl_ai)
- **Published:** 2026-07-23
- **Original source:** [FLUX 3 launch article and official showcase](https://bfl.ai/blog/flux-3)
- **Model attribution:** Official Black Forest Labs release showcase for FLUX 3 Video
- **Summary:** The official launch showcase presents native-audio video generation across text-to-video, image-to-video, reference video transfer, video-and-audio continuation, keyframe transitions, multilingual dialogue, typography, and multi-shot chaining.
- **Workflow/details:** FLUX 3 accepts text, image, and video references; generates video with native audio up to 20 seconds; and supports chaining clips into longer sequences. Black Forest Labs reports that its preliminary evaluation set used 10-second, 720p text-to-video clips with audio.
- **Prompt provenance:** `not_provided` — the launch article describes the workflows and displays official outputs, but does not publish a verified prompt for each showcased clip.
- **Why included:** Definitive primary source from the model creator, with explicit FLUX 3 attribution, official output examples, reproducible capability details, and unusually broad multimodal video coverage.

### 161. 400% meerkat-detail FLUX 3 Video Upscale benchmark vs. Topaz/Starlight/Flash VSR — Dennis Schöneberg

- **Creator:** [Dennis Schöneberg](https://de.linkedin.com/in/dennis-schoeneberg)
- **Published:** 2026-08-21 (based on LinkedIn’s public two-day relative timestamp at verification).
- **Original source:** [Dennis Schöneberg’s LinkedIn creator activity page](https://de.linkedin.com/in/dennis-schoeneberg) — the public index exposes the original creator post on-profile but not a stable direct activity permalink.
- **Model attribution:** Schöneberg explicitly identifies the test as **FLUX 3 Video Upscale**, tags `#FLUX3`, and reports the shown result from **FLUX 3 Creative**.
- **Summary:** A 400%-zoomed tiny-detail comparison uses a meerkat in a garden to pit FLUX 3 Video Upscale against Topaz Astra 2, Topaz Starlight Precise 2, and Flash VSR; Schöneberg reports that FLUX 3 Creative preserves a recognizable head and posture while the competing outputs mutate the subject more heavily.
- **Workflow/details:** Schöneberg built ComfyUI nodes for the new API and ran the same difficult tiny-detail target across the named upscalers. He documents FLUX Video Upscale as accepting source video from 480p, regenerating up to native 4K at 1.5×/2×/3×, with Precise at 4 steps for fidelity/identity and Creative at 8 steps for stronger repair/detail generation. The LinkedIn upload is a 400% zoom-in because the platform would not show the full-resolution comparison fairly.
- **Prompt provenance:** `not_provided` — no text prompt for the source clip or upscale pass is visible in the verified creator post.
- **Why included:** A fresh, primary creator-side technical benchmark with named competitors, concrete mode/step settings, ComfyUI workflow context, and a deliberately unforgiving tiny-subject reconstruction target rather than a generic launch reel.

## How updates work

The hourly ChatGPT task checks this README first, searches for newer qualifying sources, rejects duplicates and ambiguous attribution, then appends verified entries here. It reports only when at least one new entry has been successfully committed.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Repository text and curation structure are licensed under the [MIT License](LICENSE). Linked post text, prompts, media, creator names, and other third-party material remain the property of their respective authors.
