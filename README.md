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

_Last updated: 2026-07-25 · Entries: 9_

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

### 3. First-person mech vs. kaiju action test — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/cfryant/status/2080379186783379947)
- **Model attribution:** Explicitly labeled by the creator as another FLUX 3 early-access test
- **Summary:** A first-person GoPro-style action sequence puts the viewer inside a giant mech fighting a kaiju in Seattle, culminating in the Space Needle being used as an improvised weapon.
- **Workflow/details:** Text-to-video early-access test focused on POV camera coherence, large-scale interaction, fast action staging, and recognizable landmark handling.
- **Prompt provenance:** `not_provided` — the post describes the scene, but does not explicitly identify that wording as the generation prompt; no prompt has been inferred.
- **Why included:** Original AI filmmaker post with attached video, explicit FLUX 3 attribution, ambitious first-person choreography, large-scale physical interaction, and a demanding recognizable-location test.

### 4. One-shot rally-car avalanche chase — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/umesh_ai/status/2080332510358282688)
- **Model attribution:** Explicitly presented by the creator as an early FLUX 3 test
- **Summary:** A rally car races along a narrow alpine cliff road while an avalanche closes in, testing long-form action continuity, dynamic camera movement, environmental physics, and sustained tension in one generation.
- **Workflow/details:** Text-to-video; 15-second cinematic action sequence requested as one continuous shot with no cuts, morphing, or scene transitions.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Hyper realistic blockbuster cinematic 15 second action sequence in one true unbroken continuous shot, with no cuts, no morphing, and no scene transitions.” The complete prompt remains in the original post.
- **Why included:** Original early-access creator post with attached video, explicit FLUX 3 attribution, a visible prompt, complex action choreography, and a high-signal continuity test.

### 5. Predicted future vs. real robot rollout — Black Forest Labs × mimic robotics

- **Creator:** [Black Forest Labs](https://bfl.ai/) and [mimic robotics](https://www.mimicrobotics.com/)
- **Published:** 2026-07-23
- **Original source:** [FLUX 3 × mimic technical showcase](https://bfl.ai/blog/flux-3-mimic)
- **Model attribution:** Officially identified as FLUX-mimic, a video-action model built on the FLUX 3 backbone
- **Summary:** The official showcase places the FLUX 3 backbone’s predicted visual future alongside the physical robot rollout decoded from it, demonstrating contact-aware manipulation, recovery after missed grasps, and deployment on real factory tasks.
- **Workflow/details:** FLUX 3 is jointly trained across image, video, and audio; mimic adds a lightweight action decoder over intermediate video-prediction features. The article reports tasks including component kitting, tight-fixture insertion, assembly, and manipulation of flexible seals and cables, with the optimized system reacting in 101 ms.
- **Prompt provenance:** `not_provided` — this is a robotics video-action demonstration rather than a published text-to-video prompt example, and the source provides no verbatim prompt.
- **Why included:** Direct primary source from the model developer and robotics partner, explicit FLUX 3 attribution, paired predicted-video and real-world rollout evidence, and an unusually demanding demonstration of learned physics transferring from video modeling into physical action.

### 6. Mongolia visual-language stress test — Christian Hartmann / CHAIPEAU™

- **Creator:** [Christian Hartmann](https://de.linkedin.com/in/chrtmn) / [CHAIPEAU™](https://www.chaipeau.com/)
- **Published:** 2026-07-25
- **Original source:** [Creator post embedded by LinkedIn in a direct reshare](https://de.linkedin.com/posts/dr-tristan-behrens-734967a2_wir-sind-sowas-von-zur%C3%BCck-schaut-mal-was-activity-7486362273700020224-5_eY)
- **Model attribution:** Hartmann identifies himself as a member of the official Black Forest Labs creator team with exclusive FLUX 3 early access, and explicitly states that all 20 scenes were generated in the official FLUX 3 Discord.
- **Summary:** Twenty still images from Hartmann’s Mongolia-inspired CHAIPEAU™ series are translated into a coherent audiovisual production, testing whether a tightly controlled visual language—desaturated palette, shadow-heavy lighting, warm anchors, grain, haze, and 2.39:1 composition—survives the move from still imagery into continuous motion and native sound.
- **Workflow/details:** The creator first deconstructed all 20 source images into palette, lighting, atmosphere, and content constants without using them as visual inputs. Each image became a director-style scene brief with a defined camera move, a continuous 20-second take with no cuts, and sound design written into the prompt. The scenes were generated with native audio, letterboxed to 2.39:1, then assembled using Adobe Creative Cloud and Claude Cowork. Hartmann notes that terrain, leading lines, palette, haze, and light held especially well; for human and wildlife motion drift, simplifying the camera move worked better than adding complexity.
- **Prompt provenance:** `mentioned_not_in_post` — the creator says the complete scene prompt is in the comments, but it is not visible in the publicly verified source view, so no prompt text has been copied or inferred.
- **Why included:** A structured, original early-access production from an official BFL creator-team member, with unusually detailed and reproducible workflow notes, 20-second continuous-shot testing, native audio direction, a consistent multi-scene art direction system, and candid observations about where the model succeeds and how to mitigate motion drift.

### 7. Native-audio and mixed-reference capability reel — cheaty

- **Creator:** [cheaty (@cheatyyyy)](https://x.com/cheatyyyy)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/cheatyyyy/status/2080314577385132290)
- **Model attribution:** Explicitly identified by the early-access creator as FLUX 3
- **Summary:** A four-video early-access reel highlights FLUX 3’s native audio quality and its ability to generate clips up to 20 seconds while combining image, video, and audio references.
- **Workflow/details:** The creator reports support for mixed image/video/audio inputs and up to 10 reference assets in one workflow, with the references able to be combined rather than restricted to a single modality.
- **Prompt provenance:** `not_provided` — the verified post describes model capabilities and includes multiple video outputs, but does not publish a generation prompt for the showcased clips; no prompt has been inferred.
- **Why included:** Original early-access creator post with four attached video examples, explicit FLUX 3 attribution, concrete multimodal-input details, and a useful native-audio and reference-conditioning capability overview.

### 8. Twenty-second detailed-prompt cinematography tests — Jerrod Lew

- **Creator:** [Jerrod Lew (@jerrod_lew)](https://x.com/jerrod_lew)
- **Published:** 2026-07-24
- **Verification source:** [Secondary mirror preserving the original creator post and attached video](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** The mirrored original post explicitly states that Lew had been testing FLUX 3 and introduces his own example generations.
- **Summary:** A set of creator-made FLUX 3 tests focused on full 20-second generations, detailed scene direction, and cinematic shot construction.
- **Workflow/details:** Lew reports that the model responds well to detailed prompts and produces especially strong cinematography across the attached examples. The publicly indexed mirror preserves the creator handle, post wording, video attachment marker, and engagement snapshot.
- **Prompt provenance:** `not_provided` — the creator discusses detailed prompting but no verbatim generation prompt is visible in the verified mirror, so none has been reconstructed.
- **Why included:** Original early-access creator output rather than a compilation account, explicit FLUX 3 attribution, multiple video examples, a full-length 20-second stress test, and a useful creator observation about detailed direction and camera quality.

### 9. Quadratic-equation reasoning inside a generated video — @dingchilling

- **Creator:** [@dingchilling](https://x.com/dingchilling)
- **Published:** 2026-07-24
- **Verification sources:** [Secondary mirror preserving the original post text and video marker](https://www.sotwe.com/Ridho_Mrr) · [Independent mirror of the same creator post](https://www.twstalker.com/CoffeeVectors)
- **Model attribution:** The creator explicitly states that the video was created with FLUX 3 by Black Forest Labs.
- **Summary:** A generated character solves a quadratic equation on screen without the solution being supplied, testing whether FLUX 3 can combine visual generation, legible mathematical writing, sequential reasoning, and temporal consistency in one video.
- **Workflow/details:** The creator says the instruction only asked the character to solve the equation and did not provide the answer. The verified mirrors preserve the original creator handle, explicit FLUX 3 attribution, attached-video marker, and the creator’s statement that the solution emerged in the generated output.
- **Prompt provenance:** `mentioned_not_in_post` — the post characterizes the instruction as simply asking the character to solve the equation, but does not expose the exact prompt wording; no verbatim prompt has been invented.
- **Why included:** A highly distinctive capability test beyond cinematic aesthetics, with explicit creator attribution and evidence of sustained symbolic content, readable text, and apparently self-generated intermediate reasoning inside a video sequence.

## How updates work

The hourly ChatGPT task checks this README first, searches for newer qualifying sources, rejects duplicates and ambiguous attribution, then appends verified entries here. It reports only when at least one new entry has been successfully committed.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Repository text and curation structure are licensed under the [MIT License](LICENSE). Linked post text, prompts, media, creator names, and other third-party material remain the property of their respective authors.