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

_Last updated: 2026-07-28 · Entries: 35_

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

## How updates work

The hourly ChatGPT task checks this README first, searches for newer qualifying sources, rejects duplicates and ambiguous attribution, then appends verified entries here. It reports only when at least one new entry has been successfully committed.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Repository text and curation structure are licensed under the [MIT License](LICENSE). Linked post text, prompts, media, creator names, and other third-party material remain the property of their respective authors.