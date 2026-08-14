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

_Last updated: 2026-08-14 · Entries: 109_

### 1. Multi-shot realism favorites — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/venturetwins/status/2080318877154852912)
- **Model attribution:** Explicitly identified by the creator as FLUX 3.
- **Summary:** Favorite early-access generations emphasizing realistic details and multi-shot clips lasting up to 20 seconds from one prompt.
- **Workflow/details:** Text-to-video; one prompt across multiple shots, up to 20 seconds.
- **Prompt provenance:** `not_provided` — the prompt is not visible and has not been inferred.
- **Why included:** Original creator/tester examples with convincing realism and multi-shot continuity.

### 2. Official FLUX 3 Video early-access showcase — Black Forest Labs

- **Creator:** [Black Forest Labs (@bfl_ai)](https://x.com/bfl_ai)
- **Published:** 2026-07-23
- **Original source:** [FLUX 3 launch article and official showcase](https://bfl.ai/blog/flux-3)
- **Model attribution:** Official Black Forest Labs release showcase for FLUX 3 Video.
- **Summary:** Native-audio examples spanning text-to-video, image-to-video, reference transfer, continuation, keyframe transitions, dialogue, typography, and multi-shot chaining.
- **Workflow/details:** Text, image, video, and audio references; clips up to 20 seconds; preliminary evaluation used 10-second 720p clips with audio.
- **Prompt provenance:** `not_provided` — no verified prompt is published for each showcased clip.
- **Why included:** Definitive first-party source with broad multimodal capability coverage.

### 3. First-person mech vs. kaiju action test — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/cfryant/status/2080379186783379947)
- **Model attribution:** Explicitly labeled by the creator as a FLUX 3 early-access test.
- **Summary:** GoPro-style POV footage from inside a giant mech fighting a kaiju in Seattle, ending with the Space Needle used as a weapon.
- **Workflow/details:** Text-to-video test of POV coherence, scale, action staging, and landmark handling.
- **Prompt provenance:** `not_provided` — scene wording was not labeled as the exact prompt.
- **Why included:** Ambitious first-person choreography and large-scale physical interaction.

### 4. One-shot rally-car avalanche chase — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/umesh_ai/status/2080332510358282688)
- **Model attribution:** Explicitly presented as an early FLUX 3 test.
- **Summary:** A rally car races along a narrow alpine cliff road while an avalanche closes in.
- **Workflow/details:** A 15-second continuous shot with no cuts, morphing, or scene transitions.
- **Prompt provenance:** `verbatim_in_post` — “Hyper realistic blockbuster cinematic 15 second action sequence in one true unbroken continuous shot, with no cuts, no morphing, and no scene transitions.”
- **Why included:** Visible prompt, complex action choreography, environmental physics, and sustained continuity.

### 5. Predicted future vs. real robot rollout — Black Forest Labs × mimic robotics

- **Creator:** [Black Forest Labs](https://bfl.ai/) and [mimic robotics](https://www.mimicrobotics.com/)
- **Published:** 2026-07-23
- **Original source:** [FLUX 3 × mimic technical showcase](https://bfl.ai/blog/flux-3-mimic)
- **Model attribution:** Official FLUX-mimic video-action model built on the FLUX 3 backbone.
- **Summary:** Predicted visual futures are shown beside real robot rollouts, including recovery after missed grasps and factory manipulation.
- **Workflow/details:** A lightweight action decoder uses intermediate video-prediction features; the optimized system is reported to react in 101 ms.
- **Prompt provenance:** `not_provided` — this is a robotics demonstration rather than a text-prompt example.
- **Why included:** First-party evidence of video-model physics transferring into physical action.

### 6. Mongolia visual-language stress test — Christian Hartmann / CHAIPEAU™

- **Creator:** [Christian Hartmann](https://de.linkedin.com/in/chrtmn) / [CHAIPEAU™](https://www.chaipeau.com/)
- **Published:** 2026-07-25
- **Original source:** [Creator post embedded in a LinkedIn reshare](https://de.linkedin.com/posts/dr-tristan-behrens-734967a2_wir-sind-sowas-von-zur%C3%BCck-schaut-mal-was-activity-7486362273700020224-5_eY)
- **Model attribution:** The official BFL creator-team member says all 20 scenes were generated with FLUX 3.
- **Summary:** Twenty Mongolia-inspired stills become a coherent audiovisual production with a controlled palette, lighting, grain, haze, and 2.39:1 composition.
- **Workflow/details:** Director-style scene briefs, defined camera moves, continuous 20-second takes, native sound, letterboxing, and external assembly; simpler camera moves reduced motion drift.
- **Prompt provenance:** `mentioned_not_in_post` — complete prompts were said to be in comments but were not publicly visible.
- **Why included:** Detailed, reproducible multi-scene art-direction workflow and candid failure mitigation notes.

### 7. Native-audio and mixed-reference capability reel — cheaty

- **Creator:** [cheaty (@cheatyyyy)](https://x.com/cheatyyyy)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/cheatyyyy/status/2080314577385132290)
- **Model attribution:** Explicitly identified by the early-access creator as FLUX 3.
- **Summary:** Four videos demonstrate native audio, clips up to 20 seconds, and combined image, video, and audio references.
- **Workflow/details:** Mixed-modality conditioning with up to 10 reference assets.
- **Prompt provenance:** `not_provided` — no generation prompt is visible.
- **Why included:** Useful overview of native audio and reference conditioning from an original tester.

### 8. Twenty-second detailed-prompt cinematography tests — Jerrod Lew

- **Creator:** [Jerrod Lew (@jerrod_lew)](https://x.com/jerrod_lew)
- **Published:** 2026-07-24
- **Verification source:** [Secondary mirror preserving the creator post and video](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** The mirrored creator post explicitly says he was testing FLUX 3.
- **Summary:** Multiple 20-second generations focused on detailed scene direction and cinematic shot construction.
- **Workflow/details:** Lew reports strong response to detailed prompts and strong cinematography.
- **Prompt provenance:** `not_provided` — no verbatim prompt is visible in the mirror.
- **Why included:** Full-duration tests and a useful creator observation about detailed direction.

### 9. Quadratic-equation reasoning inside a generated video — @dingchilling

- **Creator:** [@dingchilling](https://x.com/dingchilling)
- **Published:** 2026-07-24
- **Verification sources:** [Creator-post mirror](https://www.sotwe.com/Ridho_Mrr) · [Independent mirror](https://www.twstalker.com/CoffeeVectors)
- **Model attribution:** The creator explicitly states that the video was made with FLUX 3.
- **Summary:** A generated character solves a quadratic equation on screen without the answer being supplied.
- **Workflow/details:** The instruction only asked the character to solve the equation, testing legible writing, sequential reasoning, and temporal consistency.
- **Prompt provenance:** `mentioned_not_in_post` — the exact instruction wording is not exposed.
- **Why included:** Distinctive test of symbolic content and apparent reasoning rather than aesthetics alone.

### 10. Scene-by-scene FLUX 3 montage — DΞV

- **Creator:** [DΞV (@junwatu)](https://x.com/junwatu)
- **Published:** 2026-07-25
- **Verification source:** [Secondary mirror preserving the creator post and video marker](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** The creator states every scene was made with FLUX 3.
- **Summary:** Independently generated scenes are selected and edited into one finished montage.
- **Workflow/details:** Generate scenes separately, curate the strongest outputs, and assemble them externally.
- **Prompt provenance:** `not_provided` — no scene prompt is visible.
- **Why included:** Clear practical workflow for producing a finished multi-scene piece.

### 11. “Mother of all prompts” audiovisual stress test — Yassine Yousfi

- **Creator:** [Yassine Yousfi (@yassineyousfi_)](https://x.com/yassineyousfi_)
- **Published:** 2026-07-24
- **Verification source:** [Secondary mirror preserving the creator post and video marker](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** The creator explicitly presents the output as FLUX 3.
- **Summary:** A comprehensive generation brief coordinates cinematic visuals and native sound.
- **Workflow/details:** Text-to-video with sound direction included in the same brief.
- **Prompt provenance:** `mentioned_not_in_post` — the comprehensive prompt is referenced but not visible.
- **Why included:** High-signal audiovisual prompt-coordination test.

### 12. Mountain-scale brutalist megastructure — Tanzim

- **Creator:** [Tanzim (@tanzim31)](https://x.com/tanzim31)
- **Published:** 2026-07-24
- **Verification source:** [Secondary mirror preserving the creator post and video marker](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** The creator identifies it as a FLUX 3 early-access test.
- **Summary:** A lone astronaut stands against a mountain-sized brutalist megastructure in a full 20-second output.
- **Workflow/details:** Text-to-video at the 20-second limit, focused on monumental scale and spatial coherence.
- **Prompt provenance:** `not_provided` — the scene description was not labeled as the exact prompt.
- **Why included:** Demanding long-duration architecture and scale-contrast test.

### 13. First-party synthetic launch film — Saksham Consul / Black Forest Labs

- **Creator:** [Saksham Consul (@TheNoise2Signal)](https://x.com/TheNoise2Signal), Black Forest Labs technical team
- **Published:** 2026-07-24
- **Verification source:** [Secondary mirror preserving the team-member post and video marker](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** Consul introduces FLUX 3 and states that none of the events in the attached film happened.
- **Summary:** A polished first-party film presents wholly synthetic scenes as the public launch reveal.
- **Workflow/details:** Team production across two continents; clip-level prompts and editing details are undisclosed.
- **Prompt provenance:** `not_provided` — no prompt or shot brief is visible.
- **Why included:** First-party production-level material with a clear synthetic-provenance statement.

### 14. Native-audio favorite-generation reel — Ostris

- **Creator:** [Ostris (@ostrisai)](https://x.com/ostrisai)
- **Published:** 2026-07-24
- **Verification source:** [Mirror on Robin Rombach’s profile](https://mobile.twstalker.com/robrombach)
- **Model attribution:** Ostris says he received FLUX 3 early access from Black Forest Labs.
- **Summary:** Four favorite audiovisual generations across several scene types.
- **Workflow/details:** Multiple early-access outputs with native audio; clip-level settings are unavailable.
- **Prompt provenance:** `not_provided` — no verbatim prompt is visible.
- **Why included:** Multiple outputs from an established model developer, amplified by a BFL co-founder.

### 15. Synchronized split-screen dual-camera test — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-24
- **Verification source:** [Mirror preserving the prompt excerpt and video](https://mobile.twstalker.com/robrombach)
- **Model attribution:** Explicitly labeled by the creator as a FLUX 3 split-screen test.
- **Summary:** One action is shown simultaneously from two camera positions in vertically divided panels.
- **Workflow/details:** Two equal panels with a static overhead view and a second angle of the same live action.
- **Prompt provenance:** `verbatim_in_post` — “Split-screen video showing the same real-time action from two different camera angles. The screen is divided vertically into two equal halves. On the left side, show a static, wide overhead view from a ceiling-mounted camera in the back…”
- **Why included:** Visible prompt and demanding synchronization across independent viewpoints.

### 16. Native scene-cut text-to-video test — A.I.Warper

- **Creator:** [A.I.Warper (@AIWarper)](https://x.com/AIWarper)
- **Published:** 2026-07-25
- **Verification source:** [Secondary mirror preserving the creator wording and video marker](https://www.twstalker.com/CoffeeVectors)
- **Model attribution:** The creator explicitly identifies the output as FLUX 3.
- **Summary:** A text-to-video experiment tests intentional scene cuts within one generation.
- **Workflow/details:** Generation focused on native transitions; exact settings are undisclosed.
- **Prompt provenance:** `not_provided` — no verbatim prompt is visible.
- **Why included:** Targeted test of editing grammar that complements continuous-shot examples.

### 17. Twenty-second Godzilla action sequence with native sound — Mark Kretschmann

- **Creator:** [Mark Kretschmann (@mark_k)](https://x.com/mark_k)
- **Published:** 2026-07-25
- **Verification source:** [Secondary mirror preserving the creator wording and video context](https://w.twstalker.com/zuesenergy)
- **Model attribution:** Kretschmann says FLUX 3 generated the 20-second video and sound.
- **Summary:** A giant-monster action sequence tests creature motion, destruction, scale, camera coherence, and audio.
- **Workflow/details:** Prompt-led 20-second generation with native sound.
- **Prompt provenance:** `not_provided` — no prompt is visible.
- **Why included:** Full-duration large-scale action and synchronized audio stress test.

### 18. 2003 nostalgia video study — MACBETH

- **Creator:** [MACBETH (@macbethAI)](https://x.com/macbethAI)
- **Published:** 2026-07-23
- **Original post:** [View on X](https://x.com/macbethAI/status/2080399545528459746)
- **Verification sources:** [Mirror on Robin Rombach’s profile](https://mobile.twstalker.com/robrombach) · [Archived discussion with video rehost](https://boards.4chan.org/g/thread/109353790)
- **Model attribution:** The creator explicitly captions the work “FLUX 3”; Robin Rombach amplified it.
- **Summary:** A nostalgia piece evokes the texture and emotional register of personal video memories from 2003.
- **Workflow/details:** Exact source ID and video evidence are preserved; settings are undisclosed.
- **Prompt provenance:** `not_provided` — the short concept caption is not labeled as a prompt.
- **Why included:** Distinctive everyday-memory aesthetic with strong provenance.

### 19. Exact-prompt community action showcase — ImagineArt

- **Creator:** [ImagineArt community / ImagineArt](https://www.imagine.art/)
- **Published:** Date not shown; first-party showcase verified 2026-07-26
- **Original source:** [FLUX 3 Community Creations](https://www.imagine.art/features/flux-3)
- **Model attribution:** The first-party page labels the section “FLUX 3 Community Creations.”
- **Summary:** Three embedded videos show a mounted knight, a motocross jump, and a sports car in snow.
- **Workflow/details:** Public prompt-to-video comparisons; duration, seed, references, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “A knight in full armor rides a white horse, sword raised, through a dramatic, motion-blurred landscape with fiery orange and dark, cloudy skies.” Two more exact prompts remain on the page.
- **Why included:** Multiple first-party embedded examples with exact prompt-to-output mappings.

### 20. Six-image reference montage in one generation — Jerrod Lew

- **Creator:** [Jerrod Lew (@jerrod_lew)](https://x.com/jerrod_lew)
- **Published:** 2026-07-25
- **Verification source:** [Secondary mirror preserving the creator wording and video marker](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** Lew explicitly states that FLUX 3 was prompted with multiple images.
- **Summary:** Six reference images are animated and joined into one 15-second generated video.
- **Workflow/details:** Six-image reference-to-video in a single prompt; the model animates each source and sequences the results.
- **Prompt provenance:** `not_provided` — the accompanying text prompt is not revealed.
- **Why included:** Reproducible multi-image conditioning and automatic sequencing test.

### 21. 1993 NYC breakdance reference-image test — A.I.Warper

- **Creator:** [A.I.Warper (@AIWarper)](https://x.com/AIWarper)
- **Published:** 2026-07-25
- **Verification sources:** [Creator-post mirror](https://www.sotwe.com/Ridho_Mrr) · [Independent prompt mirror](https://www.instalker.org/cocktailpeanut)
- **Model attribution:** Explicitly identified by the creator as FLUX 3.
- **Summary:** A reference character breakdances on cardboard on a crowded 1993 New York sidewalk.
- **Workflow/details:** Reference-image-to-video with action, prop, location, and year specified in text.
- **Prompt provenance:** `verbatim_in_post` — “Girl from the attached ref images is break dancing on a flattened cardboard box on a bustling NYC sidewalk in 1993”
- **Why included:** Fully visible prompt and demanding identity, dance, crowd, and period-style test.

### 22. First-person samurai duel in burning Kyoto — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-07-25
- **Verification source:** [Secondary mirror preserving the creator wording and video marker](https://www.sotwe.com/Ridho_Mrr)
- **Model attribution:** Fryant labels it a new FLUX 3 early-access test and tags Black Forest Labs.
- **Summary:** A first-person samurai duel unfolds inside a burning Kyoto temple during a clan war.
- **Workflow/details:** Text-to-video test of POV coherence, sword choreography, fire, smoke, and historical environment consistency.
- **Prompt provenance:** `not_provided` — the scene description is not explicitly labeled as the exact prompt.
- **Why included:** Demanding historical POV action that is distinct from the creator’s mech-versus-kaiju example.

### 23. Exact-prompt lipsync and multi-scene direction tests — Alexander S

- **Creator:** [Alexander S (@devdef)](https://x.com/devdef)
- **Published:** 2026-07-24
- **Verification source:** [Secondary creator-profile mirror preserving the full prompts and connected test posts](https://www.instalker.org/devdef)
- **Model attribution:** The creator publicly requested and received access from Black Forest Labs immediately before publishing the tests; the lipsync prompt explicitly makes the subject say that the video was generated by the “FLUX 3 neural network,” and the companion multi-scene test tags `@bfl_ai`.
- **Summary:** A static talking-head forest scene tests spoken English and precise lip synchronization, while a companion fantasy-action test uses timed scenes, deliberate cuts, camera instructions, combat choreography, and synchronized sound cues.
- **Workflow/details:** Prompt-only generation with static framing, no cuts or camera motion, stated 4K and 24 fps constraints, dialogue, and no subtitles or music; the action test is organized into timestamped scenes.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “A young woman in a bright yellow dress stands in the middle of a beautiful forest clearing… She says in English: ‘Hi, this video was generated by the FLUX 3 neural network.’” Full prompts remain in the source.
- **Why included:** Exact reproducible prompts, dialogue, lip synchronization, sound direction, and complementary multi-shot action testing.

### 24. “Brother Peter’s Choir” horror vignette — M★RS #AIAF

- **Creator:** [M★RS #AIAF (@mars_eve)](https://x.com/mars_eve)
- **Published:** 2026-07-25
- **Verification source:** [Secondary mirror directly preserving the original creator caption and engagement context](https://www.instalker.org/cocktailpeanut)
- **Model attribution:** The original creator’s caption explicitly includes `#flux3` and tags `@bfl_ai`.
- **Summary:** A compact choir-themed horror vignette titled “BROTHER PETER’S CHOIR” uses a macabre audiovisual concept rather than a generic demonstration reel.
- **Workflow/details:** The publicly preserved post confirms a FLUX 3 video concept, but does not disclose duration, references, seed, editing, or generation settings.
- **Prompt provenance:** `not_provided` — the title is not an explicitly labeled generation prompt.
- **Why included:** Original creator attribution, explicit FLUX 3 labeling, and distinctive concept-driven art direction.

### 25. Vague-prompt dialogue improvisation — Dreaming Tulpa

- **Creator:** [Dreaming Tulpa (@dreamingtulpa)](https://x.com/dreamingtulpa)
- **Published:** 2026-07-26
- **Verification sources:** [Secondary mirror preserving the creator’s wording and engagement context](https://twstalker.com/MudgilShreshth) · [Independent secondary mirror](https://www.twstalker.com/hradzka)
- **Model attribution:** The creator explicitly states that the dialogue test was generated with FLUX 3.
- **Summary:** A dialogue-driven clip demonstrates that FLUX 3 can improvise a coherent spoken performance from an extremely underspecified instruction.
- **Workflow/details:** Text-to-video with native dialogue; the actual wording and delivery are left to the model.
- **Prompt provenance:** `verbatim_in_post` — “ranting about ai”
- **Why included:** Exact visible prompt and a distinctive stress test of dialogue generation, semantic improvisation, voice delivery, and audiovisual coherence.

### 26. Four-way synchronized CCTV convenience-store test — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-26
- **Verification sources:** [Secondary mirror preserving the full creator post and attached-video context](https://www.instalker.org/KabookiAI) · [Independent mirror preserving the prompt opening and engagement](https://site.twstalker.com/nbykos)
- **Model attribution:** The original creator introduces the attached result with “This from Flux 3 is incredible!” and labels the following text as the prompt.
- **Summary:** A convenience-store event is rendered simultaneously through four fixed CCTV feeds, requiring the same people, actions, object positions, occlusions, timestamps, lighting, and physical reactions to remain synchronized across all views.
- **Workflow/details:** Four equal security-camera panels: ceiling-corner aisle view, overhead central-aisle view, checkout-facing view, and entrance-facing view. The staged action includes a customer taking a box, bumping a display, catching a bottle, checking out, and another shopper crossing behind.
- **Prompt provenance:** `verbatim_in_post` — “Four-way CCTV-style split-screen showing the same real-time event inside a convenience shop. Divide the frame into four equal security-camera views with timestamps.” The complete prompt remains visible in the verification source.
- **Why included:** Exact visible prompt and an unusually demanding multi-view temporal-consistency test covering identity, object permanence, occlusion, timestamps, physical causality, and synchronized action.

### 27. Reverse venue-setup timelapse from one reference photo — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-07-25
- **Verification source:** [Secondary profile mirror preserving the original creator wording and engagement context](https://site.twstalker.com/venturetwins)
- **Model attribution:** Moore explicitly states that the result was generated with FLUX 3.
- **Summary:** Starting from a single photograph of a finished event venue, FLUX 3 works backward to generate a continuous timelapse of staff building the space from an empty room.
- **Workflow/details:** Single-image reference-to-video; reverse temporal construction; one continuous timelapse; reported as a first-try output.
- **Prompt provenance:** `verbatim_in_post` — “generate a continuous timelapse of event staff setting this up from an empty room.”
- **Why included:** Exact visible prompt, a clear single-reference workflow, and an unusually strong test of reverse chronology, scene persistence, coordinated human activity, and long-range structural consistency.

### 28. One-prompt National Geographic-style documentary test — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-07-27
- **Verification source:** [Secondary profile mirror preserving the original creator wording, attached-video context, and engagement](https://site.twstalker.com/venturetwins)
- **Model attribution:** Moore explicitly says the video was made with FLUX 3.
- **Summary:** Moore says the result is strong enough that she is considering expanding the concept into a full National Geographic-style documentary.
- **Workflow/details:** A single-prompt FLUX 3 generation; the exact duration, input references, camera plan, and post-production details are not disclosed.
- **Prompt provenance:** `mentioned_not_in_post` — the creator states that the clip was made with one prompt, but the prompt text is not visible in the verified source.
- **Why included:** Explicit creator attribution, one-prompt workflow evidence, strong public engagement, and a high-signal documentary-style use case that differs from the existing venue timelapse and early-access realism reel.

### 29. Continuous LEGO X-wing construction timelapse — A.I.Warper

- **Creator:** [A.I.Warper (@AIWarper)](https://x.com/AIWarper)
- **Published:** 2026-07-25
- **Verification sources:** [Secondary mirror preserving the creator text, engagement, and video context](https://ngntipkolamrenang.twstalker.com/tdkardum) · [Independent secondary mirror](https://www.twstalker.com/DeepThinkerAI)
- **Model attribution:** The creator explicitly prefixes the exact prompt with “FLUX 3.”
- **Summary:** A child opens a LEGO set and builds a Star Wars X-wing from the unopened box to the completed model in one continuous generated timelapse.
- **Workflow/details:** Text-to-video; full assembly chronology; continuous-shot constraint; no cuts.
- **Prompt provenance:** `verbatim_in_post` — “a Timelapse video of a kid opening a Lego set and constructing a Star Wars X wing. Full timelapse from box opening to final constructed Lego X wing. Continuous shot with no cuts”
- **Why included:** Exact visible prompt and a difficult long-horizon test of object permanence, stepwise construction, temporal compression, hand-object interaction, and final-state consistency.

### 30. Twenty-second multi-shot cooking tutorial — Jerrod Lew

- **Creator:** [Jerrod Lew (@jerrod_lew)](https://x.com/jerrod_lew)
- **Published:** 2026-07-27
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-footage context, and engagement](https://ngntipkolamrenang.twstalker.com/jerrod_lew)
- **Model attribution:** Lew explicitly states that FLUX 3 made the 20-second cooking tutorial.
- **Summary:** A generated cooking lesson uses multiple shots within one 20-second clip, testing instructional sequencing, ingredient continuity, food handling, camera changes, and native audiovisual coherence.
- **Workflow/details:** Text-to-video at the 20-second limit with multi-shot prompting; Lew separately notes that the longer duration leaves room for more detailed timestamped shot direction.
- **Prompt provenance:** `not_provided` — no exact cooking prompt is visible in the verified source, and none has been inferred from the footage.
- **Why included:** Original creator wording, explicit FLUX 3 attribution, clear attached-footage context, strong early engagement, and a practical multi-shot instructional use case distinct from the existing cinematic and montage examples.

### 31. Exact-prompt alien-planet tracking shot — Jerrod Lew

- **Creator:** [Jerrod Lew (@jerrod_lew)](https://x.com/jerrod_lew)
- **Published:** 2026-07-27
- **Verification source:** [Secondary creator-profile mirror preserving the exact prompt and FLUX 3 attribution](https://ngntipkolamrenang.twstalker.com/jerrod_lew)
- **Model attribution:** Lew explicitly introduces the text as “the prompt for the video on FLUX 3.”
- **Summary:** A lone astronaut crosses a mist-covered alien plain at bleak daybreak in a restrained photorealistic sequence centered on atmosphere, grounded movement, and environmental continuity.
- **Workflow/details:** Text-to-video in 16:9; slow low waist-height tracking from behind; worn spacesuit continuity; volumetric fog, subtle particles, footprints, suit sounds, natural film grain, and explicit negative constraints excluding glossy CGI, game-engine aesthetics, fast action, sudden cuts, creatures, and spaceships.
- **Prompt provenance:** `verbatim_in_post` — “Cinematic ultra-realistic video scene, 16:9 widescreen, bleak daybreak on an alien planet, a lone astronaut walking slowly across a vast mist-covered plain of dark volcanic dust and pale fractured stone…” The complete prompt remains visible in the verification source.
- **Why included:** Exact reproducible prompt, explicit FLUX 3 attribution, unusually detailed cinematography and negative constraints, and a high-signal test of meditative pacing, environmental persistence, subtle body motion, and photorealistic atmosphere.

### 32. Multilingual and accent-switching dialogue in one 20-second clip — cocktail peanut

- **Creator:** [cocktail peanut (@cocktailpeanut)](https://x.com/cocktailpeanut)
- **Published:** 2026-07-25
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, video context, and engagement](https://twstalker.com/cocktailpeanut)
- **Model attribution:** The creator explicitly states that the 20-second video was generated with FLUX 3.
- **Summary:** A single clip switches among Japanese, American-accented English, and Japanese-accented English, testing multilingual speech, accent control, turn-to-turn continuity, lip synchronization, and native audiovisual timing.
- **Workflow/details:** One 20-second FLUX 3 dialogue generation containing multiple languages and accent variants; the source does not disclose reference media, seed, or post-production.
- **Prompt provenance:** `not_provided` — the exact generation prompt is not visible in the verified source and has not been inferred.
- **Why included:** Original creator wording, explicit model attribution, clear video duration, strong public engagement, and an unusually focused stress test of multilingual dialogue and accent switching within one continuous audiovisual output.

### 33. Scottish Highlands weather-and-dialogue cut — Jerrod Lew

- **Creator:** [Jerrod Lew (@jerrod_lew)](https://x.com/jerrod_lew)
- **Published:** 2026-07-27
- **Verification source:** [Secondary creator-profile mirror preserving the exact prompt and adjacent FLUX 3 thread context](https://ngntipkolamrenang.twstalker.com/jerrod_lew)
- **Model attribution:** Lew's adjacent posts explicitly identify the workflow as multi-shot prompting in FLUX 3, and the preserved prompt belongs to the showcased Scottish Highlands video thread.
- **Summary:** A stormy cliffside scene starts wide on a woman overlooking rough Scottish seas, then cuts to a side angle as she turns toward camera and delivers a short line in a Scottish accent.
- **Workflow/details:** Text-to-video prompt controlling overcast weather, strong wind, hair motion, Scottish Highlands location, a wide-to-side scene cut, and regional-accent dialogue; duration and generation settings are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Cinematic movie scene, an overcast, windy and storm day, a woman with a Scottish accent stands on the top of a cliff…” The complete prompt remains visible in the verification source.
- **Why included:** Exact reproducible prompt and a focused test of scene cutting, accent-controlled dialogue, facial performance, wind-driven motion, and atmospheric continuity within one FLUX 3 generation.

### 34. Magical fantasy battle vignette — Jerrod Lew

- **Creator:** [Jerrod Lew (@jerrod_lew)](https://x.com/jerrod_lew)
- **Published:** 2026-07-26
- **Verification source:** [Secondary creator-profile mirror preserving the original creator caption, attached-video context, and engagement](https://ngntipkolamrenang.twstalker.com/jerrod_lew)
- **Model attribution:** Lew explicitly captions the attached video “Created with FLUX 3.”
- **Summary:** A concise fantasy-action vignette built around a magical battle.
- **Workflow/details:** The source confirms a FLUX 3 video output, but does not disclose duration, input references, scene breakdown, camera plan, seed, or post-production.
- **Prompt provenance:** `not_provided` — “A magical battle” is a title or scene description, not an explicitly labeled generation prompt, and no prompt has been inferred.
- **Why included:** Direct creator attribution preserved by a public mirror, attached-video context, a distinct fantasy-combat use case, and meaningful public engagement.

### 35. 1970s self image-reference consistency and safety-behavior test — Dennis Schöneberg

- **Creator:** [Dennis Schöneberg](https://www.linkedin.com/in/dennis-sch%C3%B6neberg-3420a2221/)
- **Published:** 2026-07-24
- **Verification source:** [Secondary LinkedIn profile page embedding the original creator post](https://de.linkedin.com/in/jakob-poerschmann)
- **Model attribution:** Schöneberg says Black Forest Labs gave him early access to the new FLUX 3 video model and explicitly tags the post `#FLUX3` and `#AIVideo`.
- **Summary:** An image-reference experiment turns the creator into a consistent 1970s character across different scenes and shots; a separate misinformation probe shows the model correcting false claims or visibly marking the generated video as fiction.
- **Workflow/details:** Upload one reference image in Image Reference Mode to preserve character identity across shots, explore high seed variance through rerolls, and test how the model handles intentionally false-news instructions.
- **Prompt provenance:** `not_provided` — the creator describes the tests and outcomes but does not publish the exact generation prompts.
- **Why included:** Explicit early-access attribution, a concrete and reproducible reference-image workflow, multi-shot character-consistency evidence, candid observations about seed variance and prompt adherence, and a distinctive safety-behavior test.

### 36. Single-generation gym interview with native audio — Gökay Gökay

- **Creator:** [Gökay Gökay (@gokayfem)](https://x.com/gokayfem)
- **Published:** Creator-post date not exposed; secondary verification published 2026-07-27
- **Verification source:** [Credible secondary LinkedIn post embedding the clip and crediting the original creator](https://au.linkedin.com/in/andrew-adams2)
- **Model attribution:** Andrew Adams explicitly identifies the embedded clip as fully generated by FLUX 3 and credits it to `@gokayfem` on X.
- **Summary:** A documentary-style gym interview combines a subject with one dramatically oversized arm, handheld camerawork, an interviewer and microphone, and synchronized location audio.
- **Workflow/details:** Reported as one FLUX 3 generation with picture and native audio produced together; the source specifically notes the gym environment, interview staging, handheld camera feel, microphone audio, and dialogue synchronization. Exact duration, references, seed, resolution, and post-production are not disclosed.
- **Prompt provenance:** `not_provided` — neither the original prompt nor generation settings are visible in the verified public source, and nothing has been inferred from the footage.
- **Why included:** A traceable credited creator, explicit FLUX 3 attribution, embedded video evidence, and an unusually convincing single-pass test of documentary realism, coordinated human interaction, body deformation, handheld camera language, and synchronized speech and ambience.

### 37. Image-annotation-guided reference-video test — A.I.Warper

- **Creator:** [A.I.Warper (@AIWarper)](https://x.com/AIWarper)
- **Published:** 2026-07-28 verification date; the mirror exposes only a relative source timestamp.
- **Verification source:** [Secondary profile mirror preserving the original creator wording and engagement, amplified by Black Forest Labs co-founder Andreas Blattmann](https://twstalker.com/andi_blatt)
- **Model attribution:** The original creator explicitly states that FLUX 3 understands image annotations; Blattmann reshared the demonstration from his BFL-affiliated account.
- **Summary:** A reference-driven video demonstrates FLUX 3 following spatial guidance drawn directly onto source imagery, while also revealing that the red guide line remained visible in the generated result.
- **Workflow/details:** Image/reference-to-video using annotated source images. The creator says the prompt and source images are in the first comment and candidly notes that the prompt should also have instructed the model to remove or not render the red annotation line.
- **Prompt provenance:** `mentioned_not_in_post` — the creator points to a prompt in the first comment, but its text is not visible in the verified public source, so nothing has been copied or inferred.
- **Why included:** A distinctive and reproducible spatial-control workflow, transparent failure analysis, explicit FLUX 3 attribution, attached demonstration context, and amplification by a Black Forest Labs co-founder.

### 38. Realistic FLUX 3 lip-sync showcase — Rebel AI

- **Creator:** [Rebel AI (@realrebelai)](https://x.com/realrebelai)
- **Published:** 2026-07-24 (based on the verification mirror’s relative timestamp)
- **Original video:** [Watch on YouTube](https://youtu.be/UlH6TVHw990)
- **Verification source:** [Secondary mirror preserving the original creator wording, direct video link, and engagement context](https://w.twstalker.com/wildmindai)
- **Model attribution:** The creator explicitly states that the showcased output was generated with FLUX 3 and describes it as their best result from the model so far.
- **Summary:** A close-up spoken-performance test emphasizes realistic mouth movement and synchronized lip motion rather than broad cinematic spectacle.
- **Workflow/details:** Creator-generated FLUX 3 video shared through a direct YouTube link; the verified public post specifically highlights lip-sync quality and realistic mouth articulation. Duration, prompt, references, seed, resolution, and post-production are not disclosed.
- **Prompt provenance:** `not_provided` — no generation prompt or settings are visible in the verified source, and nothing has been inferred from the footage.
- **Why included:** Original creator attribution, a direct traceable video link, explicit FLUX 3 labeling, strong engagement, and a focused high-signal test of speech-driven facial motion and lip synchronization.

### 39. Split-camera consistency test — Rebel AI

- **Creator:** [Rebel AI (@realrebelai)](https://x.com/realrebelai)
- **Published:** 2026-07-26 (based on public mirrors’ relative timestamps)
- **Verification sources:** [Public LinkedIn repost preserving the embedded clip and FLUX 3 split-camera caption](https://pk.linkedin.com/in/merashidminhas/hi) · [Independent mirror on Black Forest Labs co-founder Andreas Blattmann’s profile preserving the original Rebel AI attribution and engagement](https://twstalker.com/andi_blatt)
- **Model attribution:** The original creator explicitly captions the video “FLUX 3 split camera testing.”
- **Summary:** A split-camera generation tests whether concurrent camera views can remain visually coherent within one FLUX 3 output.
- **Workflow/details:** Split-camera FLUX 3 video test; the exact panel layout, prompt, duration, reference inputs, seed, and post-production are not disclosed in the verified public sources.
- **Prompt provenance:** `not_provided` — the descriptive caption is not labeled as the generation prompt, and no prompt has been inferred.
- **Why included:** Explicit creator attribution, embedded-video verification across two public sources, amplification by a Black Forest Labs co-founder, strong public engagement, and a focused multi-view consistency test distinct from the creator’s lip-sync showcase.

### 40. Split-screen dramatic-irony hedge-and-dog reveal — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-27 (based on the verification mirror’s relative timestamp)
- **Verification source:** [Secondary mirror preserving the original creator wording, full prompt, and engagement context](https://instalker.org/_shift_MIND)
- **Model attribution:** Umesh explicitly attributes the result to FLUX 3's split-screen rendering.
- **Summary:** Two synchronized viewpoints follow a woman beside an opaque hedge: the ground-level view hides a dog approaching from the far side, while the aerial view makes their meeting at a hedge gap predictable, turning one event into surprise versus dramatic inevitability.
- **Workflow/details:** A 15-second vertical split-screen with identical timing, identity, and action across a shoulder-height tracking view and a top-down drone view; strict visibility rules keep the dog out of the left panel until the reveal. The creator reports upscaling the result with Topaz Astra.
- **Prompt provenance:** `verbatim_in_post` — “Split-screen video. Two equal vertical halves. Both halves show the SAME event, at the SAME time, frame-synchronized, filmed by two different cameras.” The complete prompt remains visible in the verification source.
- **Why included:** Exact visible prompt, explicit model attribution, strong engagement, and a distinctive storytelling test of synchronized identity, occlusion, viewpoint-dependent information, timed reveal, and emotional payoff.

### 41. One-prompt flat-vector video stylization — Purz.ai

- **Creator:** [Purz.ai (@PurzBeats)](https://x.com/PurzBeats)
- **Published:** 2026-07-26 (based on the public mirrors’ relative timestamps)
- **Verification sources:** [Secondary mirror on Robin Rombach’s profile preserving the original FLUX 3 post, video context, and engagement](https://mobile.twstalker.com/robrombach) · [Creator-profile mirror preserving the exact prompt follow-up](https://w.twstalker.com/PurzBeats)
- **Model attribution:** The original creator captions the showcased video “Flux 3 is pretty great”; Black Forest Labs co-founder Robin Rombach reshared it.
- **Summary:** A source video is transformed into a flat-vector illustration treatment while preserving its underlying motion and scene structure.
- **Workflow/details:** Video-to-video stylization from a single text instruction; the creator says no additional reference asset was used.
- **Prompt provenance:** `verbatim_in_post` — “Convert the video into a Flat Vector Illustration style.”
- **Why included:** Exact visible prompt, explicit creator attribution, strong engagement, first-party workflow clarification, and a distinctive reusable video-editing example rather than another text-to-video showcase.

### 42. First-person time-travel pair: French Revolution and D-Day — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-07-28 (based on the public mirror’s relative timestamp)
- **Verification source:** [Secondary creator-profile mirror preserving the original wording and two attached-video items](https://twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly captions the post “More FLUX 3 time travel gopro footage” and tags Black Forest Labs.
- **Summary:** Two first-person GoPro-style historical recreations place the viewer inside the French Revolution and the World War II D-Day invasion.
- **Workflow/details:** Text-to-video historical-POV concept presented as two separate attached clips; duration, exact prompts, references, seeds, and post-production are not disclosed.
- **Prompt provenance:** `not_provided` — the caption describes the outputs but is not labeled as the exact generation prompt, and nothing has been inferred.
- **Why included:** Explicit creator attribution, newly published attached-video evidence, and a demanding expansion of the creator’s time-machine series into crowd-scale upheaval, battlefield action, period detail, and first-person environmental continuity.

### 43. Cinematic movie-scene showcase — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-07-27 (based on the public mirror’s relative timestamp)
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, and engagement](https://twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly describes the attached output as one of the most cinematic FLUX 3 videos he has generated and tags Black Forest Labs.
- **Summary:** A standalone generation is presented as a production-oriented cinematic test that the creator says could plausibly appear in a movie scene.
- **Workflow/details:** Creator-generated FLUX 3 video focused on cinematic scene quality; the publicly indexed source does not expose the exact subject, prompt, duration, references, seed, resolution, or post-production.
- **Prompt provenance:** `not_provided` — no prompt text is visible in the verified public source, and nothing has been inferred from the footage.
- **Why included:** Explicit original-creator attribution, attached-video verification, strong public engagement, and a clear creator assessment that the output reaches movie-scene-level cinematic quality.

### 44. Single-still automatic seven-camera architectural coverage — Ryan Phillips

- **Creator:** [Ryan Phillips](https://www.linkedin.com/in/ryphil)
- **Published:** 2026-07-27 (based on the secondary verification page’s relative timestamp)
- **Verification source:** [Secondary LinkedIn profile embedding and quoting the original creator post](https://si.linkedin.com/in/luka-tisler)
- **Model attribution:** Phillips explicitly says he received early access to FLUX 3 Video from Black Forest Labs.
- **Summary:** One architectural hero still becomes a 20-second sequence with six additional camera angles, while sound and music are generated in the same pass.
- **Workflow/details:** Single-image reference into FLUX 3 Video through the early-access Discord workflow; automatic multi-camera coverage from one still; seven views total; native sound and music. Phillips reports that building geometry and materials remained coherent enough to make the workflow useful, while candidly noting that the output resolution was soft and that generation-time data was not yet available.
- **Prompt provenance:** `mentioned_not_in_post` — the creator says the prompt was simple and offers to share its structure in comments, but no prompt text is visible in the verified public source.
- **Why included:** Explicit original-creator attribution, a traceable embedded post, unusually concrete workflow details, and a production-relevant stress test of architectural geometry, material persistence, automatic camera coverage, 20-second continuity, and native audio from a single still.

### 45. Multi-style character-consistency and matching-audio reel — Dennis Schöneberg

- **Creator:** [Dennis Schöneberg](https://www.linkedin.com/in/dennis-sch%C3%B6neberg-3420a2221/)
- **Published:** 2026-07-28 (based on the secondary verification page’s relative timestamp)
- **Verification source:** [Secondary LinkedIn profile embedding and quoting the original creator post](https://de.linkedin.com/in/reinhard-patzschke-43206439)
- **Model attribution:** Schöneberg explicitly identifies the clips as FLUX 3 experiments, thanks Black Forest Labs for access, and tags the post `#FLUX3` and `#AIVideo`.
- **Summary:** A multi-clip reel ranges from cinematic drama and a science-fiction meteor panic to hand-drawn anime and a deliberately comic 3D guacamole commercial.
- **Workflow/details:** Multiple early-access FLUX 3 video generations spanning sharply different visual styles; Schöneberg specifically reports consistent characters and matching generated audio across the tests. Clip-level duration, reference inputs, seeds, prompts, and post-production are not disclosed.
- **Prompt provenance:** `not_provided` — the creator describes the concepts and outcomes but does not publish exact generation prompts.
- **Why included:** A newly published, explicitly attributed creator reel with broad style coverage, synchronized audio, and cross-shot character-consistency evidence that is distinct from Schöneberg’s previously listed 1970s reference-image and safety-behavior tests.

### 46. Frame-synchronized waterline and underwater bicycle recovery — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-28 (based on the verification mirror’s relative timestamp)
- **Original source profile:** [Umesh on X](https://x.com/umesh_ai) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the full original wording, exact prompt, attached-video context, and engagement](https://site.twstalker.com/umesh_ai)
- **Model attribution:** Umesh explicitly captions the result “Flux 3 is incredible at split screen generations!” and tags Black Forest Labs.
- **Summary:** A fisherman pulling a submerged bicycle is shown simultaneously above and below the waterline, with rope tension, rocking boat, snag release, fish movement, splash timing, and the bicycle crossing the surface synchronized across both views.
- **Workflow/details:** A 15-second text-to-video generation with two equal vertical halves, one continuous take, no cuts, and frame-perfect synchronization. The left panel is a water-level camera that never sees below the surface; the right is an underwater camera that reveals the bicycle and weeds. The creator reports upscaling the result with Topaz Astra.
- **Prompt provenance:** `verbatim_in_post` — “15-second split-screen video, two equal vertical halves, one continuous take, no cuts. Both cameras show the same event at the same time, perfectly frame-synchronized. Scene: Calm lake at dusk. An old fisherman in a small wooden rowboat pulls a rope from the water.” The complete prompt remains visible in the verification source.
- **Why included:** Exact reproducible prompt, explicit FLUX 3 attribution, visible attached-video context, and an unusually demanding test of cross-view causality, occlusion, object permanence, water-surface continuity, physical timing, and synchronized motion.

### 47. Frame-synchronized nursery and baby-monitor mirror — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-29 (based on the verification mirror’s relative timestamp)
- **Original source profile:** [Umesh on X](https://x.com/umesh_ai) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the full original wording, exact prompt, attached-video context, and engagement](https://site.twstalker.com/umesh_ai)
- **Model attribution:** Umesh explicitly captions the result “More experiments with split screens on Flux 3!”
- **Summary:** A mother warming a bottle in a downstairs kitchen watches a grainy black-and-white baby monitor while a synchronized full-color nursery view shows the same crib, mobile, sleeping baby, opening door, and cat reveal frame by frame.
- **Workflow/details:** A 15-second text-to-video generation with two equal vertical halves, one continuous take, and no cuts. The left side contains only the kitchen and the monitor; the right is the actual nursery from the monitor’s matching camera position. The prompt requires zero lag, identical nursery motion in both views, a monochrome low-resolution transformation inside the embedded monitor, and a timed suspense-to-relief sequence.
- **Prompt provenance:** `verbatim_in_post` — “15-second split-screen video, two equal vertical halves, one continuous take, no cuts. Both cameras show the same event at the same time, perfectly frame-synchronized. Scene: A house at night. A nursery upstairs; a kitchen downstairs.” The complete prompt remains visible in the verification source.
- **Why included:** Exact reproducible prompt, explicit FLUX 3 attribution, visible attached-video context, and a demanding nested-view consistency test combining frame synchronization, embedded-screen fidelity, color-to-monochrome transformation, occlusion, timed causality, and emotional storytelling.

### 48. VHS-to-IMAX camera-quality transition — Kadeka

- **Creator:** [Kadeka (@Berserkr_777)](https://x.com/Berserkr_777)
- **Published:** Date not exposed; verified 2026-07-29
- **Verification source:** [Secondary creator-profile mirror preserving the original Kadeka post and attached-video context](https://site.twstalker.com/dreamingtulpa)
- **Model attribution:** Kadeka explicitly states that “Flux 3 understands different camera pretty well” and describes switching from VHS to IMAX quality.
- **Summary:** The demonstration shifts from lo-fi VHS-style capture to an IMAX-like cinematic presentation, testing whether a scene can remain coherent through a pronounced change in apparent camera system and image quality.
- **Workflow/details:** Creator-reported FLUX 3 camera-format transition from VHS to IMAX quality. The public source does not disclose duration, exact prompt, reference inputs, seed, resolution, or post-production.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified source, and nothing has been inferred from the footage.
- **Why included:** Newly published original-creator attribution, attached-video verification, and a distinct, reusable stress test of camera-language switching, quality transformation, and scene continuity within one FLUX 3 output.

### 49. Twenty-second fluid-action comparison with candid failure notes — Mirochill

- **Creator:** [Mirochill (@mirochill)](https://x.com/mirochill)
- **Published:** 2026-07-28 (based on the secondary mirror’s relative timestamp)
- **Original source profile:** [Mirochill on X](https://x.com/mirochill) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary public mirror preserving the original creator wording, attached-video context, and engagement](https://twstalker.com/nodonmai)
- **Model attribution:** Mirochill explicitly says “J’ai essayé Flux 3” (“I tried Flux 3”) in the original caption.
- **Summary:** A 20-second creator test highlights smoother character actions than the creator observed with Seedance 2, while openly documenting visible failures including an oddly opening window and a character speaking into empty space.
- **Workflow/details:** One FLUX 3 video generation at the model’s 20-second duration; the creator provides a direct qualitative comparison with Seedance 2 and candidly identifies temporal and staging defects. Exact prompt, reference inputs, seed, resolution, and post-production are not disclosed.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified source, and nothing has been inferred from the footage.
- **Why included:** Explicit original-creator attribution, preserved attached-video context, substantial early engagement, a useful long-duration motion comparison, and unusually transparent failure analysis that makes the test reproducible as an evaluation target even without the prompt.

### 50. “Contaminated” AI-horror trailer — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-07-30 (based on the verification page’s relative timestamp)
- **Original source profile:** [Justine Moore on X](https://x.com/venturetwins) — the public index did not expose the direct status URL.
- **Verification source:** [Official Andreessen Horowitz creator profile embedding the original X post and attached-video link](https://a16z.com/author/justine-moore/)
- **Model attribution:** Moore explicitly says she has started making AI horror-movie trailers with Flux 3 and identifies the attached trailer as “Contaminated.”
- **Summary:** A concept-driven AI horror trailer titled “Contaminated,” presented as the first visible installment in an ongoing FLUX 3 trailer series.
- **Workflow/details:** Creator-produced FLUX 3 horror-trailer workflow; the verified source preserves the original caption and attached-video context, but does not disclose duration, exact prompt, reference inputs, seed, resolution, audio generation, editing, or post-production.
- **Prompt provenance:** `not_provided` — the title and caption describe the finished piece but are not labeled as the exact generation prompt, and nothing has been inferred from the footage.
- **Why included:** Explicit original-creator attribution, a traceable first-party profile embedding the video post, a newly published production-oriented use case, and distinctive horror-trailer storytelling that is separate from Moore’s existing documentary, reverse-timelapse, and early-access realism entries.

### 51. Park Chan-wook-style cinematic vignette — cocktail peanut

- **Creator:** [cocktail peanut (@cocktailpeanut)](https://x.com/cocktailpeanut)
- **Published:** Date not exposed; verified 2026-07-31
- **Original source profile:** [cocktail peanut on X](https://x.com/cocktailpeanut) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original caption, attached-video context, and engagement](https://twstalker.com/cocktailpeanut)
- **Model attribution:** The creator explicitly captions the video “Almost straight out of a Park Chan wook film #Flux3.”
- **Summary:** A cinematic generated vignette that the creator presents as approaching the visual language and production feel of a Park Chan-wook film.
- **Workflow/details:** Creator-posted FLUX 3 video; the publicly indexed source does not disclose duration, input mode, reference assets, exact prompt, seed, resolution, native-audio use, or post-production.
- **Prompt provenance:** `not_provided` — the caption is an aesthetic assessment rather than an explicitly labeled generation prompt, and nothing has been inferred from the footage.
- **Why included:** Explicit original-creator attribution, attached-video verification, meaningful public engagement, and a distinctive auteur-cinema quality benchmark that is separate from the creator’s existing multilingual dialogue test.

### 52. Persian-monologue native-dialogue quality test — Shahram Shahbazi

- **Creator:** [Shahram Shahbazi](https://ae.linkedin.com/in/nakoot)
- **Published:** 2026-07-30 (based on the original creator profile’s relative timestamp; exact time is not exposed)
- **Original source:** [Creator’s public LinkedIn profile post](https://ae.linkedin.com/in/nakoot)
- **Model attribution:** Shahbazi explicitly says he gave Flux 3 a prompt containing a Persian monologue and evaluates the resulting output.
- **Summary:** A Persian-language spoken-performance video tests whether generated native dialogue remains natural instead of drifting into garbled or foreign-sounding phonetics; the creator reports being surprised by the high quality of the Persian output.
- **Workflow/details:** Prompt-led FLUX 3 video with a Persian monologue and generated speech. Duration, exact prompt, reference inputs, seed, resolution, and post-production are not disclosed in the verified public source.
- **Prompt provenance:** `mentioned_not_in_post` — the creator states that the prompt contained a Persian monologue, but the exact prompt text is not visible and has not been reconstructed.
- **Why included:** Original-creator attribution, explicit Flux 3 labeling, a newly published generated-video test, strong early engagement, and a focused evaluation of native dialogue in an underrepresented language that is distinct from the existing Japanese/English accent-switching example.

### 53. GPU ASMR early-preview demonstration — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-07-31
- **Original post:** [View on X](https://x.com/venturetwins/status/2083018130255913366)
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, and engagement](https://site.twstalker.com/venturetwins)
- **Model attribution:** Moore explicitly calls the attached result a Flux 3 generation.
- **Summary:** A playful GPU-themed ASMR video uses computer hardware as the subject of an audio-first generative-media demonstration.
- **Workflow/details:** Moore reports that Flux 3 was available in an early preview through Nous Research’s Hermes Agent when she published the clip. The source does not expose the exact prompt, input mode, duration, references, seed, resolution, or post-production.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified source, and nothing has been inferred from the footage.
- **Why included:** Explicit original-creator attribution, a newly published attached video, a distinctive native-audio and tactile-sound use case, a publicly identified access workflow, and meaningful early engagement.

### 54. 1990s elementary-school computer-prediction footage — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-07-28
- **Original post:** [View on X](https://x.com/venturetwins/status/2081948871882911999)
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, and engagement](https://site.twstalker.com/venturetwins)
- **Model attribution:** Moore explicitly states that the historical-footage-style video was generated with Flux 3.
- **Summary:** Faux 1990s school footage shows elementary students predicting how people will use computers, combining period-specific visual language with an ensemble concept built around individual responses.
- **Workflow/details:** Creator-generated FLUX 3 historical-footage concept. The verified source does not disclose the exact prompt, duration, input references, seed, resolution, native-audio settings, or editing workflow.
- **Prompt provenance:** `not_provided` — the caption describes the concept but is not labeled as the exact generation prompt, and nothing has been inferred beyond the visible source wording.
- **Why included:** Explicit original-creator attribution, attached-video verification, exceptionally strong public engagement, and a distinctive stress test of period realism, ensemble consistency, documentary framing, and believable archival-video aesthetics.

### 55. Creepshow-style chained short-film workflow — Rebel AI

- **Creator:** [Rebel AI (@realrebelai)](https://x.com/realrebelai)
- **Published:** 2026-07-28
- **Original post:** [View on X](https://x.com/realrebelai/status/2082202785559536034)
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, and engagement](https://twstalker.com/realrebelai/status/2082202785559536034)
- **Model attribution:** The creator explicitly captions the attached horror clip “Creepshow... but FLUX 3 style.”
- **Summary:** A horror-anthology-style vignette is presented as evidence that FLUX 3 can produce material approaching a self-contained short-film scene.
- **Workflow/details:** The creator reports that feeding a generated video back into FLUX 3 supplies character and scene information, allowing additional clips to be chained together with cut scenes. Exact duration, prompt, reference assets, seed, resolution, and external editing are not disclosed.
- **Prompt provenance:** `not_provided` — the concept caption and workflow note are visible, but no exact generation prompt is published or inferred.
- **Why included:** Explicit original-creator attribution, preserved attached-video evidence, strong engagement, and an unusually actionable iterative video-reference workflow for maintaining characters and scene context across a longer sequence.

### 56. First-person grocery-store POV test — Rebel AI

- **Creator:** [Rebel AI (@realrebelai)](https://x.com/realrebelai)
- **Published:** 2026-07-28
- **Original post:** [View on X](https://x.com/realrebelai/status/2082233539580551234)
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, and engagement](https://twstalker.com/realrebelai/status/2082233539580551234)
- **Model attribution:** The creator explicitly introduces the attached first-person clip by saying “FLUX 3 has been really versatile so far.”
- **Summary:** A first-person point-of-view shot moves through a grocery-store environment, using an everyday retail scene rather than a stylized cinematic spectacle to test embodied camera perspective.
- **Workflow/details:** Creator-generated FLUX 3 first-person POV video. The verified source does not disclose the exact prompt, duration, input mode, reference media, seed, resolution, audio settings, or post-production.
- **Prompt provenance:** `not_provided` — the caption identifies the scene but is not labeled as the exact prompt, and nothing has been reconstructed from the footage.
- **Why included:** Explicit original-creator attribution, attached-video verification, strong public engagement, and a focused test of first-person camera motion, aisle geometry, object persistence, and environmental continuity in a familiar real-world setting.

### 57. Same-input FLUX.3 vs. MiniMax H3 comparison — Peter Baylies

- **Creator:** [Peter Baylies (@pbaylies)](https://x.com/pbaylies)
- **Published:** 2026-07-30
- **Original post:** [View on X](https://x.com/pbaylies/status/2082635748256199007)
- **Verification source:** [Secondary creator-profile mirror preserving the original caption, three attached media items, follow-up workflow notes, and engagement](https://site.twstalker.com/pbaylies/status/2082635748256199007)
- **Model attribution:** Baylies explicitly captions the comparison “FLUX.3 and Minimax H3; same reference photo and prompt used.”
- **Summary:** A controlled multimodal comparison applies the same reference image and prompt to FLUX.3 and MiniMax H3, allowing visual fidelity and instruction following to be evaluated against identical inputs.
- **Workflow/details:** The creator used the same prompt and reference photograph for both models, says the brief requested approximately four clips or scenes, and notes that the reference image likely came from an SDXL variant plus a character description. In follow-up comments he judges FLUX.3 stronger for realism and aesthetics, while H3 follows the multi-scene prompt more closely.
- **Prompt provenance:** `mentioned_not_in_post` — the creator repeatedly references the shared prompt and its four-scene structure, but the exact wording is not visible in the verified source and has not been reconstructed.
- **Why included:** Explicit original-creator attribution, an original post with attached model outputs, a genuinely controlled same-input workflow, and unusually candid comparative observations that isolate FLUX.3’s realism and aesthetic strengths from prompt-adherence weaknesses.

### 58. Synchronized road near-miss from aerial and roadside cameras — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-29
- **Original post:** [View on X](https://x.com/umesh_ai/status/2082488807606395005)
- **Verification source:** [Secondary creator-post mirror preserving the original caption, full prompt, downloadable video, and engagement](https://twstalker.com/umesh_ai/status/2082488807606395005)
- **Model attribution:** Umesh explicitly introduces the attached result with “Prompt on Flux 3.”
- **Summary:** A tense but collision-free road near-miss is shown simultaneously from a high aerial view and a fixed distant roadside camera, with the same car, truck, cyclist, spacing, dust, timing, and reactions required to match across both perspectives.
- **Workflow/details:** Text-to-video split-screen with two synchronized camera perspectives. The event is anchored at the 2-second mark; the prompt specifies a winding two-lane country road, realistic daylight, smooth motion, and strict cross-view consistency while explicitly avoiding a collision. Duration, seed, resolution, references, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Two-shot split-screen showing the same tense near-miss road moment from two different perspectives. Both shots happen at the same time and remain perfectly synchronized.” The complete prompt remains visible in the verification source.
- **Why included:** Explicit original-creator attribution, an attached downloadable video, a visible exact prompt, and a demanding outdoor multi-camera test of geometry, causality, object identity, timing, narrow-clearance staging, and synchronized environmental motion.

### 59. Six-reference-image single-prompt video test — Rebel AI

- **Creator:** [Rebel AI (@realrebelai)](https://x.com/realrebelai)
- **Published:** 2026-07-29
- **Original post:** [View on X](https://x.com/realrebelai/status/2082300801603584129)
- **Verification source:** [Secondary creator-profile mirror preserving the original caption, attached-result context, and engagement](https://twstalker.com/realrebelai)
- **Model attribution:** Rebel AI explicitly states, “I tested 6 input images in 1 prompt with FLUX 3.”
- **Summary:** One FLUX 3 generation conditions on six separate input images, testing whether the model can use a relatively dense set of visual references within a single video prompt.
- **Workflow/details:** Six image references supplied together in one prompt. The public source does not disclose the exact prompt text, clip duration, reference ordering, audio instructions, seed, resolution, or post-production.
- **Prompt provenance:** `not_provided` — the creator identifies the six-image setup but does not expose the accompanying generation prompt, and nothing has been inferred from the result.
- **Why included:** Explicit original-creator attribution, a direct traceable status URL, attached-result verification, and a compact, reproducible multi-reference stress test from an active FLUX 3 early-access tester.

### 60. Two-camera CCTV umbrella mishap comparison — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-29
- **Original post:** [View on X](https://x.com/umesh_ai/status/2082335273116147775)
- **Verification source:** [Secondary creator-post mirror preserving the full original caption, exact prompt, downloadable video, and engagement](https://twstalker.com/umesh_ai/status/2082335273116147775)
- **Model attribution:** Umesh explicitly says he tested the prompt across leading video models and that “Flux 3 is far ahead.”
- **Summary:** Two fixed convenience-store security cameras show the same comic incident: a customer’s umbrella opens indoors, bumps a snack display, and drops chip bags while shoppers and the cashier react.
- **Workflow/details:** Two equal fixed CCTV views with synchronized timestamps and no cinematic movement. The prompt requires matching people, clothing, umbrella, chip bags, object positions, lighting, and reactions across a ceiling-corner camera and a checkout-facing camera.
- **Prompt provenance:** `verbatim_in_post` — “Two-way CCTV split-screen showing the same harmless, funny incident inside a convenience shop. Divide the frame into two equal fixed security-camera views with perfectly synchronized timestamps.” The complete prompt remains visible in the verification source.
- **Why included:** Explicit original-creator attribution, a traceable original status URL, attached downloadable video, exact reproducible prompt, and a controlled same-event test of multi-camera identity, object permanence, physical causality, comic timing, and synchronized reactions.

### 61. Apocalyptic heatwave city realism test — Jin.B

- **Creator:** [Jin.B (@opener_ai)](https://x.com/opener_ai)
- **Published:** 2026-08-03
- **Original post:** [View on X](https://x.com/opener_ai/status/2084236317760925980)
- **Model attribution:** The creator labels the visible prompt section “[FLUX 3 FINAL PROMPT]” alongside the attached video result.
- **Summary:** A photorealistic city street is staged at peak afternoon during an extreme, apocalyptic heatwave, using a dense everyday urban environment as an environmental-realism stress test.
- **Workflow/details:** Text-to-video from a visible natural-language prompt establishing the city street, peak-afternoon timing, photorealism, and extreme-heat conditions. Duration, reference inputs, seed, resolution, native-audio instructions, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “A photorealistic city street at peak afternoon during an extreme, apocalyptic heatwave.” The complete prompt remains visible in the original post.
- **Why included:** Newly published original-creator source, explicit FLUX 3 labeling, attached-video context, an exact visible prompt excerpt, and a demanding test of photorealism, dense scene composition, atmosphere, and extreme-environment continuity.

### 62. Twenty-second handheld fennec-fox one-take — Jin.B

- **Creator:** [Jin.B (@opener_ai)](https://x.com/opener_ai)
- **Published:** 2026-08-02
- **Original post:** [View on X](https://x.com/opener_ai/status/2083730084394099176)
- **Model attribution:** The creator explicitly says “flux 3 made it!” and tags Black Forest Labs alongside the attached video.
- **Summary:** An amateur-handheld-style camera rapidly follows a tiny fennec fox through a quiet bedroom in one continuous 20-second take.
- **Workflow/details:** Text-to-video; 20-second duration; continuous single take; third-person handheld perspective; rapid follow-camera movement. Reference inputs, seed, resolution, native-audio instructions, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “20-second continuous single-take amateur handheld recording, third-person perspective.” The complete prompt remains visible in the original post.
- **Why included:** Explicit original-creator attribution, a visible exact workflow prompt, full-duration continuous motion, and a demanding test of small-subject tracking, handheld camera coherence, environmental continuity, and long-take temporal stability.

### 63. Faux 1957 interview predicting the technological future — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** 2026-08-05 (based on the public index timestamp)
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary profile mirror preserving the original creator attribution, prompt wording, attached-video context, and engagement](https://twstalker.com/nathanbenaich)
- **Model attribution:** The original creator explicitly prefixes the attached generation with “FLUX 3.”
- **Summary:** A faux archival color interview places a serious visionary in 1957 and has him accurately anticipate major technological developments through 2025, while a skeptical interviewer silently reacts.
- **Workflow/details:** Text-to-video framed as one uninterrupted period interview, with no on-screen text or shot changes. The verified source does not disclose duration, resolution, seed, reference assets, or post-production.
- **Prompt provenance:** `verbatim_in_post` — “a recently found color interview with a man in 1957, he predicts every major technological event with accuracy, up until 2025.” The remainder of the visible prompt specifies an uninterrupted serious interview and a silent, contemptuous interviewer.
- **Why included:** Explicit creator attribution, a visible reproducible prompt, attached-video verification, strong public engagement, and a distinctive stress test of period realism, sustained single-scene performance, character interaction, and narrative coherence.

### 64. Same-prompt FLUX 3 vs. Seedance 2.0 comparison — Jin.B

- **Creator:** [Jin.B (@opener_ai)](https://x.com/opener_ai)
- **Published:** 2026-08-05 (based on the public verification page’s relative timestamp)
- **Original source profile:** [Jin.B on X](https://x.com/opener_ai) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary public hashtag page preserving the original creator caption, attached downloadable video, model labels, and engagement](https://www.twstalker.com/hashtag/%23Seedance)
- **Model attribution:** Jin.B explicitly says the attached comparison tests “Flux 3 & Seedance 2.0” and tags `#Flux3`, Black Forest Labs, and Dreamina.
- **Summary:** The creator presents FLUX 3 and Seedance 2.0 outputs generated from the same creative brief, enabling a direct visual comparison rather than unrelated showcase clips.
- **Workflow/details:** One shared prompt was written with Claude Opus 5 and run through both FLUX 3 and Seedance 2.0; the source preserves the attached comparison video. Exact duration, input references, seeds, resolutions, audio settings, and post-production are not disclosed.
- **Prompt provenance:** `mentioned_not_in_post` — the creator says “Prompts👇,” but the prompt text is not visible in the verified public page and has not been inferred from the footage.
- **Why included:** Newly published original-creator attribution, an attached downloadable comparison, meaningful early engagement, and a controlled same-prompt benchmark that makes differences in cinematic interpretation and prompt execution easier to assess.

### 65. Thirty one-sentence 720p text-to-video experiments — Bennett Heyn / fal

- **Creator:** [Bennett Heyn](https://fal.ai/learn/tools/flux-3-video-examples-prompts), editor and original tester for fal
- **Published:** 2026-07-30
- **Original source:** [View the first-party fal testing guide with embedded clips and prompts](https://fal.ai/learn/tools/flux-3-video-examples-prompts)
- **Model attribution:** Heyn explicitly identifies every collected clip as generated with Black Forest Labs’ FLUX 3 after several days of direct testing.
- **Summary:** A 30-video test suite spans period documentaries, historical construction explainers, public-domain literary trailers, modern television scenes, music videos, and format-driven comedy, showing how short prompts can produce complete audiovisual sequences.
- **Workflow/details:** All examples are verified as 720p text-to-video with audio generated in the same pass. FLUX 3 supports 5-, 10-, 15-, and 20-second outputs in this workflow; the author says most examples use the full 20 seconds and almost all begin from a single sentence without shot lists, wardrobe notes, or lighting direction.
- **Prompt provenance:** `verbatim_in_post` — the source visibly publishes individual prompts, including “a 1969 documentary about Woodstock,” “How the great wall of china was made,” and “A nature documentary about shopping carts returning to the wild.”
- **Why included:** A traceable original tester and launch-platform source provides an unusually broad, reproducible corpus with embedded outputs, exact prompt text, verified resolution and generation mode, native-audio evidence, factual-sequence tests, typography, multi-shot editing, and clear prompting lessons.

### 66. Three-language conversation with generated subtitles — DΞV

- **Creator:** [DΞV (@junwatu)](https://x.com/junwatu)
- **Published:** 2026-08-02 (based on the secondary verification source’s relative timestamp)
- **Original source profile:** [DΞV on X](https://x.com/junwatu) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary mirror on Black Forest Labs co-founder Robin Rombach’s profile preserving the original creator wording and video context](https://site.twstalker.com/robrombach)
- **Model attribution:** The creator explicitly states that FLUX 3 generated the mixed-language scene.
- **Summary:** One conversational scene moves among English, Japanese, and Javanese while also rendering subtitles, testing speech, language switching, and on-screen text together.
- **Workflow/details:** A creator-generated FLUX 3 dialogue scene containing three spoken languages and subtitles. Duration, exact prompt, reference media, seed, resolution, subtitle instructions, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `not_provided` — no generation prompt is visible in the verified source, and nothing has been inferred from the video.
- **Why included:** Explicit original-creator attribution, attached-video context, amplification by a Black Forest Labs co-founder, and an unusually focused test combining multilingual native dialogue with subtitle generation, including the underrepresented Javanese language.

### 67. Twenty-second Korean-barbecue food realism test — DΞV

- **Creator:** [DΞV (@junwatu)](https://x.com/junwatu)
- **Published:** Date not exposed; verified 2026-08-06
- **Original source profile:** [DΞV on X](https://x.com/junwatu) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-post mirror preserving the original caption, exact prompt, attached-video context, and engagement](https://twstalker.com/ptmaster22)
- **Model attribution:** The creator explicitly introduces the attached result as “Exploring food in FLUX 3.”
- **Summary:** A woman eats bulgogi in a cozy Korean barbecue restaurant while meat sizzles on the tabletop grill, using an everyday dining scene to test photoreal food, human interaction, and restaurant atmosphere over a full-length clip.
- **Workflow/details:** Text-to-video; 20-second duration; 720p output; hyper-realistic cinematic treatment. The source does not disclose references, seed, aspect ratio, generation time, or post-production.
- **Prompt provenance:** `verbatim_in_post` — “A woman eating 불고기 at a cozy Korean barbecue restaurant while meat sizzles on the grill. Hyper-realistic cinematic movie. 20s. Resolution: 720p”
- **Why included:** Explicit original-creator attribution, an attached video, exact visible prompt and output settings, and a demanding food-realism test combining a human subject, eating motion, grill activity, material detail, and sustained 20-second scene coherence.

### 68. Frame-synchronized rainy café near-miss and glass catch — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-07-26
- **Original post:** [View on X](https://x.com/umesh_ai/status/2081376099519644043)
- **Verification source:** [Secondary mirror preserving the original creator wording, full prompt, attached-video context, and engagement](https://twstalker.com/dawngames2017)
- **Model attribution:** Umesh explicitly introduces the attached generation with “Prompt on Flux 3.”
- **Summary:** A rainy outdoor-café incident is shown simultaneously from a fixed elevated wide camera and a moving waist-level camera as a cyclist passes a waiter, a glass slides across a tilting tray, the waiter catches it, colored liquid spills, and a striped umbrella twists in the wind.
- **Workflow/details:** Text-to-video split-screen with two synchronized views. The left side keeps the full café terrace visible; the right tracks the waiter and uses brief foreground and arm occlusions. The prompt anchors the near-miss at the 2-second mark and requires matching identities, drink colors, hand positions, tray angle, liquid trajectory, umbrella motion, pavement reflections, weather, timing, and physical consequences across both cameras. Duration, seed, resolution, references, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Split-screen video showing the same continuous real-time event from two different camera angles. The screen is divided vertically into two equal halves. On the left side, show a static, elevated wide shot of an outdoor café terrace during light rain.” The complete prompt remains visible in the verification source.
- **Why included:** Explicit original-creator attribution, a traceable original status URL, an attached-video mirror, an exact reproducible prompt, strong public engagement, and an unusually demanding test of cross-view synchronization, occlusion, reflections, liquid physics, object permanence, and causal consistency.

### 69. Otter-on-an-airplane longitudinal benchmark variation — Ethan Mollick

- **Creator:** [Ethan Mollick (@emollick)](https://x.com/emollick)
- **Published:** 2026-08-06
- **Original source profile:** [Ethan Mollick on X](https://x.com/emollick) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary mirror preserving the original creator wording, attached-video context, quoted earlier benchmark, and engagement](https://www.twstalker.com/Ahmdnet2)
- **Model attribution:** Mollick explicitly calls the attached result a test of “the new Flux 3 video model” and says the model is “really good.”
- **Summary:** Mollick revisits his long-running benchmark of an otter using a laptop on an airplane, adds a variation that becomes apparent several seconds into the clip, and places it beside his two-year-old comparison point.
- **Workflow/details:** Creator-run FLUX 3 video benchmark using the recurring otter, laptop, and airplane concept; the post directly compares the new output with an earlier July 2024 generation. Duration, reference inputs, seed, resolution, native-audio instructions, and post-production are not disclosed.
- **Prompt provenance:** `mentioned_not_in_post` — the creator describes the benchmark concept and says the new clip is a variation, but the exact generation prompt is not visible and has not been reconstructed.
- **Why included:** Newly published original-creator attribution, attached-video verification, substantial early engagement, and a rare longitudinal benchmark that makes two years of progress in subject fidelity, lighting, scene coherence, motion, and surprise-driven staging directly comparable.

### 70. One-prompt microgravity nature documentary — Thomas the Cosmic / Black Forest Labs

- **Creator:** [Thomas the Cosmic (@thomasthecosmic)](https://x.com/thomasthecosmic), technical staff at Black Forest Labs
- **Published:** 2026-07-28
- **Original post:** [View on X](https://x.com/thomasthecosmic/status/2082111480900538608)
- **Verification source:** [Secondary public mirror preserving the original creator caption, status link, model attribution, and attached-video context](https://w.twstalker.com/thomasthecosmic)
- **Model attribution:** The creator explicitly says “FLUX 3 makes a microgravity nature documentary from one prompt” and tags Black Forest Labs.
- **Summary:** A nature-documentary-style scene depicts water and subjects behaving in microgravity, emphasizing surface tension, free-floating motion, and optical refraction through water.
- **Workflow/details:** Single-prompt FLUX 3 video generation. The creator specifically identifies surface tension, microgravity, water refraction, and coherence among those interacting details as the test targets. Duration, resolution, seed, reference inputs, native-audio instructions, and post-production are not disclosed.
- **Prompt provenance:** `mentioned_not_in_post` — the creator confirms that one prompt produced the video, but the exact prompt text is not visible in the verified source and has not been inferred.
- **Why included:** First-party team attribution, a traceable original status, attached-video verification, and a focused physical-coherence test combining fluid behavior, weightlessness, and refractive optics in one scene.

### 71. One-prompt 20-second self-edited voiceover sequence — VORTEX

- **Creator:** [VORTEX: AI Bros & AI Arena (@VORTEX_Promos)](https://x.com/VORTEX_Promos)
- **Published:** 2026-08-06 (based on the public verification page’s relative timestamp)
- **Original source profile:** [VORTEX on X](https://x.com/VORTEX_Promos) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, and engagement](https://twstalker.com/VORTEX_Promos)
- **Model attribution:** The creator explicitly introduces the attached result with “Flux 3 is pretty good!”
- **Summary:** A full 20-second audiovisual sequence is generated from one prompt, with FLUX 3 assembling the edits and producing a voiceover without requiring an on-screen lip-synced speaker.
- **Workflow/details:** Single-prompt FLUX 3 generation; 20-second duration; model-directed editing; generated voiceover; no lip-sync requirement. The source does not disclose the prompt text, input references, seed, resolution, aspect ratio, or post-production.
- **Prompt provenance:** `mentioned_not_in_post` — the creator states that one prompt produced the video, but the exact prompt is not visible in the verified source and has not been inferred.
- **Why included:** Newly published explicit creator attribution, preserved attached-video context, strong public engagement, and a production-oriented demonstration of full-duration autonomous editing and voiceover generation from a single prompt.

### 72. Same-prompt FLUX 3 vs. MiniMax H3 four-scenario comparison — Reddit creator

- **Creator:** Original poster in [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/) — the creator username is not exposed by the current public index.
- **Published:** 2026-08-06
- **Original source:** [A few Flux 3 vs H3 comparisons](https://www.reddit.com/r/StableDiffusion/comments/1vhf7e8/a_few_flux_3_vs_h3_comparisons/)
- **Model attribution:** The creator says they noticed “Flux 3 is up on API” and personally ran comparison renders using the same H3-formatted prompt for FLUX 3 and MiniMax H3.
- **Summary:** Four controlled comparisons cover a Viking longship selfie, first-person dragon flight over a medieval capital, a photoreal nature-documentary creature shot, and a stylized skeleton-witch animation.
- **Workflow/details:** The same structured H3 prompt is submitted to both models for each scenario. The published prompts combine `integrated_multimodal_description`, dialogue, `overall_soundscape`, and `non_diegetic_music`; the cartoon test additionally uses first-frame/reference retention fields. In the public discussion, the creator reports stronger FLUX 3 visuals in the Viking and dragon tests, while judging H3 stronger in the nature-documentary and cartoon examples and markedly better for audio.
- **Prompt provenance:** `verbatim_in_post` — “Live-action cinematic fantasy with grounded historical realism, photographed on 65 mm large-format film.” Full prompts for all four scenarios remain visible in the original post.
- **Why included:** Newly published primary creator post, explicit FLUX 3 attribution, attached comparison media, exact reproducible prompts, identical cross-model inputs, and unusually broad stress testing of camera motion, large-scene consistency, creature physics, dialogue, stylization, reference retention, and native audio.

### 73. Four-way synchronized aircraft engine-failure return — Future Vibes AI

- **Creator:** [Future Vibes AI (@FutureVibesAi)](https://x.com/FutureVibesAi)
- **Published:** 2026-08-06 (based on the public verification page’s relative timestamp)
- **Original source profile:** [Future Vibes AI on X](https://x.com/FutureVibesAi) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, exact prompt, clip context, and engagement](https://mobile.twstalker.com/FutureVibesAi)
- **Model attribution:** The creator explicitly introduces the clip with “Split Screen clip with Flux 3.”
- **Summary:** A passenger aircraft’s single-engine failure and controlled return are shown simultaneously from the cabin, an exterior tracking camera, the cockpit, and an aerial view, with the failure, reactions, stabilization, and return path synchronized across all four panels.
- **Workflow/details:** Four synchronized camera panels; the engine failure is anchored at the 2-second mark, followed by brief yaw, immediate pilot correction, passenger reaction, stabilization, and a controlled return toward the airport while emergency vehicles prepare. The prompt requires matching aircraft attitude, engine behavior, pilot actions, passenger reactions, weather, and flight path across every view. Duration, resolution, seed, reference inputs, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Four-way synchronized cinematic split-screen showing the same passenger aircraft experiencing a single-engine failure shortly after takeoff.” The complete prompt remains visible in the verification source.
- **Why included:** Newly published explicit creator attribution, an exact reproducible prompt, strong public engagement, and a demanding multi-camera test of procedural aviation behavior, aerodynamics, causal timing, human reactions, and scene geometry.

### 74. Four-way synchronized mountain helicopter rescue — Future Vibes AI

- **Creator:** [Future Vibes AI (@FutureVibesAi)](https://x.com/FutureVibesAi)
- **Published:** 2026-08-05 (based on the public verification page’s relative timestamp)
- **Original source profile:** [Future Vibes AI on X](https://x.com/FutureVibesAi) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, exact prompt, clip context, and engagement](https://mobile.twstalker.com/FutureVibesAi)
- **Model attribution:** The creator explicitly introduces the clip with “Split screen clip with Flux 3.”
- **Summary:** A dangerous alpine helicopter rescue is shown simultaneously from the cabin, an exterior side-following view, the cockpit, and an aerial camera as a wind gust destabilizes the hover and a stranded climber is extracted by cable.
- **Workflow/details:** Four synchronized camera panels; at the 2-second mark a strong wind pushes the helicopter sideways, the pilot corrects, the rescue crew lowers a cable, the climber is secured and lifted, and rotor wash drives snow around the aircraft. The prompt requires matching helicopter orientation, cable movement, wind direction, rotor wash, climber position, and lighting across every view. Duration, resolution, seed, reference inputs, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Four-way perfectly synchronized split-screen showing the same helicopter rescue operation during a dangerous mountain snowstorm.” The complete prompt remains visible in the verification source.
- **Why included:** Newly published explicit creator attribution, an exact reproducible prompt, and a physically demanding multi-view rescue sequence combining aircraft control, cable dynamics, weather, rotor wash, spatial consistency, and synchronized causal action.

### 75. Four-way synchronized emergency airplane river landing — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-08-04 (based on the public verification page’s relative timestamp)
- **Original source profile:** [Umesh on X](https://x.com/umesh_ai) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-post mirror preserved through a Future Vibes AI profile retweet, including the original creator wording, prompt opening, attached-video context, and engagement](https://mobile.twstalker.com/FutureVibesAi)
- **Model attribution:** Umesh explicitly introduces the attached result with “Another 4-way split screen clip with Flux 3!”
- **Summary:** An emergency airplane river landing is presented simultaneously from four synchronized camera perspectives, with each panel continuously following the same aircraft while the viewpoint-specific visuals evolve through the event.
- **Workflow/details:** Four-way split-screen text-to-video with synchronized viewpoints and continuous tracking of one aircraft. The public verification extract preserves the cross-camera synchronization requirement and the beginning of the panel-by-panel prompt, but does not expose the complete camera descriptions, duration, resolution, seed, reference inputs, or post-production.
- **Prompt provenance:** `verbatim_in_post` — “Four-way split-screen showing the same emergency airplane river landing from four synchronized camera perspectives.” The verified source also visibly states that each panel follows the aircraft continuously as the event unfolds.
- **Why included:** Explicit original-creator attribution, attached-video context, a visible reproducible prompt opening, strong public engagement, and a demanding multi-view stress test of aircraft identity, continuous tracking, event timing, spatial consistency, and synchronized action over water.

### 76. Regency-manor astronaut tracking-shot stress test — Ethan Mollick

- **Creator:** [Ethan Mollick (@emollick)](https://x.com/emollick)
- **Published:** 2026-08-07 (based on the public verification page’s relative timestamp)
- **Original source profile:** [Ethan Mollick on X](https://x.com/emollick) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, visible full prompt, attached-video context, and engagement](https://mobile.twstalker.com/emollick)
- **Model attribution:** Mollick explicitly identifies the attached result as produced by Flux 3 and introduces the visible text as the prompt used for it.
- **Summary:** A tracking shot follows an open-helmet astronaut through a Regency dance inside a traditional manor, pushes through the crowd into a hammered-tin-paneled room with an unarmed knight-versus-ninja fight, then shifts to her point of view toward a stained-glass flower-and-serpent motif.
- **Workflow/details:** Text-to-video from one visible prompt; continuous subject-following camera movement, crowd interaction, a room-to-room transition, secondary fight choreography, and a final POV handoff are all directed in the same generation. Duration, resolution, seed, reference inputs, native-audio instructions, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “tracking shot that follows a female astronaut with her helmet open as she walks through a regency dance in a traditional manor”. The complete prompt remains visible in the verification source.
- **Why included:** Newly published original-creator attribution, an exact visible prompt, attached-video verification, substantial early engagement, and a demanding cinematic test of camera continuity, crowd staging, architectural transition, multi-character choreography, viewpoint change, and scene persistence.

### 77. One-prompt 1080p “Lost Footage” multi-cut sequence — Reddit creator

- **Creator:** Original poster in [r/FluxAI](https://www.reddit.com/r/FluxAI/) — the creator username is not exposed by the current public index.
- **Published:** 2026-08-05
- **Original source:** [FLUX 3 Test (Lost Footage)](https://www.reddit.com/r/FluxAI/comments/1vg5flb/flux_3_test_lost_footage/)
- **Model attribution:** The creator explicitly captions the attached result “Just having fun with FLUX3” and identifies the output as 1080p and 20 seconds long.
- **Summary:** A “lost footage” styled audiovisual sequence uses a single FLUX 3 prompt to execute multiple planned cuts and actions across a full 20-second clip, while the model independently supplies the spoken dialogue.
- **Workflow/details:** One-prompt text-to-video; 1080p; 20-second duration. In the discussion, the creator confirms that they explicitly requested every cut and visible action, FLUX 3 followed that direction, and the dialogue itself was not specified by the creator. Exact seed, aspect ratio, reference media, audio wording, and post-production are not disclosed.
- **Prompt provenance:** `mentioned_not_in_post` — the creator confirms that one prompt contained the cut and action instructions, but the exact prompt text is not publicly visible and has not been reconstructed.
- **Why included:** Newly published primary creator post with attached video, explicit FLUX 3 attribution, verified 1080p/20-second settings, a reproducible one-prompt multi-cut workflow, model-generated dialogue, and meaningful community engagement.

### 78. Bootleg phone-recorded live-metal encore — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** 2026-08-07 (based on the public verification mirror’s relative timestamp)
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the public index did not expose a stable direct status URL.
- **Verification source:** [Secondary mirror preserving the original creator wording, exact prompt, attached-video context, and engagement](https://twstalker.com/ZachyAshworth)
- **Model attribution:** The original creator explicitly prefixes the attached generation with “Flux 3:”.
- **Summary:** A deliberately low-fi phone recording captures a metal band’s encore in a small venue at the moment the chorus peaks and a guitar solo breaks out, testing whether generated performance energy can survive an intentionally amateur recording aesthetic.
- **Workflow/details:** Text-to-video from one concise prompt specifying a bootleg phone-camera look, small live venue, encore structure, chorus peak, and featured solo. Duration, resolution, seed, reference media, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “a bootlegged phone recording of a metal band playing in a small venue, they're doing the encore and they are hitting the chorus of their big number, there's an amazing solo”
- **Why included:** Newly published explicit creator attribution, an exact reproducible prompt, attached-video verification, strong early engagement, and a distinctive audiovisual stress test of live-music staging, performance timing, crowd-scale venue realism, and convincing low-fi phone capture.

### 79. Twenty-second multi-room fennec-fox chase in one unbroken take — Reddit creator

- **Creator:** Original poster in [r/generativeAI](https://www.reddit.com/r/generativeAI/) — the creator username is not exposed by the current public index.
- **Published:** 2026-08-06
- **Original source:** [A tweaked 20-second single-take fox chase prompt held zero cuts start to finish in FLUX3](https://www.reddit.com/r/generativeAI/comments/1vgy8if/a_tweaked_20second_singletake_fox_chase_prompt/)
- **Model attribution:** The creator explicitly says the full generation was run on “FLUX 3 on Atlas Cloud,” and the original post title also identifies the model as FLUX3.
- **Summary:** A fennec fox sprints through a dark house at night while a low handheld camera follows continuously from bedroom to hallway, bathroom, stairs, kitchen, dining room, living room, laundry basket, plant corner, and entryway without a cut.
- **Workflow/details:** Text-to-video; 20-second duration; one unbroken take; low floor-level handheld follow camera that intentionally reacts slightly late, allows imperfect framing, camera shake, and brief focus slips. The creator also stages physical interaction beats including a falling pillow, trailing toilet paper, a knocked remote, and dirt smearing the lens.
- **Prompt provenance:** `mentioned_not_in_post` — the creator explains how the camera prompt and route were structured, but the exact full generation prompt is not publicly visible and has not been reconstructed.
- **Why included:** Newly published primary creator post, explicit FLUX 3 attribution, a concrete Atlas Cloud workflow, and a demanding full-20-second continuity test combining multi-room spatial handoffs, small-subject tracking, deliberate handheld imperfection, object interaction, and persistent physical causality.

### 80. Structured kaiju-destruction FLUX 3 vs. Seedance 2.0 benchmark — Jin.B

- **Creator:** [Jin.B (@opener_ai)](https://x.com/opener_ai)
- **Published:** 2026-08-06 (based on the public verification mirror’s relative timestamp)
- **Original source profile:** [Jin.B on X](https://x.com/opener_ai) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, full structured prompt, and engagement](https://mobile.twstalker.com/opener_ai)
- **Model attribution:** Jin.B explicitly says the attached comparison runs “Flux 3 vs Seedance 2.0” and describes using closely matched timing/settings for the two outputs.
- **Summary:** A photorealistic stormy-coastal kaiju sequence pits a skyscraper-scale deep-sea octopus against a city, with the creature crushing buses and streetlights, pulling down a glass tower, sprinting through intersections, vaulting a full block, and charging through waterfront cranes.
- **Workflow/details:** Controlled cross-model comparison from one highly structured prompt. The visible setup specifies 15 seconds, rapid creature movement, controlled cameras, five time-coded camera/action beats, storm lighting, VFX, native audio design, and hard constraints to keep all eight tentacles connected, distinct, and readable while avoiding anatomy drift, flicker, weightless debris, and chaotic camera motion. Jin.B notes using closely matched 20s/15s settings for the two models.
- **Prompt provenance:** `verbatim_in_post` — “Build the monster, city, scale, and destruction entirely from text. … Photorealistic kaiju disaster film, stormy coastal metropolis, grounded structural destruction. … A colossal deep-sea octopus taller than nearby skyscrapers. … It never stops or poses. Four tentacles pull its body rapidly forward while the others destroy obstacles.” The complete time-coded prompt remains visible in the verification source.
- **Why included:** Original-creator attribution, attached comparison video, a visible reproducible structured prompt, substantial public engagement, and an unusually difficult benchmark of multi-limb anatomy, fast physical action, time-coded cinematography, city-scale destruction, weather, debris, audio, and cross-model prompt adherence.

### 81. Blackout-disappearance subway FLUX 3 vs. Seedance 2.0 benchmark — Jin.B

- **Creator:** [Jin.B (@opener_ai)](https://x.com/opener_ai)
- **Published:** 2026-08-07 (based on the public verification mirror’s relative timestamp)
- **Original source profile:** [Jin.B on X](https://x.com/opener_ai) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original comparison caption, attached-video context, and FLUX 3 prompt follow-up](https://mobile.twstalker.com/opener_ai)
- **Model attribution:** Jin.B explicitly says the attached comparison tests “Flux 3 & Seedance 2.0,” tags `#Flux3` and Black Forest Labs, then publishes a follow-up labeled “[Flux3 prompt].”
- **Summary:** A single continuous first-person subway shot uses timed blackouts to make passengers disappear while the moving train, camera sway, surviving passengers, empty seats, abandoned objects, and later ceiling impacts preserve scene continuity.
- **Workflow/details:** Controlled cross-model comparison from a Claude Opus 5-authored prompt. The visible FLUX 3 brief specifies a moving nighttime subway car, continuous POV with no cuts, handheld/body-cam rocking, cold green-cyan lighting, blue tunnel strobes, staged passenger disappearances across three blackouts, then a sequence of physically progressive ceiling impacts. It runs to 20 seconds and includes explicit native-audio cues such as rail clatter, fluorescent buzz, ballast clicks, metallic cracks, glass shattering, and bending steel.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Single continuous first-person POV shot, no cuts. A standing passenger inside a moving subway car at night. The entire frame rocks and jolts with the train throughout, handheld body-cam energy.” The complete 20-second FLUX 3 prompt remains visible in the verification source.
- **Why included:** Newly published original-creator comparison with explicit FLUX 3 labeling, attached video, exact visible prompt, controlled shared-prompt methodology, and a difficult test of temporal continuity, disappearing-character logic, lighting transitions, handheld motion, object persistence, progressive physical damage, audio timing, and scene-state consistency.

### 82. Pelican shoegaze band “Pelicans on Bikes” — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** 2026-08-08 (based on the public verification mirrors’ relative timestamps)
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the public indexes did not expose the direct status URL.
- **Verification sources:** [Secondary mirror preserving fofr’s follow-up and its quoted same-creator FLUX 3 parent post](https://twstalker.com/ZachyAshworth); [Black Forest Labs co-founder Robin Rombach’s public profile mirror resharing the follow-up](https://site.twstalker.com/robrombach).
- **Model attribution:** The follow-up is shown directly beneath and quoting fofr’s immediately preceding same-creator post, which explicitly prefixes the generation series with “Flux 3:”. Robin Rombach then reshared the “Pelicans on Bikes” follow-up and praised its prompting.
- **Summary:** A deliberately bootleg-looking phone recording captures a shoegaze band named “Pelicans on Bikes” introducing itself in a small venue and launching into its first song, while every performer is rendered as an actual pelican.
- **Workflow/details:** Prompt-led generation using an intentionally low-fi phone-recording aesthetic, a small live venue, spoken band introduction, a named first song (“SVG”), and non-human performers. Duration, resolution, seed, reference media, and post-production are not disclosed in the verified sources.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “bootlegged phone recording of a shoegaze band called \"Pelicans on Bikes\" playing in a small venue, they introduce themselves”. The remaining prompt text is visibly preserved in the verification source.
- **Why included:** Newly published same-creator FLUX 3 thread attribution, visible prompt text, strong public engagement, and first-party signal from Black Forest Labs co-founder Robin Rombach. The result is a distinctive audiovisual stress test of animal identity consistency, live-band staging, spoken introduction, generated music/performance timing, and convincing low-fi phone capture.

### 83. 1995 television documentary explaining the internet — Bennett / Generative Media

- **Creator:** [Bennett | Generative Media | AI SEO @ fal (@influencer_seo)](https://x.com/influencer_seo)
- **Published:** 2026-08-08 (based on the public verification mirror’s relative timestamp)
- **Original source profile:** [Bennett on X](https://x.com/influencer_seo) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary mirror directly preserving the original creator post, model attribution, prompt, and evaluation](https://twstalker.com/ZachyAshworth)
- **Model attribution:** The creator explicitly labels the post “Flux 3 Prompt” and evaluates the resulting FLUX 3 generation.
- **Summary:** A deliberately period-authentic 1995 TV documentary explains the internet using bulky computers, office cubicles, slow demonstrations, animated graphics, formal narration, and carefully staged explanations of email.
- **Workflow/details:** Minimal text-to-video prompting: the creator uses a single short era-and-format instruction rather than a long shot list, then notes that FLUX 3 reproduced not just period technology but the pacing, framing, performances, production design, optimism, and awkward explanatory tone of mid-1990s television.
- **Prompt provenance:** `verbatim_in_post` — “a 1995 television documentary explaining the internet”
- **Why included:** Newly published creator-attributed FLUX 3 example with an exact compact prompt and unusually strong style/era semantics. It is valuable as a reusable test showing that a short prompt can target both a historical period and the period-specific media grammar through which people of that era imagined new technology.

### 84. Rocket-launcher lawyer argument — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-07
- **Original post:** [View on X](https://x.com/cfryant/status/2085732465205735927)
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, post identity, attached-media context, and engagement](https://twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly captions the clip “When lawyers argue, but with rocket launchers. FLUX 3”.
- **Summary:** A darkly comic action vignette literalizes a heated lawyer argument by escalating the confrontation to rocket launchers.
- **Workflow/details:** Creator-posted FLUX 3 video built around a concise high-level premise rather than a publicly disclosed shot list. The verified public source does not disclose duration, resolution, input references, seed, native-audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the visible caption describes the finished concept but is not explicitly labeled as the generation prompt, so no prompt text is inferred.
- **Why included:** Traceable original status, explicit creator attribution, thousands of early views, and a distinctive compact concept that stresses multi-character staging, escalation, action timing, and comedic readability without relying on a long visible prompt.

### 85. Household spider-removal comedy — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-06
- **Original post:** [View on X](https://x.com/cfryant/status/2085492904286396422)
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, post identity, attached-media context, and engagement](https://twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly captions the clip “When your girlfriend tells you to take care of a spider. FLUX 3”.
- **Summary:** A familiar household request to deal with a spider is turned into an exaggerated visual-comedy scenario, using an immediately legible everyday setup as the joke’s anchor.
- **Workflow/details:** Creator-posted FLUX 3 video from an experienced AI filmmaker. The public verification source preserves the concept and strong early engagement but does not disclose duration, exact generation prompt, input references, seed, resolution, audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the caption states the premise but is not labeled as the exact generation prompt, and nothing has been reconstructed from the footage.
- **Why included:** Explicit original-creator FLUX 3 attribution, a traceable status URL, roughly eight thousand views in the verified mirror snapshot, and a concise comedy setup that provides a useful test of believable everyday context, reaction timing, and escalation.

### 86. One-prompt, one-generation Fable 5 + Flux 3 Video single-shot — Yuval Avidani

- **Creator:** [Yuval Avidani](https://il.linkedin.com/in/yuval-avidani-87081474)
- **Published:** Date not exposed; verified 2026-08-09
- **Original source profile:** [Yuval Avidani on LinkedIn](https://il.linkedin.com/in/yuval-avidani-87081474) — the public index exposes the creator's activity but not a stable direct activity URL.
- **Verification source:** [Secondary LinkedIn profile preserving Yuval's original activity wording and relative timestamp](https://eg.linkedin.com/in/mohamedali-linked)
- **Model attribution:** Yuval explicitly labels the generation “Fable 5 + Flux 3 Video”; his first-party profile describes it as one prompt and one generation, while the public LinkedIn verification copy preserves “Single shot. No edit.”
- **Summary:** A one-pass FLUX 3 Video test is presented as a single-shot result produced from one prompt and one generation, with no editing, making the finished clip a compact demonstration of end-to-end prompt execution rather than an externally assembled sequence.
- **Workflow/details:** One prompt; one generation; single shot; no edit. No verified seed, duration, resolution, reference inputs, or post-production settings are publicly exposed beyond the creator's explicit no-edit statement.
- **Prompt provenance:** `verbatim_in_post` — the accessible LinkedIn index visibly places “Clear the noise.” immediately after “Prompt below 👇”. Because the public index may truncate subsequent text, no additional prompt wording is copied or inferred.
- **Why included:** First-party creator attribution, explicit Flux 3 Video labeling, a highly reproducible one-pass/no-edit workflow, visible prompt text, and strong public engagement across LinkedIn activity snapshots.

### 87. Southeast Asian vernacular school-vlog realism tests — MXVDXN // DAN

- **Creator:** [MXVDXN // DAN (@mxvdxn)](https://x.com/mxvdxn)
- **Published:** 2026-07-27
- **Original post:** [View on X](https://x.com/mxvdxn/status/2081801246474904031)
- **Verification sources:** [Secondary creator-profile mirror preserving MXVDXN’s original FLUX 3 test notes and engagement](https://www.instalker.org/mxvdxn) · [Public discussion preserving the exact original status ID and identifying the attached work as FLUX.3 Southeast Asian schoolgirl vlogs](https://boards.4chan.org/g/thread/109386035/ldg-local-diffusion-general)
- **Model attribution:** MXVDXN explicitly says he tested FLUX 3 and later labels the same test series “FLUX 3 by @bfl_ai”; the preserved original-status reference independently identifies the attached vlog footage as FLUX.3.
- **Summary:** Raw Southeast Asian school-vlog footage tests whether FLUX 3 can reproduce local vernacular rather than generic cinematic language, with emphasis on region-specific faces, dialect, gestures, intonation, and everyday handheld-video texture.
- **Workflow/details:** The creator deliberately avoided polished Hollywood-style prompting and instead stress-tested local Southeast Asian nuance and a raw handheld aesthetic. He reports especially strong dialect, gesture, intonation, and natural-looking faces, while candidly noting that crowd control, high-dynamic performance, distortion, and face consistency from character references still need work.
- **Prompt provenance:** `not_provided` — the creator explains the creative goal and evaluation criteria but does not expose the exact generation prompt for the verified vlog post, so no prompt text has been inferred.
- **Why included:** Traceable original status, explicit creator-side FLUX 3 attribution, roughly twenty-two thousand views in the verification snapshot, distinctive regional-language and cultural-specificity testing, and unusually useful qualitative failure notes alongside the creator’s praise for realism.

### 88. 1920s speakeasy-to-street gangster shootout — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-07 (based on the public verification mirror’s relative timestamp)
- **Original source profile:** [Christopher Fryant on X](https://x.com/cfryant) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary mirror preserving a retweet of the original creator post, original wording, attribution, attached-video context, and engagement](https://twstalker.com/cdcwatson)
- **Model attribution:** Fryant explicitly calls the attached work “Another early access FLUX 3 time travel gopro video” and tags Black Forest Labs.
- **Summary:** A first-person GoPro-style historical action sequence drops the viewer into a 1920s gangster shootout inside a speakeasy, then carries the confrontation out into the street.
- **Workflow/details:** Creator-posted FLUX 3 historical-POV generation built around first-person GoPro camera language, period production design, multi-character gunfight staging, and an interior-to-exterior action transition. The verified public source does not disclose duration, exact prompt, reference media, seed, resolution, native-audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the visible caption describes the generated scene but is not explicitly labeled as the generation prompt, so no prompt text has been inferred.
- **Why included:** Explicit original-creator FLUX 3 attribution preserved by a public secondary source, strong public engagement, and a demanding historical-action test combining period fidelity, first-person camera coherence, sustained combat staging, spatial continuity, and a location transition from enclosed speakeasy to open street.

### 89. Twenty-second live-action arcade rhythm-game cat — あいきみ

- **Creator:** [あいきみ (@AiWithYou1)](https://x.com/AiWithYou1)
- **Published:** Date not exposed; verified 2026-08-09
- **Original source profile:** [あいきみ on X](https://x.com/AiWithYou1) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary public mirror preserving a retweet of the original creator post, explicit FLUX 3 wording, visible settings, prompt text, attached-video context, and engagement](https://ww.twstalker.com/o81morimori)
- **Model attribution:** The original creator explicitly opens the post with “FLUX 3の20秒生成いいね” and then lists a 20-second generation setup and time-coded video prompt.
- **Summary:** A photorealistic orange tabby performs an impossibly precise rhythm-game run inside a neon Japanese arcade while a handheld smartphone-style camera moves through an excited crowd, cuts between the cat’s paws, face, game screen, and reactions, and finishes on a record-breaking score.
- **Workflow/details:** The visible source specifies a 20-second duration, 16:9 aspect ratio, photorealistic live-action smartphone-video aesthetics, and five time-coded beats spanning 0–20 seconds. It directs a handheld push through the crowd, close-ups and screen inserts, escalating rhythm-game performance, crowd reactions, flashing machine feedback, and a final score beat. Seed, resolution, reference inputs, and post-production are not exposed in the verified public source.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “A fully realistic live-action style video set inside a vibrant Japanese arcade at night. A real orange tabby cat is standing in front of a rhythm game machine, surrounded by glowing neon lights, arcade cabinets, reflective floors, and excited onlookers.” The public verification source preserves the subsequent time-coded 0–20 second prompt; no wording has been reconstructed from the footage.
- **Why included:** Explicit original-creator FLUX 3 attribution, a visible full-duration structured prompt, reproducible duration and aspect-ratio settings, attached-video verification, public engagement, and a demanding stress test of animal motion, fast paw-to-machine interaction, legible arcade feedback, handheld camera grammar, reflective lighting, crowd continuity, and synchronized escalation across a complete 20-second sequence.

### 90. “When you have your own Kuato” body-horror comedy vignette — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-06
- **Original post:** [View on X](https://x.com/cfryant/status/2085404360201113665)
- **Verification source:** [Secondary creator-profile mirror preserving the original caption and engagement context](https://twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly labels the attached video “FLUX 3.”
- **Summary:** A compact body-horror/comedy vignette built around the recognizable premise “When you have your own Kuato,” using a concise visual gag rather than a generic model demo.
- **Workflow/details:** No duration, references, seed, editing workflow, or generation settings are publicly disclosed in the verified source.
- **Prompt provenance:** `not_provided` — the visible caption is presented as the concept/title, not as an explicitly labeled generation prompt.
- **Why included:** Original creator attribution, explicit FLUX 3 labeling, a distinctive concept from an experienced AI filmmaker, and meaningful engagement in the preserved source snapshot (about 9K views and 63 likes).

### 91. “Snakes on a Plane, but in reverse” concept vignette — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-07
- **Original post:** [View on X](https://x.com/cfryant/status/2085860627222765641)
- **Verification source:** [Secondary creator-profile mirror preserving the original creator caption and traceable status link](https://twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly captions the creator-posted video “Snakes on a Plane, but in reverse. FLUX 3”.
- **Summary:** A compact comedy/action vignette inverts the familiar “Snakes on a Plane” premise, using a one-line high-concept setup as the basis for the generated scene.
- **Workflow/details:** Creator-posted FLUX 3 video from an experienced AI filmmaker. The verified public source does not disclose duration, exact generation prompt, references, seed, resolution, native-audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the visible caption is presented as the concept/title, not as an explicitly labeled generation prompt, so no prompt text is inferred.
- **Why included:** Explicit original-creator FLUX 3 attribution, a traceable original status URL, a concise high-concept premise, and a distinct test of visual-comedy readability and model interpretation from minimal public direction.

### 92. Faux 1999 CNN broadcast announcing text-to-video AI — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-08-09 (based on the first-party profile’s relative timestamp)
- **Original source profile:** [Justine Moore on X](https://x.com/venturetwins) — the public index did not expose a stable direct status URL.
- **Verification source:** [Andreessen Horowitz’s first-party Justine Moore profile embedding her original X activity, visible prompt, and attached-media links](https://a16z.com/author/justine-moore/)
- **Model attribution:** The first-party profile preserves Moore’s FLUX 3 launch post and the adjacent creator prompt addressed to Black Forest Labs, with the prompt itself ending in an on-screen “FLUX 3” reveal.
- **Summary:** A faux archival 1999 CNN broadcast has an anchor announce that researchers demonstrated AI capable of generating convincing video from text; a second anchor laughs off the claim before the single continuous shot glitches into a FLUX 3 reveal.
- **Workflow/details:** Prompt-led text-to-video using a 1999 archival-news aesthetic, spoken anchor dialogue, one uninterrupted shot, an intentional screen glitch, and a final model-name typography reveal. Duration, resolution, seed, reference media, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “1999 CNN broadcast that looks archival. Anchor: ‘Today researchers demonstrated an AI that can generate convincing video from text.’” The same visible prompt continues with the second anchor’s reaction, single-take constraint, glitch, and FLUX 3 reveal.
- **Why included:** Fresh first-party creator evidence with visible prompt text and attached-media links, plus a compact reproducible test of period-specific broadcast grammar, dialogue, comedic timing, continuous-shot control, transition timing, and legible typography.

### 93. Twenty-second “supercar commercial, but it’s actually grandma” — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** Date not exposed; verified 2026-08-10
- **Original source profile:** [Christopher Fryant on X](https://x.com/cfryant) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary mirror preserving a retweet of the original creator post, explicit FLUX 3 attribution, 20-second setting, attached-video context, and engagement](https://mobile.twstalker.com/doerstokyo342)
- **Model attribution:** Fryant explicitly says he received FLUX 3 early access and introduces the attached clip as one of his tests.
- **Summary:** A full-length generative commercial flips a conventional supercar-ad premise by making the star “actually grandma,” using a compact high-concept setup as a production-oriented FLUX 3 demonstration.
- **Workflow/details:** Early-access FLUX 3 video; 20-second output. The verified source does not disclose the exact generation prompt, reference media, seed, resolution, native-audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — “A supercar commercial but it’s actually grandma” is presented as the test concept/caption, not explicitly as the generation prompt, so no prompt text is inferred.
- **Why included:** Explicit original-creator FLUX 3 attribution, verified full-20-second output, substantial engagement in the preserved creator post, and a production-oriented commercial concept from an experienced AI filmmaker.

### 94. Handheld Saturn-view space-cruise room — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** 2026-08-10 (based on the secondary verification index’s relative timestamp)
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary public index directly quoting the original creator post, model attribution, prompt text, and video context](https://aihot.virxact.com/all?category=tip&channel=x&page=1)
- **Model attribution:** fofr explicitly begins the creator post with “Imagining a space cruise with Flux 3:” before the visible prompt.
- **Summary:** Amateur handheld tourist POV inside a plush space-cruise cabin frames Saturn through a large window, keeps the room reflection visible in the glass, then turns the room lights off halfway through so the exterior view becomes clearer.
- **Workflow/details:** Prompt-led text-to-video using amateur handheld POV, a comfortable interior, a large reflective window, Saturn as the exterior anchor, and a mid-shot lighting-state change. Duration, resolution, seed, reference media, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “amateur handheld pov footage of a tourist in their plush and comfortable room of a space cruise, carpeted floor and comfy bed, large window shows a view of Saturn, you can see their reflection in the window, they turn off the light half way through so we can see outside better”
- **Why included:** Newly surfaced creator-attributed Flux 3 video with an exact prompt and a compact but difficult realism test combining reflective glass, interior/exterior exposure, a deliberate lighting transition, handheld camera language, and a persistent astronomical background.

### 95. Sofa-mounted GoPro Saturn timelapse aboard a space cruise — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** 2026-08-10 (based on the secondary verification index’s relative timestamp)
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary public index directly quoting the original creator prompt and same-creator FLUX 3 Saturn follow-up](https://aihot.virxact.com/all?category=tip&channel=x&page=1)
- **Model attribution:** The paired same-creator Saturn posts are preserved together: the prompt post describes the timelapse, while fofr immediately follows with “I'm impressed that Flux 3 can handle other more interesting angles of Saturn too.” The verification page explicitly identifies the video as a Flux 3 generation.
- **Summary:** An intentionally amateur timelapse watches a space-cruise cabin orbit Saturn from an unusual angle, with changing room reflections and lighting while background passengers streak through the frame; the camera is a GoPro on a tripod placed beside the window, deliberately perched on a sofa.
- **Workflow/details:** Prompt-led timelapse video with a mostly fixed GoPro/tripod viewpoint, a moving orbital exterior, interior reflections, intermittent lights-off states, accelerated background human movement, and an explicit audio constraint of calm music with no sound effects. Duration, resolution, seed, reference media, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “an amateur timelapse video taken by a tourist from ` plush and comfortable room on a space cruise, timelapse is as it orbits around saturn at a peculiar angle, at times you can see the reflection of the room, at other times the lights are off, it's from a gopro on a tripod mounted next to the window. in a timelapse fashion we see people moving around quickly in the background, no sound effects, just calm music You can tell it's amateur as they put the tripod on a sofa.”
- **Why included:** Newly published creator-attributed FLUX 3 follow-up with visible prompt text and a distinctive temporal-photography stress test: orbital motion, reflections, exposure changes, accelerated human motion, deliberately imperfect camera placement, and explicit non-diegetic audio direction all have to coexist coherently.

### 96. Self-referential 1990s documentary about itself — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** Date not exposed; verified 2026-08-12
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary public mirror preserving a retweet of the original creator post, exact wording, explicit model attribution, attached-video context, and engagement](https://mobile.twstalker.com/SpyHive)
- **Model attribution:** The preserved creator post explicitly begins “Flux 3:” before the visible prompt.
- **Summary:** A faux 1990s documentary recursively documents the very documentary the viewer is watching and includes clips from itself, turning a one-line concept into a meta-narrative continuity test.
- **Workflow/details:** Prompt-led text-to-video from a single concise self-referential instruction. No verified duration, resolution, seed, reference media, audio settings, or post-production details are publicly exposed.
- **Prompt provenance:** `verbatim_in_post` — “a 90s documentary that is a documentary about this exact documentary, the documentary includes clips from itself”
- **Why included:** Exact reproducible prompt, explicit original-creator FLUX 3 attribution, attached-video context, and strong early engagement in the preserved snapshot (about 6K views and 230 likes). The recursive premise is also a distinctive stress test of period media grammar, self-reference, nested visual continuity, and narrative coherence.

### 97. “Knights in the modern world” anachronistic vignette — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** Date not exposed; verified 2026-08-12
- **Original source profile:** [Justine Moore on X](https://x.com/venturetwins) — the public index did not expose a stable direct status URL.
- **Verification source:** [Andreessen Horowitz’s first-party Justine Moore profile embedding her original X activity and attached-media link](https://a16z.com/author/justine-moore/)
- **Model attribution:** Moore explicitly captions the attached work “Knights in the modern world (made with FLUX 3 😉).”
- **Summary:** A concise anachronistic concept places medieval knights into a modern-world setting, using the historical-versus-contemporary contrast as the scene’s core visual premise.
- **Workflow/details:** Creator-posted FLUX 3 media. The first-party profile preserves the original caption and attached-media link but does not expose duration, exact generation prompt, input references, seed, resolution, audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the visible caption describes the concept but is not explicitly labeled as the generation prompt, so no prompt text is inferred.
- **Why included:** Fresh original-creator FLUX 3 attribution preserved on a first-party profile, attached-media verification, and a distinctive anachronistic scene concept that tests whether historically specific costume and character cues remain readable inside a contemporary context.

### 98. Three five-second realism benchmarks vs. Sora 2 and MiniMax H3 — Timely_Collar1960

- **Creator:** [Timely_Collar1960](https://www.reddit.com/user/Timely_Collar1960/)
- **Published:** 2026-08-12
- **Original source:** [Sora 2 vs Flux 3 & MiniMax H3 – Part 2 with Prompts Included](https://www.reddit.com/r/SoraAi/comments/1vlicif/sora_2_vs_flux_3_minimax_h3_part_2_with_prompts/)
- **Model attribution:** The creator explicitly names Flux 3 in the comparison title, states that the exact same prompt was used for all three models, and separately evaluates the Flux 3 outputs as having fewer errors plus stronger camera motion and fine-detail handling.
- **Summary:** Three photorealistic everyday-scene benchmarks compare FLUX 3 against Sora 2 and MiniMax H3: a teenage dancer self-recording in a bedroom, a surgeon scrubbing outside an operating theatre, and a woman shopping in an upscale grocery store. The FLUX 3 clips are presented inside a controlled same-prompt comparison rather than as isolated cherry-picked examples.
- **Workflow/details:** Three test prompts; each model receives the exact same prompt; clips are kept to 5 seconds each. The prompts deliberately specify practical camera grammar and capture aesthetics, including a phone-as-camera bedroom setup, a RED Komodo / 35 mm clinical setup, and handheld documentary grocery-store tracking. The creator also notes that their access path supports video uploads in addition to text-to-video and image-to-video.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt from Test 1: “A teenage girl practises a choreographed dance routine alone in her bedroom at 9pm, phone propped against her mirror recording her.” The complete Test 1, Test 2, and Test 3 prompts are visibly published in the original post; no wording has been inferred from the footage.
- **Why included:** Fresh primary creator post with attached media, explicit Flux 3 attribution, three visible reproducible prompts, controlled same-prompt methodology, and direct qualitative comparison against two strong competing video models. The creator specifically reports fewer visual errors and more convincing camera motion/details from Flux 3, making the post unusually useful for evaluating photorealism and prompt adherence rather than just showcasing a single aesthetic demo.

### 99. Fifteen-second ice-cream commercial benchmark — Reddit creator

- **Creator:** Original poster in [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/) — the creator username is not exposed by the current public index.
- **Published:** 2026-08-12
- **Original source:** [Ice cream ad MiniMax H3 vs Flux 3 Pro](https://www.reddit.com/r/StableDiffusion/comments/1vm775g/ice_cream_ad_minimax_h3_vs_flux_3_pro/)
- **Model attribution:** The creator explicitly labels one comparison output “Flux 3 pro” and states that the same prompt was used for Flux 3 and MiniMax H3.
- **Summary:** A vertical 15-second ice-cream commercial keeps one photorealistic young woman recognizable through multiple outfit and setting changes, shifting between flat graphic-animation backgrounds and product-focused realism while using in-frame transitions, product close-ups, synchronized effects, and a final lip-synced line.
- **Workflow/details:** Same prompt used for both models. The visible prompt specifies 9:16, 15 seconds, 50 mm medium/waist-up framing for character shots, a final product close-up, time-coded transition beats, strict face/body consistency, no subtitles or music, and synchronized sound directions. The creator separately states that MiniMax H3 used 0.8 MP, no speed LoRA, Spectrum and Sage Attention at 20 steps; the FLUX 3 service’s exact resolution and generation settings are not disclosed, so the creator’s “probably 720p” remark is not treated as verified.
- **Prompt provenance:** `verbatim_in_post` — “9:16 vertical, 15 seconds, high-saturation commercial style: photo-realistic character on flat graphic animation backgrounds”. The complete time-coded prompt remains visibly published in the original thread.
- **Why included:** Newly published primary creator post with attached comparison media, explicit Flux 3 Pro attribution, a same-prompt cross-model setup, and an unusually reproducible commercial brief that stress-tests identity across outfit changes, transition choreography, stylized/photoreal compositing, product-text rendering, synchronized effects, and English lip-sync.

### 100. Minimal-prompt medieval peasants meet an escalator — Blendi

- **Creator:** [Blendi (@BlendiByl)](https://x.com/BlendiByl)
- **Published:** Date not exposed; verified 2026-08-13
- **Original source profile:** [Blendi on X](https://x.com/BlendiByl) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary public mirror directly quoting the original creator post, exact prompt, explicit model attribution, attached-video context, and engagement](https://www.twstalker.com/johnsavage_ai)
- **Model attribution:** The preserved original creator post explicitly introduces the attached generation with “flux 3 prompt:” before the visible prompt text.
- **Summary:** Medieval peasants encounter a modern escalator, turning a deliberately tiny anachronistic premise into a visual-comedy and world-model test of period characters reacting to unfamiliar moving infrastructure.
- **Workflow/details:** Text-to-video from one very short natural-language prompt with no visible shot list, camera directions, or detailed staging. Duration, resolution, seed, reference media, audio settings, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “Medieval peasants encountering an escalator”
- **Why included:** Newly surfaced creator-attributed FLUX 3 video with an exact highly reusable minimal prompt, roughly three thousand views and 44 likes in the preserved snapshot, and a compact but difficult test of anachronistic world understanding, human reaction, mechanical motion, spatial interaction, and comedic readability from almost no explicit direction.

### 101. Ant-scale Formula 1 racing concept — Blendi

- **Creator:** [Blendi (@BlendiByl)](https://x.com/BlendiByl)
- **Published:** Date not exposed; verified 2026-08-13
- **Original source profile:** [Blendi on X](https://x.com/BlendiByl) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary public mirror directly preserving the original creator post and its engagement context](https://www.twstalker.com/johnsavage_ai)
- **Model attribution:** Blendi explicitly calls the attached work “my favorite flux 3 generation yet” and states that the prompt is provided below the creator post.
- **Summary:** A miniature Formula 1 racing concept built around ants, using a compact surreal premise to test scale, fast motion, racing readability, and physically coherent interaction at macro size.
- **Workflow/details:** The verified public mirror preserves the creator’s FLUX 3 attribution and the concept label “Ant F1 racing,” but does not expose the full prompt text, duration, resolution, seed, reference media, audio settings, or post-production.
- **Prompt provenance:** `mentioned_not_in_post` — Blendi explicitly says “Prompt below 👇,” but the prompt text itself is not visible in the accessible verification source, so no wording has been reconstructed or inferred.
- **Why included:** Fresh original-creator FLUX 3 attribution, roughly four thousand views and 84 likes in the preserved snapshot, the creator’s own “favorite generation yet” quality signal, and a distinctive macro-scale action concept that differs clearly from the already-listed medieval-escalator example.


### 102. Believable TikTok/Reels-style short-form realism — DΞV

- **Creator:** [DΞV (@junwatu)](https://x.com/junwatu)
- **Published:** Date not exposed; verified 2026-08-13
- **Original source profile:** [DΞV on X](https://x.com/junwatu) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary public mirror directly quoting the original creator post, explicit FLUX 3 attribution, short-form-video wording, and engagement](https://www.twstalker.com/johnsavage_ai)
- **Model attribution:** DΞV explicitly says FLUX 3 is good at creating TikTok- and Reels-style videos and describes the results as very believable.
- **Summary:** A creator-posted short-form social-video realism test targets the feed-native visual grammar of TikTok and Instagram Reels rather than polished cinematic footage, emphasizing everyday authenticity and the kind of natural capture style viewers associate with real social posts.
- **Workflow/details:** Creator-posted FLUX 3 short-form video generation. The verified public source does not expose duration, resolution, seed, reference inputs, exact prompt, audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the visible creator caption describes the target format and perceived realism but does not present generation prompt text.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, a clearly identified short-form-video use case, and a realism target distinct from the cinematic and documentary examples already curated. The preserved snapshot shows roughly 2K views and 39 likes, while the secondary verifier independently characterizes the result as not looking AI-generated.

### 103. Authentic 1990s soap-opera benchmark vs. Seedance 2.0 — Vlad Dubchak

- **Creator:** [Vlad Dubchak (@vladdubchak_x)](https://x.com/vladdubchak_x)
- **Published:** Date not exposed; verified 2026-08-13
- **Original source profile:** [Vlad Dubchak on X](https://x.com/vladdubchak_x) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary public mirror directly quoting the original creator comparison, explicit Flux 3 attribution, video-style target, and engagement](https://www.twstalker.com/johnsavage_ai)
- **Model attribution:** Dubchak explicitly frames the attached work as another “Flux 3 vs Seedance 2.0” round and evaluates which model can reproduce an authentic 1990s soap-opera style.
- **Summary:** A direct cross-model video comparison asks FLUX 3 and Seedance 2.0 to reproduce the recognizable look and media grammar of a 1990s soap opera, using period-style authenticity rather than generic cinematic polish as the differentiator.
- **Workflow/details:** Side-by-side or paired cross-model benchmark between Flux 3 and Seedance 2.0. The verified public source does not expose the exact shared prompt, duration, resolution, seed, reference media, audio settings, or post-production, so none of those details are inferred.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified source.
- **Why included:** Fresh original-creator Flux 3 attribution, a clearly stated comparison against Seedance 2.0, roughly 4K views in the preserved creator-post snapshot, and a useful style-fidelity benchmark focused on whether a model can reproduce the distinctive texture and pacing of 1990s television rather than merely generate a plausible-looking scene.

### 104. Analog-horror Michael Jackson vignette — Kadeka

- **Creator:** [Kadeka (@Berserkr_777)](https://x.com/Berserkr_777)
- **Published:** 2026-08-12 (based on the public verification mirrors’ relative timestamps)
- **Original source profile:** [Kadeka on X](https://x.com/Berserkr_777) — the accessible public indexes did not expose a stable direct status URL.
- **Verification sources:** [Secondary public mirror preserving a retweet of the original Kadeka post, explicit Flux 3 wording, and engagement](https://mobile.twstalker.com/KeyTryer) · [Independent public mirror preserving the same original creator post](https://twstalker.com/ZachyAshworth)
- **Model attribution:** Kadeka explicitly says, “Analog Horror Michael Jackson videos were not on my Flux 3 bingo card.”
- **Summary:** A Michael Jackson-themed analog-horror video uses the degraded, uncanny grammar of found-footage horror rather than polished cinematic imagery, making recognizable celebrity imagery collide with an intentionally unsettling archival-video aesthetic.
- **Workflow/details:** Creator-posted FLUX 3 video. The verified public mirrors preserve the explicit model attribution and attached-post context but do not expose duration, resolution, seed, reference media, exact prompt, audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the visible creator caption describes the concept but does not present generation prompt text, so no prompt has been reconstructed or inferred.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, clear identification as a video, roughly 3K–5K views and 44–70 likes across preserved snapshots, and a distinctive analog-horror style test that differs materially from Kadeka’s existing VHS-to-IMAX camera-format experiment.


### 105. Twenty-second Japanese fantasy creature-selection sequence — Pablo Prompt

- **Creator:** [Pablo Prompt (@pabloprompt)](https://x.com/pabloprompt)
- **Published:** Date not exposed; verified 2026-08-13
- **Original source profile:** [Pablo Prompt on X](https://x.com/pabloprompt) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving Pablo Prompt’s original FLUX 3 wording, attached-video context, full prompt, and engagement](https://www.twstalker.com/pabloprompt)
- **Model attribution:** Pablo explicitly says this is one of his first videos created with FLUX 3 after receiving early access, then posts the generation prompt directly beneath it.
- **Summary:** A live-action Japanese coming-of-age fantasy sequence follows a 15-year-old arriving late at a hilltop research laboratory, choosing one of three metallic spheres, and releasing a small ember-marked fox-like creature, with Japanese dialogue and a warm cinematic visual language across the full clip.
- **Workflow/details:** Text-to-video; exactly 20 seconds; nine time-coded beats from 0–20s; live-action 35mm-grain look with warm amber/soft-teal grading; clean multi-angle cuts; diegetic sound only; Japanese dialogue with explicit lip-sync direction; detailed continuity specifications for the teenager, professor, three identical devices, and creature; negative constraints prohibit text, subtitles, logos, anime styling, and a CGI look.
- **Prompt provenance:** `verbatim_in_post` — “Cinematic live-action Japanese coming-of-age fantasy film. Modern hilltop research laboratory, warm morning sunlight through large windows, shallow depth of field, 35mm grain, warm amber and soft teal grading, clean cuts between angles, diegetic sound only. Exactly 20 seconds. TEENAGER: 15-year-old Japanese boy, messy black hair, worn red baseball cap with black brim, light blue baseball jersey over a black T-shirt, jeans, green backpack. PROFESSOR: Japanese man in his mid-60s, gray hair, white lab coat over a red polo shirt. DEVICES: Three identical tennis-ball-sized metallic spheres, glossy royal-blue top half with a yellow stripe, white bottom half, white central button. CREATURE: A cat-sized fox-like quadruped, burnt ginger-orange fur, cream white muzzle and belly, dark paws, copper-amber eyes, two tiny black horn nubs, glowing ember cracks on its shoulders and a big bushy crimson tail burning like a living flame. Real fur always visible, never a body made of fire. 0-2s: [Wide Tracking] He sprints up a gravel path to the laboratory, breathless, dust rising. 2-4s: [Interior Medium] The door slides open, he stumbles in, bows and gasps in Japanese: \"すみません！遅れました！\" 4-6s: [Reverse Medium] The professor turns from his workbench, smiles and says in Japanese: \"やっと来たな。さあ、選びなさい。\" 6-8s: [Slow Push-In] He pulls a white cloth off a metal pedestal revealing exactly three identical spheres. Insert on the boy's wide eyes. 8-11s: [Over-the-Shoulder] He steps closer, hand hovering hesitantly over each sphere, then looks back at the professor, who nods. 11-12.5s: [Close-Up] He grabs one, lifts it to eye level and whispers in Japanese: \"決めた。\" Two spheres remain behind him. 12.5-14s: [Low Angle] He throws it at the polished floor, it spins, bounces with a metallic sound and rests intact without breaking. 14-16s: [Floor-Level Close-Up] The button pulses gold, the seam parts and a compact spiral of golden-orange energy and embers rises above it. 16-18s: [Low-Angle Reveal] The energy condenses into the creature, fur forming beneath the fading sparks. It lands on all fours and shakes off a cloud of embers. 18-20s: [Intimate Close-Up] It looks up, tilts its head and chirps. He crouches grinning and says in Japanese: \"よろしくな。\" It presses its head into his palm, tail swaying, embers drifting. Photorealistic skin and fur detail, accurate Japanese lip sync, seamless continuity and identical character design across every cut, no text, no subtitles, no logos, no anime style, no CGI look.”
- **Why included:** Fresh original-creator FLUX 3 attribution with substantial early engagement, an exact full prompt, and unusually dense reproducible direction. The single generation stress-tests nine-shot continuity, object counts and persistence, Japanese speech/lip sync, human interaction, transformation effects, creature identity, fur/fire separation, sound, and cinematic editing over a full 20 seconds.

### 106. Deliberately anti-climactic “goes nowhere” narrative prompt — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-12 (based on the public verification mirror’s relative timestamp)
- **Original source profile:** [Christopher Fryant on X](https://x.com/cfryant) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving Fryant’s original wording, explicit FLUX 3 attribution, public prompt text, attached-video context, and engagement](https://twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly introduces the attached result with “I love this FLUX 3 prompt!” and tags Black Forest Labs.
- **Summary:** A deliberately misleading narrative clip is prompted to look as though it is building toward a meaningful destination or payoff, only to resolve by intentionally wasting the viewer’s time. The concept turns anti-climax itself into the generation target rather than merely describing a visual scene.
- **Workflow/details:** Prompt-led FLUX 3 generation from a short meta-narrative instruction. Fryant notes that a more advanced version of the prompt is available only to subscribers; that paywalled text was not accessed, copied, or reconstructed. Duration, resolution, seed, reference media, audio instructions, and post-production are not publicly disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — “Video that looks like it's really going somewhere but then ends up wasting everyone's time.” This is the publicly visible base prompt; the separately mentioned subscriber-only advanced version is intentionally excluded.
- **Why included:** Explicit original-creator FLUX 3 attribution, a publicly visible reusable prompt, attached-video context, and strong engagement in the preserved snapshot (about 20K views and 79 likes). More importantly, it is a distinctive test of high-level narrative intent: pacing, expectation-setting, apparent story progression, and an intentional anti-climactic payoff from one compact instruction.

### 107. Rain-soaked Chinese alley relationship drama — Practical_Low29

- **Creator:** [Practical_Low29](https://www.reddit.com/user/Practical_Low29/)
- **Published:** 2026-08-13
- **Original source:** [Reddit creator post with attached FLUX 3 video and full prompt](https://www.reddit.com/r/FluxAI/comments/1vn4z31/first_flux_3_test_surprisingly_realistic/)
- **Model attribution:** The original creator explicitly titles the post “First Flux 3 test, surprisingly realistic” and states that this was their first Flux 3 test.
- **Summary:** A restrained late-night relationship argument unfolds in a rain-wet Chinese residential alley across three hard-cut beats: a woman walks away from a man, confronts him outside a noodle shop, then ends the exchange after a long silence while an electric scooter passes behind them.
- **Workflow/details:** One 20-second text-to-video prompt with three explicitly staged hard cuts. The prompt specifies Mandarin dialogue, a handheld follow shot for beat one, an eye-level 50 mm two-shot for beat two, a static wide shot for beat three, practical wet-street reflections, restrained acting and facial emotion, and diegetic ambience only—footsteps, extractor fan, distant traffic, scooter and breathing—with no music, subtitles, or on-screen text. The creator reports that FLUX 3 handled wet pavement, night lighting, awkward pauses, subtle expressions, and overall realism especially well, while judging fight choreography and flashy effects weaker than Seedance 2.0.
- **Prompt provenance:** `verbatim_in_post` — the complete prompt is visibly published in the original creator post:

> A 20-second scene in a narrow residential alley in a Chinese city late at night, in three hard-cut beats. The ground is still wet from rain and reflects the warm yellow lightbox of a small noodle shop.
>
> A young Chinese woman walks quickly away from the camera with her arms crossed. A young Chinese man catches up beside her and says quietly in Mandarin: “你能不能别走这么快。” She doesn’t answer.
>
> HARD CUT.
>
> She stops and turns to face him, speaking quietly so the neighbors won’t hear: “你根本就没听我说话。” He starts to reach for her arm but stops halfway. “……我听了。” She looks at him and asks: “那你说我刚才说什么了。”
>
> HARD CUT.
>
> He says nothing. Three full seconds of silence. Her eyes turn red, but no tears fall. She looks away, exhales, and says quietly: “算了。” Neither of them moves as an electric scooter passes behind them.
>
> Camera: handheld follow shot for the first beat, an eye-level 50mm two-shot for the second, and a static wide shot from the far end of the alley for the third.
>
> Audio: quiet tired voices, footsteps on wet pavement, the noodle shop’s extractor fan, distant traffic, a passing electric scooter, and his slightly heavy breathing. No music, no subtitles, no on-screen text.

- **Why included:** Newly published primary creator post with attached video, explicit Flux 3 attribution, and a fully reproducible prompt. It is a high-signal realism test because the difficulty comes from understated performance rather than spectacle: multilingual dialogue, three-shot continuity, subtle facial acting, held silence, interrupted physical gesture, environmental reflections, background traffic causality, and tightly specified native audio all have to remain coherent across a full 20-second scene.

### 108. Multi-character color-coded destination steering — FossyCat

- **Creator:** [FossyCat (@FossyCatAI)](https://x.com/FossyCatAI)
- **Published:** Date not exposed; verified 2026-08-14
- **Original source profile:** [FossyCat on X](https://x.com/FossyCatAI) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording and attached-media test](https://www.twstalker.com/FossyCatAI)
- **Model attribution:** FossyCat explicitly introduces the result with “More Flux 3 testing.”
- **Summary:** A multi-character motion-control test guides separate characters toward predetermined destinations while trying to prevent either character from drifting away from its assigned target.
- **Workflow/details:** The creator says the prompt assigns each character to a color-coded space, using those visually distinct destination regions as control anchors. The public source does not expose duration, resolution, seed, reference media, exact prompt text, audio settings, or post-production.
- **Prompt provenance:** `mentioned_not_in_post` — the creator explains the prompt strategy (“prompt guides each character to color-coded space”) but does not publish the exact generation prompt, so no wording has been reconstructed or inferred.
- **Why included:** Fresh explicit original-creator Flux 3 attribution and a highly reusable spatial-control idea. The test targets independent multi-character trajectory adherence, destination binding, identity separation, and drift prevention rather than generic aesthetics, making it a useful technical benchmark for choreographing several subjects in one generation.

### 109. Mechanical-dragon interaction and fire-breath comparison — jefharris

- **Creator:** [jefharris](https://www.reddit.com/user/jefharris/)
- **Published:** 2026-08-14
- **Original source:** [MiniMaxH3 vs Flux3](https://www.reddit.com/r/StableDiffusion/comments/1vo7eo3/minimaxh3_vs_flux3/)
- **Model attribution:** The original creator explicitly titles the comparison “MiniMaxH3 vs Flux3” and states that the Flux 3 video was created through the official Black Forest Labs page with all default settings.
- **Summary:** A woman gently pets the neck of a massive mechanical dragon; both turn toward camera before the dragon rears back, roars, and fires a blast directly into the lens, providing a same-prompt comparison against MiniMax H3.
- **Workflow/details:** The creator used MiniMax H3’s official ComfyUI image-to-video workflow for the comparison side and generated the Flux 3 side on Black Forest Labs’ official page with all default settings. The visible prompt coordinates tactile hand-to-metal contact, servo-driven neck motion, eye contact, a camera push-in, fire directed at the camera, and diegetic mechanical, breathing, roar, and flame audio with no music.
- **Prompt provenance:** `verbatim_in_post` — “The woman raises her left hand and reaches out toward the dragon's neck, fingertips making contact with the cool metal scales”. The complete prompt remains visible in the original Reddit post.
- **Why included:** Newly published primary creator post with attached comparison video, explicit Flux 3 attribution, a visible reproducible prompt, verified use of the official BFL interface and defaults, and a demanding combination of human-creature interaction, scale, articulated mechanical motion, gaze, fire physics, camera timing, and synchronized diegetic audio.

## How updates work

The hourly ChatGPT task checks this README first, searches for newer qualifying sources, rejects duplicates and ambiguous attribution, then appends verified entries here. It reports only when at least one new entry has been successfully committed.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Repository text and curation structure are licensed under the [MIT License](LICENSE). Linked post text, prompts, media, creator names, and other third-party material remain the property of their respective authors.
