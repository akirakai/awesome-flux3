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

_Last updated: 2026-08-03 · Entries: 60_

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
- **Workflow/details:** Reported as one FLUX 3 generation with picture and native audio produced together; the source specifically notes the gym environment, interview staging, handheld camera feel, microphone audio, and dialogue synchronization. Exact duration, references, seed, and post-production are not disclosed.
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

## How updates work

The hourly ChatGPT task checks this README first, searches for newer qualifying sources, rejects duplicates and ambiguous attribution, then appends verified entries here. It reports only when at least one new entry has been successfully committed.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Repository text and curation structure are licensed under the [MIT License](LICENSE). Linked post text, prompts, media, creator names, and other third-party material remain the property of their respective authors.