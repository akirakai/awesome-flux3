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

_Last updated: 2026-08-23 · Entries: 160_

-->

## Curated videos

_Last updated: 2026-09-17 · Entries: 234_

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
- **Summary:** A GoPro-style first-person sequence places the viewer inside a giant mech fighting a kaiju in Seattle, ending with the Space Needle used as a weapon.
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
- **Verification source:** [Secondary creator-profile mirror preserving the creator post and video](https://www.sotwe.com/Ridho_Mrr)
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
- **Published:** 2026-08-06
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
- **Published:** 2026-08-06
- **Original source profile:** [Future Vibes AI on X](https://x.com/FutureVibesAi) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, exact prompt, clip context, and engagement](https://mobile.twstalker.com/FutureVibesAi)
- **Model attribution:** The creator explicitly introduces the clip with “Split Screen clip with Flux 3.”
- **Summary:** A passenger aircraft’s single-engine failure and controlled return are shown simultaneously from the cabin, an exterior tracking camera, the cockpit, and an aerial view, with the failure, reactions, stabilization, and return path synchronized across all four panels.
- **Workflow/details:** Four synchronized camera panels; the engine failure is anchored at the 2-second mark, followed by brief yaw, immediate pilot correction, passenger reaction, stabilization, and a controlled return toward the airport while emergency vehicles prepare. The prompt requires matching aircraft attitude, engine behavior, pilot actions, passenger reactions, weather, and flight path across every view. Duration, resolution, seed, reference inputs, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Four-way synchronized cinematic split-screen showing the same passenger aircraft experiencing a single-engine failure shortly after takeoff.” The complete prompt remains visible in the verification source.
- **Why included:** Newly published explicit creator attribution, an exact reproducible prompt, strong public engagement, and a demanding multi-camera test of procedural aviation behavior, aerodynamics, causal timing, human reactions, and scene geometry.

### 74. Four-way synchronized mountain helicopter rescue — Future Vibes AI

- **Creator:** [Future Vibes AI (@FutureVibesAi)](https://x.com/FutureVibesAi)
- **Published:** 2026-08-05
- **Original source profile:** [Future Vibes AI on X](https://x.com/FutureVibesAi) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, exact prompt, clip context, and engagement](https://mobile.twstalker.com/FutureVibesAi)
- **Model attribution:** The creator explicitly introduces the clip with “Split screen clip with Flux 3.”
- **Summary:** A dangerous alpine helicopter rescue is shown simultaneously from the cabin, an exterior side-following view, the cockpit, and an aerial camera as a wind gust destabilizes the hover and a stranded climber is extracted by cable.
- **Workflow/details:** Four synchronized camera panels; at the 2-second mark a strong wind pushes the helicopter sideways, the pilot corrects, the rescue crew lowers a cable, the climber is secured and lifted, and rotor wash drives snow around the aircraft. The prompt requires matching helicopter orientation, cable movement, wind direction, rotor wash, climber position, and lighting across every view. Duration, resolution, seed, reference inputs, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Four-way perfectly synchronized split-screen showing the same helicopter rescue operation during a dangerous mountain snowstorm.” The complete prompt remains visible in the verification source.
- **Why included:** Newly published explicit creator attribution, an exact reproducible prompt, and a physically demanding multi-view rescue sequence combining aircraft control, cable dynamics, weather, rotor wash, spatial consistency, and synchronized causal action.

### 75. Four-way synchronized emergency airplane river landing — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-08-04
- **Original source profile:** [Umesh on X](https://x.com/umesh_ai) — the public index did not expose the direct status URL.
- **Verification source:** [Secondary creator-post mirror preserved through a Future Vibes AI profile retweet, including the original creator wording, prompt opening, attached-video context, and engagement](https://mobile.twstalker.com/FutureVibesAi)
- **Model attribution:** Umesh explicitly introduces the attached result with “Another 4-way split screen clip with Flux 3!”
- **Summary:** An emergency airplane river landing is presented simultaneously from four synchronized camera perspectives, with each panel continuously following the same aircraft while the viewpoint-specific visuals evolve through the event.
- **Workflow/details:** Four-way split-screen text-to-video with synchronized viewpoints and continuous tracking of one aircraft. The public verification extract preserves the cross-camera synchronization requirement and the beginning of the panel-by-panel prompt, but does not expose the complete camera descriptions, duration, resolution, seed, reference inputs, or post-production.
- **Prompt provenance:** `verbatim_in_post` — “Four-way split-screen showing the same emergency airplane river landing from four synchronized camera perspectives.” The verified source also visibly states that each panel follows the aircraft continuously as the event unfolds.
- **Why included:** Explicit original-creator attribution, attached-video context, a visible reproducible prompt opening, strong public engagement, and a demanding multi-view stress test of aircraft identity, continuous tracking, event timing, spatial consistency, and synchronized action over water.

### 76. Regency-manor astronaut tracking-shot stress test — Ethan Mollick

- **Creator:** [Ethan Mollick (@emollick)](https://x.com/emollick)
- **Published:** 2026-08-07
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
- **Published:** 2026-08-07
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the accessible public index did not expose a stable direct status URL.
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
- **Published:** 2026-08-06
- **Original source profile:** [Jin.B on X](https://x.com/opener_ai) — the public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, full structured prompt, and engagement](https://mobile.twstalker.com/opener_ai)
- **Model attribution:** Jin.B explicitly says the attached comparison runs “Flux 3 vs Seedance 2.0” and describes using closely matched timing/settings for the two outputs.
- **Summary:** A photorealistic stormy-coastal kaiju sequence pits a skyscraper-scale deep-sea octopus against a city, with the creature crushing buses and streetlights, pulling down a glass tower, sprinting through intersections, vaulting a full block, and charging through waterfront cranes.
- **Workflow/details:** Controlled cross-model comparison from one highly structured prompt. The visible setup specifies 15 seconds, rapid creature movement, controlled cameras, five time-coded camera/action beats, storm lighting, VFX, native audio design, and hard constraints to keep all eight tentacles connected, distinct, and readable while avoiding anatomy drift, flicker, weightless debris, and chaotic camera motion. Jin.B notes using closely matched 20s/15s settings for the two models.
- **Prompt provenance:** `verbatim_in_post` — “Build the monster, city, scale, and destruction entirely from text. … Photorealistic kaiju disaster film, stormy coastal metropolis, grounded structural destruction. … A colossal deep-sea octopus taller than nearby skyscrapers. … It never stops or poses. Four tentacles pull its body rapidly forward while the others destroy obstacles.” The complete time-coded prompt remains visible in the verification source.
- **Why included:** Original-creator attribution, attached comparison video, a visible reproducible structured prompt, substantial public engagement, and an unusually difficult benchmark of multi-limb anatomy, fast physical action, time-coded cinematography, city-scale destruction, weather, debris, audio, and cross-model prompt adherence.

### 81. Blackout-disappearance subway FLUX 3 vs. Seedance 2.0 benchmark — Jin.B

- **Creator:** [Jin.B (@opener_ai)](https://x.com/opener_ai)
- **Published:** 2026-08-07
- **Original source profile:** [Jin.B on X](https://x.com/opener_ai) — the public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original comparison caption, attached-video context, and FLUX 3 prompt follow-up](https://mobile.twstalker.com/opener_ai)
- **Model attribution:** Jin.B explicitly says the attached comparison tests “Flux 3 & Seedance 2.0,” tags `#Flux3` and Black Forest Labs, then publishes a follow-up labeled “[Flux3 prompt].”
- **Summary:** A single continuous first-person subway shot uses timed blackouts to make passengers disappear while the moving train, camera sway, surviving passengers, empty seats, abandoned objects, and later ceiling impacts preserve scene continuity.
- **Workflow/details:** Controlled cross-model comparison from a Claude Opus 5-authored prompt. The visible FLUX 3 brief specifies a moving nighttime subway car, continuous POV with no cuts, handheld/body-cam rocking, cold green-cyan lighting, blue tunnel strobes, staged passenger disappearances across three blackouts, then a sequence of physically progressive ceiling impacts. It runs to 20 seconds and includes explicit native-audio cues such as rail clatter, fluorescent buzz, ballast clicks, metallic cracks, glass shattering, and bending steel.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Single continuous first-person POV shot, no cuts. A standing passenger inside a moving subway car at night. The entire frame rocks and jolts with the train throughout, handheld body-cam energy.” The complete 20-second FLUX 3 prompt remains visible in the verification source.
- **Why included:** Newly published original-creator comparison with explicit FLUX 3 labeling, attached video, exact visible prompt, controlled shared-prompt methodology, and a difficult test of temporal continuity, disappearing-character logic, lighting transitions, handheld motion, object persistence, progressive physical damage, audio timing, and scene-state consistency.

### 82. Pelican shoegaze band “Pelicans on Bikes” — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** 2026-08-08
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the public indexes did not expose the direct status URL.
- **Verification sources:** [Secondary mirror preserving fofr’s follow-up and its quoted same-creator FLUX 3 parent post](https://twstalker.com/ZachyAshworth); [Black Forest Labs co-founder Robin Rombach’s public profile mirror resharing the follow-up](https://site.twstalker.com/robrombach).
- **Model attribution:** The follow-up is shown directly beneath and quoting fofr’s immediately preceding same-creator post, which explicitly prefixes the generation series with “Flux 3:”. Robin Rombach then reshared the “Pelicans on Bikes” follow-up and praised its prompting.
- **Summary:** A deliberately bootleg-looking phone recording captures a shoegaze band named “Pelicans on Bikes” introducing itself in a small venue and launching into its first song, while every performer is rendered as an actual pelican.
- **Workflow/details:** Prompt-led generation using an intentionally low-fi phone-recording aesthetic, a small live venue, spoken band introduction, a named first song (“SVG”), and non-human performers. Duration, resolution, seed, reference media, and post-production are not disclosed in the verified sources.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “bootlegged phone recording of a shoegaze band called \"Pelicans on Bikes\" playing in a small venue, they introduce themselves”. The remaining prompt text is visibly preserved in the verification source.
- **Why included:** Newly published same-creator FLUX 3 thread attribution, visible prompt text, strong public engagement, and first-party signal from Black Forest Labs co-founder Robin Rombach. The result is a distinctive audiovisual stress test of animal identity consistency, live-band staging, spoken introduction, generated music/performance timing, and convincing low-fi phone capture.

### 83. 1995 television documentary explaining the internet — Bennett / Generative Media

- **Creator:** [Bennett | Generative Media | AI SEO @ fal (@influencer_seo)](https://x.com/influencer_seo)
- **Published:** 2026-08-08
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
- **Why included:** Traceable original status, explicit creator attribution, thousands of early views, and a distinctive compact concept that stresses multi-character staging, escalation, action timing, and comedic readability without relying on a long visible prompt for each model.

### 85. Household spider-removal comedy — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-06
- **Original post:** [View on X](https://x.com/cfryant/status/2085492904286396422)
- **Verification source:** [Secondary creator-profile mirror preserving the original wording, attached-video context, and engagement](https://twstalker.com/cfryant/status/2085492904286396422)
- **Model attribution:** Fryant explicitly captions the clip “When your girlfriend tells you to take care of a spider. FLUX 3”.
- **Summary:** A familiar household request to deal with a spider is turned into an exaggerated visual-comedy scenario, using an immediately legible everyday setup as the joke’s anchor.
- **Workflow/details:** Creator-posted FLUX 3 video from an experienced AI filmmaker. The public verification source preserves the concept and strong early engagement but does not disclose duration, exact generation prompt, input references, seed, resolution, audio instructions, or post-production.
- **Prompt provenance:** `not_provided` — the caption states the premise but is not labeled as the exact generation prompt, and nothing has been reconstructed from the footage.
- **Why included:** Explicit original-creator FLUX 3 attribution, attached-video verification, strong public engagement, and a concise comedy setup that provides a useful test of believable everyday context, reaction timing, and escalation.

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
- **Published:** 2026-08-07 (based on the public verification mirror’s relative timestamp at verification).
- **Original source profile:** [Christopher Fryant on X](https://x.com/cfryant) — the accessible public index did not expose the direct status URL.
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
- **Published:** 2026-08-12
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
- **Prompt provenance:** `verbatim_in_post` — full prompt remains visible in the verification source.
- **Why included:** Fresh original-creator FLUX 3 attribution with substantial early engagement, an exact full prompt, and unusually dense reproducible direction. The single generation stress-tests nine-shot continuity, object counts and persistence, Japanese speech/lip sync, human interaction, transformation effects, creature identity, fur/fire separation, sound, and cinematic editing over a full 20 seconds.

### 106. Deliberately anti-climactic “goes nowhere” narrative prompt — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-12
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
- **Workflow/details:** One 20-second text-to-video prompt with three explicitly staged hard cuts. The prompt specifies Mandarin dialogue, a handheld follow shot for beat one, an eye-level 50 mm two-shot for beat two, a static wide shot for beat three, practical wet-street reflections, restrained acting and facial emotion, and diegetic ambience only—footsteps, extractor fan, distant traffic, scooter and breathing—with no music, subtitles, or on-screen text.
- **Prompt provenance:** `verbatim_in_post` — the complete prompt is visibly published in the original creator post.
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

### 110. Amsterdam bookshop cat with layered native audio — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-08-04 (date shown on the Runware FLUX 3 model guide)
- **Original source:** [Runware FLUX 3 prompting guide with embedded generated clip and request code](https://runware.ai/docs/models/bfl-flux-3-video/guides/prompting)
- **Model attribution:** Runware explicitly identifies the page as Black Forest Labs’ FLUX 3 Video and the exact generation request uses model ID `bfl:flux@3-video`.
- **Summary:** A continuous rainy-afternoon shot begins on an empty Amsterdam bookshop, pans across the shelves, and settles on a tabby cat; a distant thunder roll coincides with the cat’s ear twitch while room tone, a wall clock, rain, and thunder form layered native audio.
- **Workflow/details:** Single text-to-video API call; 10-second duration; 1280×704; exact `positivePrompt` visibly published in both prose and request code. Runware states the clip above came from that single call; the model returns an MP4 with synchronized audio, and audio is enabled by default in this workflow. No reference media or post-production are disclosed for the hero example.
- **Prompt provenance:** `verbatim_in_post` — “An unbroken continuous 10-second shot inside a small independent bookshop on a rainy autumn afternoon in Amsterdam. Warm interior lighting from dim brass sconces…” The complete prompt remains visible in the source.
- **Why included:** A first-party generation-platform guide pairs an embedded FLUX 3 output with the exact model ID, request dimensions, duration, and visible prompt. It is unusually reproducible and simultaneously tests directed hold-then-pan camera motion, subtle event-timed animal behavior, interior realism, and synchronized multi-layer ambience.

### 111. Formula-car finish-line continuation with victory salute — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-08-04 (date shown on the Runware FLUX 3 model guide)
- **Original source:** [Runware FLUX 3 video-continuation guide with generated continuation and request code](https://runware.ai/docs/models/bfl-flux-3-video/guides/video-continuation)
- **Model attribution:** Runware identifies the page as Black Forest Labs’ FLUX 3 Video and the request code uses model ID `bfl:flux@3-video`.
- **Summary:** A red Formula-style car crosses the finish line at full speed; the generated continuation opens on that terminal frame, decelerates toward the paddock, and has the driver raise a gloved victory salute while the engine and crowd audio evolve with the action.
- **Workflow/details:** Video-to-video continuation through `inputs.video`; one source clip; 8-second continuation at 720p; native audio. The source’s final frames anchor the car identity, track, camera position, lighting, subject state, and ambient audio while the prompt directs the new action.
- **Prompt provenance:** `verbatim_in_post` — “Continue the reference video from its final frames. The racing car decelerates smoothly over the next three seconds…” The complete prompt remains visible in the source.
- **Why included:** First-party generated-video evidence with a visible source clip, exact model ID, prompt, reference count, duration, and resolution; it is a demanding benchmark of temporal, visual, physical, and audio continuity across a video-to-video boundary.

### 112. First-frame chef-knife and lime animation — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-08-04 (date shown on the Runware FLUX 3 model guide)
- **Original source:** [Runware FLUX 3 keyframes guide with source image, generated video, and request code](https://runware.ai/docs/models/bfl-flux-3-video/guides/keyframes)
- **Model attribution:** Runware identifies the guide as Black Forest Labs’ FLUX 3 Video; the exact request uses model ID `bfl:flux@3-video`.
- **Summary:** A product-packshot image of a walnut-handled Damascus chef’s knife becomes an 8-second video in which a hand picks up the knife and slices a lime while preserving the source composition and warm product lighting.
- **Workflow/details:** One image reference pinned to `frameImages[0].frame = "first"`; 8 seconds; 720p; native audio with knife, board, and kitchen ambience. Runware notes that the opening source is a strong visual anchor rather than a pixel-identical lock.
- **Prompt provenance:** `verbatim_in_post` — “Use this image as the first frame. An 8-second clip: the camera holds locked on the knife for a beat…” The complete prompt remains visible in the source.
- **Why included:** First-party embedded source/output pairing with exact reference placement, model ID, duration, resolution, and prompt; it cleanly tests first-frame fidelity, hand-object interaction, product-material continuity, motion onset, and synchronized foley.

### 113. Home-podcast lip-sync with layered native ambience — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-08-04 (date shown on the Runware FLUX 3 model guide)
- **Original source:** [Runware FLUX 3 audio-and-speech guide with generated clip and request code](https://runware.ai/docs/models/bfl-flux-3-video/guides/audio-and-speech)
- **Model attribution:** Runware identifies the page as Black Forest Labs’ FLUX 3 Video and the exact request uses model ID `bfl:flux@3-video`.
- **Summary:** A woman in a home podcast studio delivers a quoted line directly into a brass microphone while FLUX 3 synchronizes her mouth to the words and layers room tone, laptop-fan hum, and distant traffic into the same generated MP4.
- **Workflow/details:** One text-to-video request; 8 seconds; 704×1280. Audio is generated in the same request and enabled by default; the visible-speaker-plus-quoted-line pattern is used for lip-sync, with explicit no-music, no-text, and no-subtitles constraints.
- **Prompt provenance:** `verbatim_in_post` — “An 8-second interior shot in a home podcast studio. A woman in her late twenties with a warm auburn bob…” The complete prompt remains visible in the source.
- **Why included:** First-party embedded result with exact model ID, dimensions, duration, dialogue pattern, and audio design; it is a reproducible test of speech generation, lip-sync, portrait framing, and multiple spatial ambience layers without a post-hoc audio pass.

### 114. Three-cut boutique coffee commercial with continuous music bed — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-08-04 (date shown on the Runware FLUX 3 model guide)
- **Original source:** [Runware FLUX 3 multi-shot-sequences guide with generated clip and request code](https://runware.ai/docs/models/bfl-flux-3-video/guides/multi-shot-sequences)
- **Model attribution:** Runware identifies the page as Black Forest Labs’ FLUX 3 Video and the exact generation request uses model ID `bfl:flux@3-video`.
- **Summary:** A 15-second coffee-brand spot makes two real hard cuts—from roasting beans, to a Chemex pour, to an overhead finished cup—while a warm indie-folk guitar bed persists across all three shots and the diegetic ambience changes with each scene.
- **Workflow/details:** Single `videoInference` call; 15 seconds; 1440×608; three shots defined entirely inside `positivePrompt` with `HARD CUT` tokens; one continuous music bed plus shot-specific ambient sound. No external clip stitching is used for the demonstrated sequence.
- **Prompt provenance:** `verbatim_in_post` — “A 15-second boutique coffee brand spot with three real cuts. SHOT ONE: extreme close-up of dark specialty coffee beans cascading…” The complete prompt remains visible in the source.
- **Why included:** First-party generated-video evidence with exact model ID, dimensions, duration, shot grammar, and prompt; it is a strong production benchmark for native multi-shot editing, visual contrast between setups, audio continuity, and commercial pacing within one generation.

### 115. Synchronized living-room robot-vacuum comedy from two natural cameras — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** Date not exposed; verified 2026-08-16
- **Original source profile:** [Umesh on X](https://x.com/umesh_ai) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror directly preserving Umesh’s original FLUX 3 wording, full prompt, attached-video context, and engagement](https://mobile.twstalker.com/umesh_ai)
- **Model attribution:** Umesh explicitly introduces the attached generation with “Prompt on Flux 3”.
- **Summary:** A harmless living-room comedy is shown simultaneously from a wide corner view and a closer opposite-side camera as a person sits with popcorn, accidentally activates a robot vacuum, lifts their feet, watches the vacuum push a slipper, and reacts while a curious cat follows the moving object and jumps onto the sofa.
- **Workflow/details:** Two synchronized natural-camera views rather than CCTV styling. The prompt fixes the left camera wide enough to preserve the room layout and the right camera close enough for facial expressions and props, anchors the triggering action at the 2-second mark, and requires identical person, cat, vacuum, popcorn, slipper, furniture, movement, lighting, and reactions across both perspectives. Cameras stay steady with realistic home-video quality, warm indoor light, natural movement, no cuts, and no dramatic effects.
- **Prompt provenance:** `verbatim_in_post` — “Two-shot split-screen showing the same harmless, funny incident in a cozy house living room. Both shots happen at the same time from different perspectives, like two cameras recording the scene naturally. Do not use CCTV styling, timestamps, security overlays, or distorted footage.” The complete prompt remains visible in the verification source.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, an attached video, the full reproducible prompt, and meaningful early engagement (roughly 3K views and 58 likes in the preserved snapshot). Technically, it is a strong same-event consistency benchmark because two visually different but synchronized cameras must preserve identity, object positions, small prop motion, human reaction timing, animal behavior, and causal sequencing without relying on CCTV artifacts.

### 116. Official FLUX 3 Video general-availability showcase — Black Forest Labs

- **Creator:** [Black Forest Labs (@bfl_ai)](https://x.com/bfl_ai)
- **Published:** Date not exposed; verified 2026-08-17
- **Original source:** [Black Forest Labs official LinkedIn page](https://de.linkedin.com/company/bflai)
- **Model attribution:** Black Forest Labs explicitly announces “FLUX 3 Video is here” in the official public-launch showcase; a BFL team member independently describes the release as general availability.
- **Summary:** The first-party launch reel spans documentary realism, animation, product film, typography, and dialogue scenes, emphasizing accurate motion, sound, and interaction across a broad range of production styles.
- **Workflow/details:** Officially supports text-to-video, image-to-video with multiple keyframes, video continuation, and native audio with lip-sync, effects, and ambience. Outputs run up to 20 seconds at native 1080p. Draft mode generates a fast lower-cost preview; an approved draft can be sent back for a full-quality render of the same video. The model is available through the API and partner tools; 2K, 4K, and open weights are announced as upcoming.
- **Prompt provenance:** `not_provided` — the general-availability showcase does not expose clip-level generation prompts, so none are inferred from the reel.
- **Why included:** Definitive first-party release video from the model maker, newly published after the early-access phase, with broad stylistic coverage, concrete production settings and workflow details, and a strong public quality signal.

### 117. 1990s “Override” hacker-gameshow benchmark vs. MiniMax H3 and Seedance 2.5 — Georg Neumann

- **Creator:** Georg Neumann
- **Published:** Date not exposed; verified 2026-08-17 (the public LinkedIn page shows a relative one-week timestamp).
- **Original source:** [Georg Neumann’s public LinkedIn post with the attached three-model comparison video](https://de.linkedin.com/posts/georg-neumann_flux-3-minimax-h3-und-seedance-25-in-einer-activity-7490640245982494720-SCv6)
- **Model attribution:** Neumann explicitly says the attached video compares FLUX 3, MiniMax H3, and Seedance 2.5, and states that the FLUX 3 version was generated through the Black Forest Labs Playground.
- **Summary:** A retro 1990s hacker gameshow concept called “Override,” inspired by the film *Hackers*, is rendered across three current video models, with a German-speaking host and period-style television presentation providing a practical side-by-side benchmark.
- **Workflow/details:** FLUX 3 was generated through the Black Forest Labs Playground; Seedance 2.5 through CapCut/Dreamina; and MiniMax H3 locally on an RTX 6000 Ada with 48 GB VRAM, where Neumann reports roughly 96 minutes for the H3 render. The public page includes a transcript of the German host dialogue. No verified FLUX 3 duration, resolution, seed, reference inputs, or post-production settings are disclosed.
- **Prompt provenance:** `not_provided` — the creator explains the “Override” concept and the model-specific generation paths, but does not publish the exact FLUX 3 generation prompt, so none has been reconstructed or inferred.
- **Why included:** Primary creator source with an attached comparison video, explicit FLUX 3 attribution, concrete generation-tool details, and a high-signal cross-model test of German speech, retro broadcast styling, presenter performance, and audiovisual coherence. It is especially useful because the same creative concept is shown across three newly released systems rather than as an isolated showcase clip.

### 118. Same-prompt K-pop comeback teaser with render telemetry — Photogenic Weekend

- **Creator:** [Photogenic Weekend (@PhotogenicWeekE)](https://x.com/PhotogenicWeekE)
- **Published:** Date not exposed; verified 2026-08-18 (the public verification mirror shows a relative four-hour timestamp).
- **Original source profile:** [Photogenic Weekend on X](https://x.com/PhotogenicWeekE) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, quoted source prompt, FLUX 3 render metadata, attached-result context, and engagement](https://twstalker.com/PhotogenicWeekE)
- **Model attribution:** Photogenic Weekend explicitly says FLUX.3 access had become available, that the quoted prompt was entered unchanged, and reports the render metadata as `modelFLUX 3`.
- **Summary:** A high-budget K-pop girl-group comeback-teaser brief originally used for a MiniMax H3 example is rerun unchanged through FLUX 3, creating a direct same-prompt benchmark centered on a seven-member adult Korean idol group with distinct identities and a polished music-video presentation.
- **Workflow/details:** FLUX 3 text-to-video; 1280×704; 15-second output; creator-reported cost approximately $2.72 USD and latency 287.88 seconds. The creator explicitly says the quoted prompt was used as-is, making the result a controlled prompt-transfer comparison rather than a separately rewritten FLUX-specific brief. The quoted source prompt targets 16:9, 2K and seven original Korean adult female idols with distinct faces, hairstyles, and outfits; the actual FLUX render metadata shown by the creator is 1280×704.
- **Prompt provenance:** `verbatim_in_post` — the creator quotes the prompt being reused unchanged. Verified visible excerpt: “Create a 15-second, 16:9, 2K, high-budget K-pop girl-group comeback teaser. The group consists of seven original Korean female idols, all aged 22 or older. They must not resemble any real celebrities. Give each member a distinct face, hairstyle, outfit, and …” The public mirror truncates the remainder, so no missing text has been reconstructed or inferred.
- **Why included:** Fresh original-creator FLUX 3 attribution with attached-result context, unusually concrete runtime/cost/resolution metadata, a visible prompt excerpt, and a clean unchanged-prompt cross-model methodology. It is a useful production benchmark for multi-character identity separation, polished music-video staging, and how FLUX 3 interprets a prompt authored for another current video model.

### 119. Arabic-dialect AI rant from a minimal prompt — MrDejie

- **Creator:** [MrDejie (@mrdejie)](https://x.com/mrdejie)
- **Published:** Date not exposed; verified 2026-08-18 (the public verification mirror shows a relative four-day timestamp).
- **Original source profile:** [MrDejie on X](https://x.com/mrdejie) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original MrDejie post, exact prompt, attached-video context, and engagement](https://mobile.twstalker.com/Abdullah4AI)
- **Model attribution:** MrDejie explicitly introduces the attached result with “Look what Flux 3 made.”
- **Summary:** An older man delivers an improvised rant about AI in an Arabic dialect, turning an extremely short scene brief into a spoken performance with facial motion, dialectal speech, and native audiovisual timing.
- **Workflow/details:** FLUX 3 text-to-video from a minimal natural-language prompt. The verified source does not disclose duration, resolution, seed, reference media, audio parameters, or post-production.
- **Prompt provenance:** `verbatim_in_post` — “an old man ranting about AI in Arabic dialect”
- **Why included:** Fresh traceable original-creator attribution with an attached video, exact reproducible prompt, and strong public engagement in the preserved snapshot (about 20K views and 63 likes). Technically, it is a compact multilingual stress test of dialect delivery, semantic improvisation, facial performance, lip synchronization, and coherent native audio from almost no direction.

### 120. Late-1990s public-TV computer-show benchmark vs. Seedance 2.0 — MAXFUSION.AI

- **Creator:** [MAXFUSION.AI / u/mementomori2344323](https://www.reddit.com/user/mementomori2344323/)
- **Published:** 2026-08-18 (based on the original Reddit posts’ relative four-hour timestamps)
- **Original sources:** [FLUX 3 vs SEEDANCE 2.0](https://www.reddit.com/r/FluxAI/comments/1vanc9z/flux_3_vs_seedance_20/) · [Same-prompt companion thread with the full prompt](https://www.reddit.com/r/Seedance_AI/comments/1vana5s/seedance_20_vs_flux_3_head_to_head_comparison_on/)
- **Model attribution:** The creator explicitly titles the primary post “FLUX 3 vs SEEDANCE 2.0,” states that both models received the exact same prompt, and separately confirms that no extra instructions were given.
- **Summary:** A faux late-1990s public-television computer show has a host type a request to plan his daughter’s wedding into a beige CRT chat interface while a skeptical co-host watches; the sequence cuts to the screen and back as the software generates a wedding checklist and the hosts deliver dry period-TV dialogue.
- **Workflow/details:** Controlled FLUX 3 vs. Seedance 2.0 comparison using the same prompt with no extra instructions. The visible brief is time-coded from 0–20 seconds, uses two locked-off cameras, standard-definition late-1990s television styling, scripted dialogue, CRT/keyboard room tone with no music, and an attached reference image of a Claude square-icon logo. The creator reports FLUX 3 as stronger in this test for native audio, 1990s/2000s film grading, in-video text rendering, and temporal scene consistency.
- **Prompt provenance:** `verbatim_in_post` — full prompt remains visibly published in the companion creator thread.
- **Why included:** Newly published primary creator posts with attached comparison media, explicit FLUX 3 attribution, an exact full prompt, same-prompt/no-extra-instructions methodology, a disclosed reference image, and unusually concrete creator evaluation of audio, period grading, temporal consistency, and text rendering. It is a strong reproducible benchmark for retro-video semantics, generated dialogue, screen text, shot transitions, timing, and native audio rather than a generic aesthetic showcase.

### 121. Real-story color-grading realism test — MAXFUSION.AI

- **Creator:** [MAXFUSION.AI / u/mementomori2344323](https://www.reddit.com/user/mementomori2344323/)
- **Published:** 2026-08-18
- **Original source:** [FLUX 3 color grading and realism is superior to any other model in this style](https://www.reddit.com/r/FluxAI/comments/1vg1dk0/flux_3_color_grading_and_realism_is_superior_to/)
- **Model attribution:** The original creator explicitly titles the attached-media post “FLUX 3 color grading and realism is superior to any other model in this style,” and the post carries the `FLUX 3` flair.
- **Summary:** A realism-focused FLUX 3 video is presented specifically as a color-grading and photorealism benchmark rather than a stylized effects showcase; one early viewer says they initially mistook it for a real story.
- **Workflow/details:** The creator says current FLUX 3 inference is still fairly slow, notes that 1080p is already live, and says 2K and 4K are forthcoming. The public post does not establish that this particular clip was rendered at 1080p and does not disclose its exact prompt, duration, input mode, reference media, seed, audio settings, or post-production.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the original creator post, and nothing has been inferred from the footage.
- **Why included:** Fresh primary creator post with attached media, explicit FLUX 3 attribution, a focused real-world realism/color-grading target, and a strong qualitative quality signal from an early commenter who believed the synthetic clip was a real story.

### 122. Japanese text-and-audio text-to-video test — 聖星あい

- **Creator:** [聖星あい＠AI愛好家 (@seisei_ai_1st)](https://x.com/seisei_ai_1st)
- **Published:** 2026-08-18 (the secondary verification source showed “about 10 hours ago” at verification)
- **Original source profile:** [聖星あい on X](https://x.com/seisei_ai_1st) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, explicit `#FLUX3` attribution, attached tweet video, follow-up evaluation, and engagement](https://www.sotwe.com/seisei_ai_1st)
- **Model attribution:** The creator explicitly describes the attached output as text-to-video and tags it `#FLUX3`.
- **Summary:** A Japanese-language text-to-video test focuses on FLUX 3’s ability to generate clean Japanese text together with spoken Japanese audio and caption-like on-screen typography.
- **Workflow/details:** Text-to-video. In creator follow-ups, 聖星あい says the Japanese audio and on-screen captions may be among the best of recent video models and specifically reports fewer Japanese-caption failures than the Seedance family. The creator also notes that the music only pays homage to the original because the original music is rights-protected. No verified duration, resolution, seed, reference media, exact prompt, or post-production settings are publicly exposed.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified public source, and nothing has been reconstructed from the video.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, an attached tweet video, roughly 4K views and 65 likes in the preserved snapshot, and a high-signal multilingual benchmark centered on Japanese speech plus in-video text rendering—an area the creator directly compares favorably against Seedance.

### 123. RIFTFALL retro-FPS cinematic trailer — VORTEX

- **Creator:** [VORTEX: AI Bros & AI Arena (@VORTEX_Promos)](https://x.com/VORTEX_Promos)
- **Published:** 2026-08-16
- **Original source profile:** [VORTEX on X](https://x.com/VORTEX_Promos) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, explicit FLUX 3 attribution, attached-video context, and engagement](https://twstalker.com/VORTEX_Promos)
- **Model attribution:** The creator explicitly says, “I made this Riftfall trailer with it,” immediately after identifying the model as FLUX 3 Video.
- **Summary:** A cinematic trailer for the creator’s retro FPS project RIFTFALL, used as a production-style test of FLUX 3’s game-trailer aesthetics and shot-to-shot cinematic presentation.
- **Workflow/details:** The creator identifies the trailer as made with FLUX 3 and, in the same post, describes FLUX 3’s general capabilities. The verified source does not establish this trailer’s exact duration, resolution, input mode, reference assets, seed, audio configuration, shot-generation count, or post-production workflow, so those details are not inferred.
- **Prompt provenance:** `not_provided` — no exact generation prompt or shot brief is visible in the verified public source, and nothing has been reconstructed from the footage.
- **Why included:** Fresh traceable original-creator attribution, an attached trailer, roughly 60K views and 248 likes in the preserved snapshot, and a strong production-oriented test of cinematic game-trailer staging, pacing, action, and visual coherence rather than a generic single-shot demo.

### 124. Four-minute “WINGED” mythic short film — Tony Simons

- **Creator:** [Tony Simons (@tonysimons_)](https://x.com/tonysimons_)
- **Published:** 2026-08-18
- **Original source profile:** [Tony Simons on X](https://x.com/tonysimons_) — the accessible public index did not expose a stable direct status URL.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, FLUX 3 attribution, contest context, attached-film post, and engagement](https://w.twstalker.com/tonysimons_)
- **Model attribution:** Simons explicitly calls WINGED “a mythic short film built end-to-end with @NousResearch Hermes and @bfl_ai FLUX 3” and identifies it as his FLUX 3 Short Film Contest entry.
- **Summary:** A four-minute mythic short in which the sun is dying, Night has stolen Zeus’s final decree, and Hermes has one chance to deliver a message that can only be spoken once.
- **Workflow/details:** End-to-end film workflow using Nous Research’s Hermes Agent with FLUX 3; the creator explicitly states the finished piece is four minutes long. The public source does not expose the exact prompt, number or duration of generated shots, resolution, seeds, reference assets, audio settings, or any manual-versus-agent editing breakdown, so those details are left unclaimed.
- **Prompt provenance:** `not_provided` — the story synopsis is visible, but it is not labeled as the exact generation prompt and has not been treated as one.
- **Why included:** Fresh original-creator attribution and a rare multi-minute narrative use of FLUX 3, making it an unusually ambitious production-scale test of end-to-end shot orchestration, continuity, and story pacing beyond a single benchmark clip.

### 125. Twenty-second character-and-voice continuity test — Heather Cooper

- **Creator:** [Heather Cooper (@HBCoop_)](https://x.com/HBCoop_)
- **Published:** Date not exposed; verified 2026-08-19 (the public verification index labels the video “6 days ago”).
- **Original source profile:** [Heather Cooper on X](https://x.com/HBCoop_) — the accessible public index does not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-channel mirror preserving Cooper’s attribution, attached 0:20 video listing, caption, and view count](https://www.24vids.com/channel/hbcoop_)
- **Model attribution:** Cooper’s preserved creator caption explicitly says, “FLUX 3 is really good at maintaining characters and voices throughout a 20-second video.”
- **Summary:** A full-length 20-second FLUX 3 continuity test focused on keeping character identity and voices stable across the entire generated clip rather than only across a short dialogue beat.
- **Workflow/details:** Verified duration is 20 seconds. The public verification source does not expose resolution, input/reference mode, seed, generation count, audio parameters, or post-production, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — the creator caption says “Prompt below,” but the publicly indexed verification source does not expose the prompt text; no missing wording has been reconstructed or inferred.
- **Why included:** Fresh explicit creator-side FLUX 3 attribution, an attached 20-second video, and a strong public quality signal (about 35.8K views in the preserved index). It is a useful long-horizon stress test of identity and voice persistence across FLUX 3’s full 20-second window.

### 126. Accidental 1980s Handycam realism from an aspect-ratio-mistake prompt — Diego Jr

- **Creator:** [Diego Jr (@CallMeDiegoJr)](https://x.com/CallMeDiegoJr)
- **Published:** Date not reliably exposed; verified 2026-08-19.
- **Original source profile:** [Diego Jr on X](https://x.com/CallMeDiegoJr) — the accessible public indexes do not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving Diego Jr’s original wording, explicit Flux 3 attribution, attached-video context, and engagement](https://ww.twstalker.com/CallMeDiegoJr)
- **Model attribution:** The creator explicitly opens the post with “Still Flux 3” while discussing this specific video and its generation prompt.
- **Summary:** A live-action-looking generation whose image texture and wardrobe read to the creator like footage captured on a 1980s Handycam, making the clip a strong test of period-specific consumer-video realism rather than polished modern cinematography.
- **Workflow/details:** Diego Jr says he forgot to correctly account for the intended 16:9 or 9:16 aspect ratio in the prompt and that the very first output from that flawed prompt unexpectedly became the best generation. The verified source does not expose the exact prompt, duration, resolution, seed, reference assets, audio settings, or post-processing, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — the creator explicitly discusses the prompt and its aspect-ratio mistake, but the exact prompt text is not visible in the verified public source and has not been reconstructed.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution preserved by a public secondary mirror, attached-video context, a strong public quality signal (roughly 103K views and 411 likes in one preserved snapshot), convincing accidental period-video texture, and an unusually useful candid note about a flawed prompt outperforming the intended setup.

### 127. Twenty-second office mockumentary with readable prop text and timed dialogue — Brent Lynch

- **Creator:** [Brent Lynch (@BrentLynch)](https://x.com/BrentLynch)
- **Published:** Date not exposed; verified 2026-08-19 (the public creator-profile mirror shows a relative two-day timestamp).
- **Original source profile:** [Brent Lynch on X](https://x.com/BrentLynch) — the accessible public index does not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving Lynch’s original wording, explicit FLUX 3 attribution, complete visible prompt, attached-video context, and engagement](https://mobile.twstalker.com/BrentLynch)
- **Model attribution:** Lynch explicitly titles the attached generation “FLUX 3 20-Second Office Mockumentary Parody” while announcing that FLUX 3 is broadly available.
- **Summary:** An original workplace mockumentary uses four speaking characters, awkward documentary looks to camera, crash zooms, nested prop boxes labeled “FLUX 3” and “NOT THAT OFFICE,” and a final silent reaction beat to parody familiar office-comedy grammar without reproducing an existing cast.
- **Workflow/details:** One 20-second prompt divided into five timed beats: 0–5, 5–9, 9–14, 14–17, and 17–20 seconds. The brief specifies unfamiliar actors, handheld documentary camerawork, awkward crash zooms, fluorescent office lighting, restrained performances, precisely timed dialogue and pauses, readable prop labels, realistic office ambience, and no music or laugh track.
- **Prompt provenance:** `verbatim_in_post` — the complete prompt remains visible in the verification source.
- **Why included:** Fresh explicit creator-side FLUX 3 attribution with an attached 20-second video and a fully visible, highly reproducible prompt. It is a demanding combined test of multi-character dialogue assignment, lip-sync, timed comedic pacing, documentary camera grammar, readable in-scene typography, nested-object continuity, and native ambience across the full 20-second window.

### 128. Endless-room handheld sprint through surreal spaces — fofr

- **Creator:** [fofr (@fofrAI)](https://x.com/fofrAI)
- **Published:** Date not reliably exposed; verified 2026-08-19.
- **Original source profile:** [fofr on X](https://x.com/fofrAI) — the accessible public indexes do not expose a stable direct status URL for this video.
- **Verification sources:** [Secondary public thread preserving fofr’s original caption, explicit FLUX 3 attribution, prompt excerpt, video context, and engagement](https://w.twstalker.com/minchoi) · [Secondary creator-retweet mirror preserving the same original creator post and prompt](https://mobile.twstalker.com/Felirami)
- **Model attribution:** fofr explicitly captions the attached generation “I love how strange Flux 3 makes this.”
- **Summary:** An amateur-handheld POV sprints continuously through an apparently endless succession of radically different, surreal rooms without stopping, using rapid spatial change rather than conventional cuts as the central effect.
- **Workflow/details:** Prompt-led text-to-video from one compact instruction emphasizing amateur handheld capture, continuous forward sprinting, nonstop motion, and a new strange room after room. Duration, resolution, seed, reference media, audio settings, and post-production are not disclosed in the verified public sources.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “an amateur handheld recording of a sprint through room after room after room, non stop, never ending rooms are all completely different to each other”. The complete one-line prompt remains visible in the verification sources.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, a visible reproducible prompt, and a strong public quality signal: preserved mirrors show roughly 90K–116K views and around one thousand likes. The concept is also a demanding long-horizon test of continuous camera motion, scene-to-scene spatial transformation, novelty, and temporal coherence without relying on a detailed shot list.

### 129. Agentic children’s-book-to-animation test workflow — Georg Neumann

- **Creator:** [Georg Neumann](https://de.linkedin.com/in/georg-neumann)
- **Published:** Date not exposed; verified 2026-08-19.
- **Original source:** [Georg Neumann’s public LinkedIn post with the attached FLUX 3 test generations](https://de.linkedin.com/posts/georg-neumann_ich-mach-einen-animationsfilm-aus-kinderbuch-activity-7490330694716571648-PZhq)
- **Model attribution:** Neumann explicitly closes the post with “Videos generiert mit FLUX 3” while describing the attached first test generations.
- **Summary:** Early animated-film tests adapt the creator’s daughter’s children’s book into moving scenes with spoken-character audio, while the post documents the upstream planning and reference pipeline used to turn the book into a full shot plan.
- **Workflow/details:** Claude Cowork is given the book folder containing PDFs and images, then briefed to turn the existing story into a film and supporting shot list rather than merely animate each spread. Through MCP, Claude accesses a Magnific project containing the book spreads, references, and character sheets and generates supporting images. Neumann reports ending with a complete film concept and storyboard in an Excel sheet, prompts included, plus 27 reference images that he only had to curate and refine; the next production step is iterating all 27 video clips, with voice consistency called out as a forthcoming challenge.
- **Prompt provenance:** `mentioned_not_in_post` — the creator says the storyboard contains prompts, but the exact FLUX 3 clip prompts are not publicly visible in the verified post, so none have been reconstructed or inferred.
- **Why included:** Primary creator source with attached video and transcript, explicit FLUX 3 attribution, and one of the most concrete end-to-end production workflows surfaced in this collection: agentic story breakdown, multimodal source ingestion, MCP-based reference generation, character assets, a 27-shot plan, human curation, and planned voice-continuity work.

### 130. Rain-soaked 1980s ninja trailer with dialogue-to-title transition — Brent Lynch

- **Creator:** [Brent Lynch (@BrentLynch)](https://x.com/BrentLynch)
- **Published:** 2026-08-16 (based on the secondary verification source’s relative three-day timestamp at verification).
- **Original source profile:** [Brent Lynch on X](https://x.com/BrentLynch) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving Lynch’s original creator wording, explicit FLUX 3 attribution, complete visible prompt, attached-video context, and engagement](https://mobile.twstalker.com/BrentLynch)
- **Model attribution:** Lynch explicitly opens the attached generation with “FINALLY! ⚔️ I GOT FLUX 3! TIME FOR NINJAS!” and tags Black Forest Labs in the published prompt.
- **Summary:** A rain-soaked rooftop confrontation between a ninja and a woman plays like a restrained early-1980s thriller, then turns a lightning white-out into an in-generation transition to a fictional theatrical title card, “NIGHT OF THE AI DROPS,” followed by a coming-soon tagline.
- **Workflow/details:** One long prompt coordinates two-character dialogue, held eye lines and restrained acting, a slow push-in with anamorphic over-the-shoulder framing, rain and traffic ambience, synth underscore, thunder, a lightning-driven transition, analog film texture, trailer-announcer voiceover, and readable title/tagline typography.
- **Prompt provenance:** `verbatim_in_post` — visible prompt begins: “A cold, controlled confrontation between two rivals on a rain-soaked rooftop at night shot with the discipline of a 1980's thriller: clean geometric framing, wide nocturnal cityscapes bleeding blue and amber through the rain…” The complete prompt remains publicly visible in the verification source.
- **Why included:** Traceable original-creator FLUX 3 attribution, attached-video context, roughly 3K views and 56 likes in the preserved snapshot, and an unusually detailed audiovisual brief. It stress-tests multi-speaker dialogue, understated performance, weather and lighting continuity, native sound design, a motivated scene-to-title transition, and generated typography in one cohesive cinematic sequence.

### 131. Fifteen-second kinetic-typography path-writing motion-design test — LudovicCreator

- **Creator:** [LudovicCreator (@LudovicCreator)](https://x.com/LudovicCreator)
- **Published:** 2026-08-19 (the public verification index showed “10 hours ago” at verification).
- **Original source profile:** [LudovicCreator on X](https://x.com/LudovicCreator) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving the original creator wording, explicit FLUX 3 attribution, attached-video context, Pixio AI workflow note, and full prompt comment](https://w.twstalker.com/LudovicCreator)
- **Model attribution:** The creator explicitly captions the attached piece “🎨 FLUX 3 🎨 Testing Motion design with Flux 3” and says it was made in Pixio AI.
- **Summary:** A vertical motivational motion-design piece turns a warm luminous line into both a walking path and a writing stroke, progressively revealing a three-line quote as the palette moves from near-dark midnight blue toward a calmer dawn-like blue and the composition builds from hesitation to momentum.
- **Workflow/details:** 15 seconds at 9:16. The visible prompt specifies five timed stages, exact final line breaks, handwritten-to-serif text resolution, a golden path/writing stroke, subtle paper texture and particles, restrained glow, parallax, one very slow camera push, controlled scale emphasis on “path,” gold emphasis on “courage,” a static final hold, and explicit spelling/readability/stability constraints. It also directs original minimal sound design with piano, ambient pad, pen texture, footstep-like ticks, shimmer accents, and a resolving chord.
- **Prompt provenance:** `verbatim_in_post` — the visible prompt begins: “Create a 15-second, 9:16 premium cinematic kinetic-typography film built around the exact quote:” and then supplies the exact sentence to be animated. The complete time-coded prompt remains visible in the creator’s first-comment post preserved by the verification source.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, attached-video context, a complete reproducible prompt, and a less-common motion-design benchmark rather than another generic realism clip. It tests legible animated typography, controlled graphic motion, temporal text stability, layout, palette progression, camera/parallax behavior, and synchronized sound cues across a full 15-second design sequence.

### 132. Twenty-second Monaco selfie-vlog benchmark vs. Seedance 2.5 — John

- **Creator:** [John (@johnAGI168)](https://x.com/johnAGI168)
- **Published:** 2026-08-19 (based on the secondary verification mirror’s relative one-hour timestamp at verification).
- **Original source profile:** [John on X](https://x.com/johnAGI168) — the accessible public index did not expose a stable direct status URL for this comparison video.
- **Verification source:** [Secondary creator-profile mirror preserving John’s original wording, explicit FLUX 3 vs. Seedance 2.5 attribution, visible prompt, attached-comparison context, and engagement](https://twstalker.com/johnAGI168)
- **Model attribution:** John explicitly captions the post “Flux 3 🆚 Seedance 2.5 📺 Who is better ❓ prompt 👇” before publishing the generation brief.
- **Summary:** A photorealistic vertical influencer-style selfie vlog follows the same young woman from a Monaco penthouse terrace to a private marina and then onto a moving yacht, using deliberately imperfect front-facing-phone capture and casual spoken performance rather than polished commercial cinematography.
- **Workflow/details:** The visible prompt specifies 20 seconds, 9:16, synchronized native audio, one consistent face/hair/outfit/voice, arm’s-length front-facing smartphone capture, slight hand shake, imperfect framing, brief autofocus/exposure changes, wind interaction, and three timed beats. It directs a palm-cover transition from the penthouse to the marina, a later whip-pan to the moving yacht, exact English dialogue with lip-sync, coastal ambience plus a soft house beat, and negative constraints excluding subtitles, logos, third-person/drone shots, beauty filtering, plastic skin, hand distortion, outfit changes, and face changes. The comparison post publishes one detailed prompt but does not expose model-specific generation settings or explicitly document any hidden per-model modifications.
- **Prompt provenance:** `verbatim_in_post` — “Create a photorealistic 20-second, 9:16 Instagram Reels-style selfie vlog with synchronized native audio.” The complete time-coded prompt remains visible in the verification source; no wording has been reconstructed from the footage.
- **Why included:** Newly published explicit original-creator FLUX 3 attribution, attached comparison context, a complete highly reproducible prompt, and a strong practical stress test of UGC realism, long-horizon identity and voice consistency, multi-location transitions, phone-camera imperfections, native ambience, exact dialogue, and lip-sync across a full 20-second vertical clip.

### 133. Five-language Charles de Gaulle transfer-desk dialogue test — Koh Terai

- **Creator:** [Koh Terai (@koh_terai)](https://x.com/koh_terai)
- **Published:** 2026-08-14 (based on the public verification mirror’s relative six-day timestamp at verification).
- **Original source profile:** [Koh Terai on X](https://x.com/koh_terai) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving Terai’s original wording, explicit FLUX.3 attribution, complete visible prompt, and video context](https://site.twstalker.com/koh_terai)
- **Model attribution:** Terai explicitly says, “I tried getting FLUX.3 to speak 5 languages in one video,” before publishing the exact prompt.
- **Summary:** A crowded airline transfer desk at Charles de Gaulle handles a cancellation through French, Arabic, English, Portuguese, and Russian dialogue, ending on a narrative turn where the agent prioritizes a silent passenger with a printed order of service over the growing queue.
- **Workflow/details:** One visible natural-language FLUX.3 prompt coordinates a single location, one agent, a growing line, six speaking turns across five languages, departure-board and luggage continuity, fluorescent airport lighting, and a final story beat driven by the last passenger’s document and the agent’s phone call. The verified source does not disclose duration, resolution, seed, reference media, or post-production.
- **Prompt provenance:** `verbatim_in_post` — the complete multilingual prompt remains visible in the verification source.
- **Why included:** Fresh original-creator FLUX.3 attribution and an unusually reproducible multilingual performance test. The prompt demands speaker assignment, five-language speech, turn-taking, facial and queue continuity, semantic context across languages, prop/story-state persistence, and a coherent dramatic payoff rather than merely testing isolated lip-sync.

### 134. “Future Dance” CRT-glitch motion test — Ralph Edelman

- **Creator:** [Ralph Edelman (@Ralph_Edelman)](https://x.com/Ralph_Edelman)
- **Published:** Date not exposed; verified 2026-08-20 (the public verification mirror labels the creator post “4 days ago”).
- **Original source profile:** [Ralph Edelman on X](https://x.com/Ralph_Edelman) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary mirror on Leonardo.Ai’s public profile preserving Edelman’s original creator post, exact prompt, explicit Flux 3 Video attribution, and engagement](https://twstalker.com/LeonardoAi)
- **Model attribution:** Edelman explicitly captions the work “Future Dance Created with @LeonardoAi using Flux 3 Video” before the prompt; Leonardo.Ai subsequently reshared the creator post.
- **Summary:** An energetic futuristic dancer moves while the camera smoothly zooms in and the background continuously changes color, with aggressive CRT breakup, RGB separation, chromatic aberration, datamoshing, pixel tearing, VHS tracking errors, and eventual signal-collapse styling layered through the motion.
- **Workflow/details:** Generated in Leonardo.Ai using Flux 3 Video. The visible prompt combines energetic human dance motion, a smooth zoom-in, continuous background color changes, and a dense stack of temporal glitch treatments. Duration, resolution, seed, reference inputs, audio direction, and post-production are not disclosed in the verified source.
- **Prompt provenance:** `verbatim_in_post` — full prompt remains visible in the verification source.
- **Why included:** Traceable original-creator attribution, an exact public prompt, and first-party platform amplification from Leonardo.Ai. It is a distinctive motion-design stress test because fast human movement, smooth camera motion, evolving color, and a large stack of unstable temporal glitch effects all need to remain intentionally readable rather than collapsing into uncontrolled artifacts.

### 135. Tearful close-up emotional-realism test — 𝐙𝐞𝐧𝐠

- **Creator:** [𝐙𝐞𝐧𝐠 💜 (@zeng_wt)](https://x.com/zeng_wt)
- **Published:** Date not exposed; verified 2026-08-20 (the public verification source labels the creator post “a week ago”).
- **Original source profile:** [𝐙𝐞𝐧𝐠 on X](https://x.com/zeng_wt) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary verification on Leonardo.Ai’s public profile preserving the original creator post, explicit FLUX 3 attribution, attached-video context, and Leonardo.Ai reshare](https://twstalker.com/LeonardoAi)
- **Model attribution:** Zeng explicitly says the emotional-realism video was generated with “FLUX 3” and “Created in @LeonardoAi”; Leonardo.Ai’s official account reshared the original creator post.
- **Summary:** A close-up performance centers on a visibly tearful character, using subtle facial emotion, wet-eye detail, and naturalistic skin rendering as a realism test rather than relying on spectacle or fast motion.
- **Workflow/details:** Generated in Leonardo.Ai using FLUX 3 Video. The verified public source does not expose duration, resolution, seed, reference inputs, audio direction, or post-production details.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified source, and none has been reconstructed from the footage.
- **Why included:** Traceable original-creator FLUX 3 attribution plus first-party platform amplification from Leonardo.Ai. The example targets a difficult failure mode for generated video — sustained, believable facial emotion with tears and photoreal close-up detail — and was singled out by the creator specifically for its emotional depth and realism.

### 136. Same-prompt luxury restaurant advertisement vs. MiniMax H3 — ContentStudio

- **Creator:** [ContentStudio](https://contentstudio.io/)
- **Published:** 2026-08-18 (based on the first-party LinkedIn page’s relative two-day timestamp at verification).
- **Original source:** [ContentStudio’s first-party LinkedIn page with the attached “Flux 3 vs MiniMax H3” comparison](https://www.linkedin.com/company/contentstudio/)
- **Model attribution:** ContentStudio explicitly labels the attached comparison “Flux 3 vs MiniMax H3” and states that both models received the exact same prompt.
- **Summary:** A 15-second premium restaurant commercial follows a chef preparing steak over open flame, then moves through slow-motion slicing, plating, and sauce-pouring close-ups before traveling through the kitchen to a final hero shot of the finished dish on an elegant table.
- **Workflow/details:** Controlled same-prompt comparison: ContentStudio states “No edits. No cherry picking.” and places both outputs side by side. The brief specifies 15 seconds, realistic food textures, cinematic lighting, natural hand movement, smooth camera transitions, slow-motion inserts, sparks, and premium commercial styling. No model-specific seed, resolution, reference media, or hidden generation parameters are disclosed.
- **Prompt provenance:** `verbatim_in_post` — the complete prompt remains visible in the first-party source.
- **Why included:** Fresh first-party platform source with attached comparison media, exact model attribution, a complete reproducible prompt, and a controlled no-edit same-prompt methodology. It is a useful production benchmark for food texture, flame and spark behavior, hand-object interaction, slicing and plating continuity, liquid sauce motion, camera travel, slow motion, and commercial-grade lighting without relying on a hand-picked bespoke prompt for each model.

### 137. Single-pass cinematic trailer with native synchronized audio — ContentStudio

- **Creator:** [ContentStudio](https://contentstudio.io/)
- **Published:** 2026-08-20 (the first-party LinkedIn page showed the post as approximately 15 hours old at verification).
- **Original source:** [ContentStudio’s first-party LinkedIn page with the attached “Flux 3 Trailer” video](https://www.linkedin.com/company/contentstudio/)
- **Model attribution:** ContentStudio explicitly states, “Flux 3 generated this trailer in a single pass,” and identifies FLUX 3 as the model used for both picture and audio.
- **Summary:** A polished trailer-style generation demonstrates cinematic staging while keeping action-linked sound synchronized inside the same render, including impacts, footsteps, facial performance, on-screen text, and animated typography.
- **Workflow/details:** ContentStudio states the trailer was generated in one pass with native audio and no separate scoring step. The post highlights up to 20-second outputs, synchronized action-driven sound, human-readable facial expressions, a style range from candid camcorder footage to full cinematics, and accurate in-scene text/animated typography. The exact duration, resolution, seed, reference media, prompt, and post-production settings for this specific trailer are not disclosed.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified first-party source, and none has been reconstructed from the footage.
- **Why included:** Newly published first-party attached-video example with explicit FLUX 3 attribution and a production-oriented single-pass claim. It is a useful quality benchmark because trailer pacing has to coordinate cinematic motion, facial performance, readable typography, impact timing, footsteps, and native sound without a separate audio pass.

### 138. Lissy PONY branded-series teaser with consistent characters and custom voices — Blue Ocean Entertainment / Burda Media

- **Creator:** [Blue Ocean Entertainment AG](https://www.linkedin.com/company/blue-ocean-entertainment-ag/) / [Hubert Burda Media](https://www.linkedin.com/company/hubert-burda-media/)
- **Published:** 2026-08-20 (Blue Ocean Entertainment’s first-party LinkedIn page showed the teaser post as approximately 47 minutes old at verification).
- **Original source:** [Blue Ocean Entertainment AG’s first-party LinkedIn page with the official teaser](https://www.linkedin.com/company/blue-ocean-entertainment-ag/)
- **Supporting first-party source:** [Hubert Burda Media’s LinkedIn announcement](https://www.linkedin.com/company/hubert-burda-media/)
- **Model attribution:** Blue Ocean explicitly states that the series’ visual content is created with FLUX 3 from Black Forest Labs and tags `#FLUX3`; Burda Media separately identifies itself as an official FLUX 3 release partner and says the teaser demonstrates the model’s new video capabilities.
- **Summary:** The official teaser brings Blue Ocean’s established Lissy PONY children’s IP into animated video, centered on unicorn Tamani and her pony friends around the Crystal Academy, while preserving a recognizable branded visual world and character identity.
- **Workflow/details:** FLUX 3 is used for the visual video generation, while ElevenLabs supplies individual character voices. Blue Ocean says the project is designed to preserve the existing brand and characters as they move from print/comic media into video; the planned series will launch in autumn 2026 in German, French, Spanish, Polish, and English. Burda describes the broader workflow as combining visually consistent characters, recognizable voices, and AI-assisted synchronization for international scaling. Exact FLUX 3 duration, resolution, reference assets, generation settings, and post-production for the teaser are not disclosed.
- **Prompt provenance:** `not_provided` — neither first-party source exposes an exact FLUX 3 generation prompt, so none has been reconstructed or inferred from the teaser.
- **Why included:** Fresh first-party release-partner material with an official attached/embedded teaser and unambiguous FLUX 3 attribution. Unlike a one-off demo, it is a production-oriented test of adapting an existing commercial IP into repeatable video while maintaining character/world consistency, integrating distinct voices, and preparing multilingual distribution at series scale.

### 139. Six-minute 27-scene “BERKUTCHI” Altai world-consistency production — Christian Hartmann / CHAIPEAU™

- **Creator:** [Christian Hartmann](https://de.linkedin.com/in/chrtmn) / [CHAIPEAU™](https://www.chaipeau.com/)
- **Published:** Date not exposed; verified 2026-08-20.
- **Original source profile:** [Christian Hartmann on LinkedIn](https://de.linkedin.com/in/chrtmn) — the accessible public index did not expose a stable direct activity URL for this Altai post.
- **Verification source:** [Secondary LinkedIn profile directly embedding and quoting the original creator/project post](https://de.linkedin.com/in/luke-lewandowski-6742a9166)
- **Model attribution:** The creator says he is part of Black Forest Labs’ first FLUX Creator cohort and explicitly states that everything in this six-minute CHAIPEAU™ test production was generated with the FLUX 3 beta model.
- **Summary:** “BERKUTCHI » Eagle Hunter of the Altai” follows Kazakh golden-eagle hunters across winter landscapes as a six-minute, 27-scene production designed to test whether one written visual specification can keep a world coherent even when every scene is generated independently.
- **Workflow/details:** The creator wrote 28 scenes before generation, each specifying subject, camera package, runtime, audio, and negative prompt, then dropped one duplicate macro before rendering. Format was locked three ways—in the prompt body, the generation field, and negative instructions excluding wrong ratios—and palette-defining colors were written both as hex values and words. The final 27 scenes were generated in the official FLUX 3 Discord with native audio and native 16:9, then cut end to end with no crop and no grading rescue; the creator reports stable palette, haze, terrain, and light behavior across scenes that never saw one another.
- **Prompt provenance:** `mentioned_not_in_post` — the creator details the scene-specification method and says all 28 scenes were written in advance, but the accessible verified source does not expose a complete generation prompt, so none has been copied or reconstructed.
- **Why included:** A rare production-scale FLUX 3 stress test rather than a single clip: 27 independently generated scenes must preserve environmental language, palette, light, audio treatment, and native framing across six minutes. The post also publishes concrete failure-prevention lessons—especially ratio locking and duplicated color specification—making the workflow unusually reusable.

### 140. One-line Hyperframes explainer with agentic script, lip-sync, effects, and music — Yuval Avidani

- **Creator:** [Yuval Avidani](https://il.linkedin.com/in/yuval-avidani-87081474)
- **Published:** Date not exposed; verified 2026-08-20.
- **Original source profile:** [Yuval Avidani on LinkedIn](https://il.linkedin.com/in/yuval-avidani-87081474) — the public index did not expose a stable direct activity URL for this Hyperframes post.
- **Verification source:** [Secondary LinkedIn activity page preserving Yuval’s original creator wording, attached-video context, exact prompt, workflow description, and engagement](https://il.linkedin.com/in/aviranm)
- **Model attribution:** Yuval explicitly says the attached video was created with the new Flux 3 Video model.
- **Summary:** A short YouTube-commenter-style explainer about HeyGen’s Hyperframes is generated from a single terse brief and an attached portrait of the creator, with the system researching the topic, creating a script and expanded internal direction, combining animations, and producing a finished social-style explainer.
- **Workflow/details:** The creator reports a one-prompt, no-video-editing workflow. Starting inputs were the visible one-line prompt plus his attached image. He says FLUX 3 researched Hyperframes, wrote its own more detailed prompt and script, incorporated animations, and generated lip-sync, effects, and background music; he also notes support for portrait or landscape output. The internal expanded prompt and script are not exposed, so those details are not reconstructed.
- **Prompt provenance:** `verbatim_in_post` — “A YouTube commenter video explaining about HeyGen’s Hyperframes in 20 seconds.” This is the exact user-level prompt visibly published in the verified source; no hidden expanded prompt wording has been inferred.
- **Why included:** Explicit original-creator Flux 3 Video attribution, attached-video context, an exact highly reusable minimal prompt, and an unusually agentic end-to-end workflow. The example is especially useful for social/explainer production because it combines topic research, reference-image identity, script creation, animation, lip-sync, effects, music, and a finished no-edit result from a single short instruction.

### 141. Agentic 1980s WORM TV singularity-news channel — Fabian Stelzer / Glif

- **Creator:** [Fabian Stelzer (@fabianstelzer)](https://x.com/fabianstelzer) / [WORM TV (@wormtelevision)](https://x.com/wormtelevision)
- **Published:** 2026-08-16 (based on the secondary verification source’s relative five-day timestamp at verification).
- **Original source profiles:** [Fabian Stelzer on X](https://x.com/fabianstelzer) · [WORM TV on X](https://x.com/wormtelevision) — the accessible public index did not expose stable direct status URLs for the launch post and workflow follow-ups.
- **Verification source:** [Secondary public creator-profile mirror preserving Stelzer’s original explicit Flux3 attribution, the quoted WORM TV launch-post media context, workflow follow-ups, and engagement](https://zamantika.com/profile/fabianstelzer)
- **Model attribution:** Stelzer explicitly describes WORM TV as an “autonomous interdimensional Flux3 powered 80s news channel covering the singularity.”
- **Summary:** A recurring retro-1980s, intergalactic-news format turns current AI developments into an ongoing fictional broadcast world, with recurring reporters and street-interview segments rather than a standalone one-off clip. The preserved launch post covers topics including Anthropic watermarks and DeepSeek V4 Pro.
- **Workflow/details:** Stelzer says the channel is built inside the Glif harness from a defined world, characters, rules, and his creative taste. At verification it was not yet fully autonomous: he remained the creative director, sent ideas from his phone, let Glif execute, and manually selected what to publish. His stated direction is toward full self-driving media channels and an open-source harness/Glif-agent workflow for entertainment, brand, and marketing use.
- **Prompt provenance:** `not_provided` — no exact FLUX 3 generation prompt is visible in the verified source, so the channel concept and workflow notes are not presented as a prompt.
- **Why included:** Explicit creator-level Flux3 attribution, directly quoted WORM TV media context, strong public engagement (about 68.6K views and 571 likes in the preserved snapshot), and unusually reusable agentic-production notes. It demonstrates FLUX 3 as part of a persistent world/character system for recurring AI-native media rather than only a single generated clip.

### 142. Oil-painting style animation persistence test — NOBU

- **Creator:** [NOBU (@nbykos)](https://x.com/nbykos)
- **Published:** Date not reliably exposed; verified 2026-08-21 (public mirrors place the creator post roughly one to two days earlier).
- **Original source profile:** [NOBU on X](https://x.com/nbykos) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving NOBU’s original wording, explicit Flux 3 attribution, attached-video context, follow-up observations, and engagement](https://ww.twstalker.com/nbykos)
- **Model attribution:** NOBU explicitly captions the attached video “Flux 3 の期待度が上がってきた 油彩スタイルが動く,” directly identifying Flux 3 as the model behind the moving oil-painting-style result.
- **Summary:** A stylized animation preserves an oil-painting look through motion instead of collapsing back toward ordinary rendered frames, using persistent painterly texture as the core test.
- **Workflow/details:** In a follow-up, NOBU says that in his own test the model reproduced the oil-painting animation by effectively redrawing the whole frame uniformly. He also says he has been testing Flux 3 through Runway and fal generally, but the public source does not establish which platform produced this exact clip. Duration, resolution, seed, reference inputs, exact prompt, audio settings, and post-production are not publicly verified.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified public source. A viewer asks whether special prompting beyond ideas like maintaining the oil-painting look and low FPS was used, but NOBU’s exact prompt is not exposed, so none is reconstructed.
- **Why included:** Fresh explicit original-creator Flux 3 attribution, attached-video context, strong public engagement (roughly 13K–16K views across preserved snapshots), and a distinctive temporal-style-consistency benchmark. Maintaining an oil-painted surface coherently while the scene moves is a materially different challenge from generic cinematic realism and gives the collection a useful style-persistence example.

### 143. 21:9 coastal signal-station dialogue previs with measured render telemetry — Himanshu Goel / Segmind

- **Creator:** [Himanshu Goel](https://blog.segmind.com/author/himanshu/) / [Segmind](https://www.segmind.com/)
- **Published:** 2026-08-19
- **Original source:** [FLUX 3 Text to Video: Features, Real Costs and How It Compares](https://blog.segmind.com/flux-3-text-to-video-features-real-costs-and-how-it-compares/)
- **Model attribution:** Goel explicitly documents running the clip through Segmind’s `flux-3-text-to-video` endpoint and labels the embedded result “FLUX 3 output, film previs at 21:9 with a scripted line.”
- **Summary:** A cinematic anamorphic night scene places a lone radio operator in a rain-lashed coastal signal station, delivering a scripted line into a desk microphone while the camera slowly dollies in and native audio layers rain, electronics hum, and radio static.
- **Workflow/details:** Text-to-video at full-quality HD, 5 seconds, 21:9, `draft: false`, `generate_audio: true`. The returned file measured 1440×608 with an AAC audio track; Goel reports a 62-second render and a billed cost of $1.2155 for this run. The broader hands-on article also records the endpoint’s 5–20 second duration control, HD/FHD tiers, draft-preview workflow, and measured per-render costs.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Cinematic anamorphic wide shot: a lone radio operator in a rain-lashed coastal signal station at night, green CRT glow lighting her face from below”. The complete prompt, including dialogue, camera movement, ambience, and no-music instruction, remains visible in the original source.
- **Why included:** Newly published first-party hands-on test with an embedded FLUX 3 output, exact public prompt, precise generation parameters, real billed cost and render-time telemetry, plus a demanding combination of widescreen composition, controlled camera motion, intelligible scripted dialogue, lip-sync, weather, and layered native audio.

### 144. Fifteen-second cyber-grunge rap editorial performance — AI_poruru(world)

- **Creator:** [AI_poruru(world) (@poruru_ai)](https://x.com/poruru_ai)
- **Published:** 2026-08-12 (date preserved by Yahoo! Japan’s public X real-time index).
- **Original source profile:** [AI_poruru(world) on X](https://x.com/poruru_ai) — the accessible public indexes did not expose a stable direct status URL for the video/prompt thread.
- **Verification sources:** [Secondary creator-profile mirror preserving the original FLUX 3 prompt follow-up, parent-video context, and engagement](https://www.twstalker.com/poruru_ai) · [Yahoo! Japan real-time X index preserving the creator, exact date, and prompt excerpt](https://search.yahoo.co.jp/realtime/search?ei=UTF-8&p=second+video&save=5)
- **Model attribution:** The creator explicitly labels the prompt follow-up `FLUX 3:プロンプト` and, in the adjacent parent post, identifies the associated clip as FLUX 3 Video.
- **Summary:** A high-fashion dark-pop/rap performance is staged as a kinetic cyber-grunge editorial film, using scanned-magazine grain, halftone and distressed-print texture, red-black graphic energy, close facial performance, and five hard-cut movement beats rather than static beauty posing.
- **Workflow/details:** The visible brief specifies 15 seconds and five 3-second sections. It directs an extreme close-up push-in, a tight three-quarter tracking angle, a backward-dolly medium close-up, a mini-orbit close-up, and a final aggressive push-in, with continuous hair, shoulder, hand, facial, and body motion. The prompt also specifies two reference roles—one for performer identity/outfit and one for visual style—although the actual reference assets and model-side settings are not preserved in the public verification sources. An adjacent creator post describes the associated FLUX 3 test as 15 seconds at 720p.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “15-second cyber-grunge rap music video.” The full time-coded prompt remains visible in the secondary verification source; no missing text has been reconstructed.
- **Why included:** Explicit original-creator FLUX 3 attribution, a visible structured prompt, traceable video-thread context, and unusually reusable direction for high-motion performance video: identity/style references, hard-cut rhythm, close-up camera choreography, body momentum, hair physics, editorial surface treatment, and anti-static constraints are all specified in one compact 15-second plan.

### 145. Police-helicopter chase with a parkouring robot — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-08-13 (based on the public verification mirror’s preserved relative timestamp at crawl).
- **Original source profile:** [Christopher Fryant on X](https://x.com/cfryant) — the accessible public index did not expose a stable direct status URL for this post.
- **Verification source:** [Secondary public mirror preserving a retweet of Fryant’s original creator caption, explicit FLUX 3 attribution, attached-video context, and engagement](https://twstalker.com/ZachyAshworth)
- **Model attribution:** Fryant explicitly captions the attached work “Police helicopter chase with a parkouring robot. FLUX 3” and tags Black Forest Labs.
- **Summary:** A police-helicopter pursuit tracks a robot performing parkour, combining fast aerial chase language with agile articulated locomotion and urban action staging.
- **Workflow/details:** The creator explicitly says the prompt is in the original post, but the accessible verification mirror does not expose that prompt text. Duration, resolution, seed, reference assets, audio instructions, and post-production are therefore left unclaimed rather than inferred from the footage.
- **Prompt provenance:** `mentioned_not_in_post` — Fryant says “prompt in the post,” but the prompt itself is not visible in the verified public mirror, so no wording is copied or reconstructed.
- **Why included:** Traceable original-creator FLUX 3 attribution, attached-video context, and a strong public quality signal in the preserved snapshot (about 32K views and 247 likes). The concept is also a demanding action benchmark: sustained helicopter pursuit, rapid robot parkour, changing camera-to-subject geometry, urban spatial continuity, and physically readable articulated motion must remain coherent at speed.

### 146. Five-second rainy-Tokyo ramen-shop native-audio API example — Cloudflare Workers AI

- **Creator:** [Cloudflare Workers AI](https://developers.cloudflare.com/ai/) using Black Forest Labs’ FLUX 3 Video model.
- **Published:** Date not stated on the model page; Cloudflare’s models index was last updated 2026-08-12; verified 2026-08-21.
- **Original source:** [Cloudflare’s first-party FLUX 3 Video model documentation and runnable example](https://developers.cloudflare.com/ai/models/black-forest-labs/flux-3-video/)
- **Model attribution:** Cloudflare explicitly identifies the model as “FLUX 3 Video” with model ID `black-forest-labs/flux-3-video`, and the documented response directly links to the generated MP4.
- **Summary:** A cozy ramen shop on a rainy Tokyo night is rendered with visible broth steam while rain patter and quiet kitchen sounds are generated alongside the picture.
- **Workflow/details:** Text-to-video via Workers AI with `mode: "t2v"`, `resolution: "hd"`, `duration: 5`, and `generate_audio: true`. The documented response links directly to `https://examples.aig.cloudflare.com/black-forest-labs/flux-3-video/text-to-video.mp4`; Cloudflare documents generated MP4 output at 24 fps with audio by default. No seed, explicit aspect ratio, or post-production is stated for this example, so none is inferred.
- **Prompt provenance:** `verbatim_in_post` — “A cozy ramen shop on a rainy Tokyo night, steam rising from the broth. Rain patter and quiet kitchen sounds.”
- **Why included:** A first-party platform example with an actual linked FLUX 3 video, exact model identifier, complete visible prompt, and reproducible generation parameters. It is a compact native-audio benchmark tying a visually simple atmospheric scene to synchronized environmental sound without relying on inferred settings.

### 147. FLUX 3-powered 2K/4K super-resolution comparison — Black Forest Labs / Cyril Diagne

- **Creator:** [Black Forest Labs](https://bfl.ai/) / [Cyril Diagne](https://bfl.ai/blog/flux-video-upscale)
- **Published:** 2026-08-20
- **Original source:** [FLUX Video Upscale product page](https://bfl.ai/video-upscaler) · [Launch article](https://bfl.ai/blog/flux-video-upscale)
- **Model attribution:** Black Forest Labs explicitly describes FLUX Video Upscale as “FLUX 3 powered super-resolution” and says it is tuned for FLUX 3 output.
- **Summary:** First-party original-vs-upscaled video comparisons demonstrate FLUX 3-aware super-resolution that regenerates video at higher resolution while preserving motion and style and repairing details such as faces and natural textures.
- **Workflow/details:** Accepts 480p+ source video; 1.5×, 2×, or 3× upscale factors; Precise mode (`creativity: 0`) uses 4 steps at $0.07/MP/s, while Creative mode (`creativity: 1`) uses 8 steps at $0.10/MP/s and can add or repair more detail. Inputs can be up to 20 seconds / 50 MB; source audio is preserved; standard output is 24 fps; Creative mode can optionally be steered with a prompt.
- **Prompt provenance:** `not_provided` — the product documents optional prompt steering, but no exact prompt is published for the showcased comparison videos.
- **Why included:** A newly published first-party FLUX 3 video workflow with embedded comparison media and unusually reproducible controls for resolution, mode, steps, pricing, duration, audio, and optional prompt steering.

### 148. Ten-second carrier-deck three-shot launch with native audio — John Ozuysal / fal

- **Creator:** [John Ozuysal](https://fal.ai/learn/tools/how-to-use-flux-3) / [fal](https://fal.ai/)
- **Published:** 2026-08-12 (the first-party guide’s last-updated date; the clip’s original publication date is not separately stated).
- **Original source:** [fal’s first-party “How To Use FLUX 3: Prompts & Workflows” guide with the embedded generated video](https://fal.ai/learn/tools/how-to-use-flux-3)
- **Model attribution:** fal explicitly labels the embedded result “Generated using FLUX 3 on fal, an AI model from Black Forest Labs.”
- **Summary:** A golden-hour aircraft-carrier launch is covered like a real deck operation across three planned angles: long-lens taxi and catapult lock, a low deck-level launch, then a tilt-up holding the jet into a climbing turn.
- **Workflow/details:** Text-to-video; 10-second duration; timestep prompting at 0.0–3.5s, 3.5–7.0s, and 7.0–10.0s with explicit `HARD CUT` markers. The prompt coordinates long-lens heat haze, a low wide camera, tilt-up tracking, anamorphic flare, deck-crew action, and continuous turbine, catapult, wind, and radio audio. The guide supports 720p/1080p generally, but this clip’s exact resolution and aspect ratio are not separately stated, so none is inferred.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Golden hour on a carrier deck, cut like coverage of a real deck operation. Grainy anamorphic, hard raking sun, heavy flare across the lens.” The complete time-coded prompt remains visible in the first-party source.
- **Why included:** First-party embedded FLUX 3 output with explicit attribution, exact duration, visible prompt, timed cuts, camera choreography, physical action, and native-audio direction. It is a strong reproducible benchmark of multi-shot editorial grammar inside one generation.

### 149. Astronaut re-entry dialogue and lighting-change image-to-video — John Ozuysal / fal

- **Creator:** [John Ozuysal](https://fal.ai/learn/tools/how-to-use-flux-3) / [fal](https://fal.ai/)
- **Published:** 2026-08-12 (the first-party guide’s last-updated date; the clip’s original publication date is not separately stated).
- **Original source:** [fal’s first-party FLUX 3 workflow guide with source still, prompt, and embedded generated video](https://fal.ai/learn/tools/how-to-use-flux-3)
- **Model attribution:** fal explicitly labels the embedded result “Generated using FLUX 3 on fal, an AI model from Black Forest Labs.”
- **Summary:** A close spacecraft portrait animates from a still: the astronaut flips an overhead switch, addresses the lens, then re-entry begins as orange light fills the window and sweeps across her visor and instrument panel.
- **Workflow/details:** Image-to-video from one Seedream 5.0 source portrait. The prompt explicitly preserves the same face, white pressure suit, and switch banks, calls for a slight push-in, scripted dialogue, changing practical light, structural groan, hull buffeting, and a rising roar, with no music, on-screen text, or subtitles. The exact clip duration, resolution, seed, and post-production are not separately disclosed.
- **Prompt provenance:** `verbatim_in_post` — the visible spoken line is: “Tell them we made it to the far side.” The complete generation prompt remains visible in the first-party source.
- **Why included:** First-party source/output pairing with explicit FLUX 3 attribution and a highly reusable image-to-video pattern combining identity retention, precise human action, direct-to-camera speech, environmental state change, moving light, camera motion, and layered native sound.

### 150. 21:9 three-keyframe vault-heist interpolation — John Ozuysal / fal

- **Creator:** [John Ozuysal](https://fal.ai/learn/tools/how-to-use-flux-3) / [fal](https://fal.ai/)
- **Published:** 2026-08-12 (the first-party guide’s last-updated date; the clip’s original publication date is not separately stated).
- **Original source:** [fal’s first-party FLUX 3 workflow guide with all three keyframes, prompt, and embedded generated video](https://fal.ai/learn/tools/how-to-use-flux-3)
- **Model attribution:** fal explicitly labels the final video “Generated using FLUX 3 on fal, an AI model from Black Forest Labs.”
- **Summary:** A heist-film vault opening is storyboarded with three fixed compositions: hands on the brass dial in near darkness, the heavy door partway open with warm light spilling out, then a suited figure silhouetted in the fully open doorway.
- **Workflow/details:** Keyframes-to-video; 10 seconds; 21:9. Three keyframes are pinned at frames 0, 96, and 216; fal documents FLUX 3’s frame indexing at 24 fps, placing them at 0s, 4s, and 9s with one second of motion runway after the final composition. The source frames were created with Nano Banana 2 Lite and its edit mode. The video prompt specifies a locked-off low angle, one continuous move, dial/bolt/hinge sounds, and a final breath with no music.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “The final beat of a heist picture. The hands work the dial until the lock gives, the door swings out under its own weight”. The complete video prompt and all three source-frame prompts remain visible in the first-party guide.
- **Why included:** Exceptionally reproducible first-party example with embedded output, explicit FLUX 3 attribution, exact duration/aspect ratio, exact keyframe indices, source-frame provenance, and visible prompt. It demonstrates storyboard-like temporal control rather than relying on text prompting alone.

### 151. Sunday-morning UGC influencer realism with deliberate DV imperfections — Kaan

- **Creator:** [Kaan (@kaanakz)](https://x.com/kaanakz)
- **Published:** 2026-08-18
- **Original source profile:** [Kaan on X](https://x.com/kaanakz) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving Kaan’s original “Made with Flux 3” wording, complete visible prompt, video context, and engagement](https://w.twstalker.com/kaanakz)
- **Model attribution:** Kaan explicitly introduces the attached result with “Made with Flux 3.”
- **Summary:** A synthetic Sunday-morning lifestyle vlog follows one adult woman from bed through curtains, bathroom, coffee and breakfast, tidying, skincare, dressing, and a balcony finish while trying to retain the imperfect look and behavior of casual social footage instead of polished advertising.
- **Workflow/details:** Prompt-led FLUX 3 video built around a DV/16 mm-tape-inspired handheld language: selfie and first-person capture mixed with occasional fixed external cuts, realistic shake, crooked framing, autofocus delay, exposure variation, motion blur, subtle vintage tape texture, and soft morning lighting. The prompt scripts short dialogue beats and requires consistent identity, natural breathing/movement, home ambience, and continuity through several apartment spaces. Duration, resolution, seed, reference assets, and post-production are not publicly verified.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “CAMERA: DV 16mm tape camcorder handheld aesthetic. Gorgeous glamorous European woman films herself in selfie-cam and first-person style during a slow Sunday morning at home. Realistic hand shake, crooked framing, delayed autofocus, occasional motion blur.” The complete storyboard prompt remains visible in the verification source.
- **Why included:** Fresh explicit creator-side FLUX 3 attribution, a fully visible reproducible prompt, and a strong public quality signal (about 21K views and 217 likes in the preserved snapshot). It is a practical UGC-realism stress test of identity persistence, multi-room staging, imperfect consumer-camera behavior, natural dialogue, facial performance, and mundane action continuity.

### 152. Twenty-second orbital-hotel vacation POV with reflection-to-exposure transition — Jin.B

- **Creator:** [Jin.B (@opener_ai)](https://x.com/opener_ai)
- **Published:** 2026-08-19
- **Original source profile:** [Jin.B on X](https://x.com/opener_ai) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving Jin.B’s original Flux3 attribution, attached-video context, complete visible prompt, and engagement](https://mobile.twstalker.com/opener_ai)
- **Model attribution:** Jin.B explicitly says “Flux3 is amazing at making natural-looking videos,” calls out T2V, labels the following text `[FLUX 3 PROMPT]`, and tags `#flux3`.
- **Summary:** Amateur first-person phone footage moves through a private orbital-hotel cabin toward a huge observation window; the bright room initially dominates the glass reflection, then the tourist switches off the cabin lights and the phone takes a beat to adapt, revealing a much clearer Earth, city lights, and green aurora outside.
- **Workflow/details:** Text-to-video for a 20-second, one-continuous-shot vacation-video aesthetic with no cuts. The prompt time-codes 0–5s cabin movement, 5–10s approach/reflection, 10–13s lights-off and natural auto-exposure adaptation, and 13–20s the clearer exterior reveal. It specifies handheld walking bounce, slight tremor, imperfect framing, autofocus hunting, physically coherent glass reflections, warm-to-blue/green lighting change, spacecraft ventilation/footsteps/fabric/light-switch/breathing audio, and strict no-teleportation/no-HUD/no-floating-camera constraints.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Overview: Amateur first-person handheld phone footage recorded by a tourist inside a comfortable private room aboard a commercial orbital hotel above Earth. It feels like a casual vacation video, not a polished sci-fi movie. One continuous shot, no cuts.” The complete time-coded prompt remains visible in the verification source.
- **Why included:** Fresh explicit creator-side Flux3 attribution and a highly reproducible long-take brief. The clip is a high-signal realism benchmark because the scene must preserve room/window/Earth geometry while coordinating handheld motion, reflections, a physical switch action, delayed smartphone exposure adaptation, environmental sound, and a lighting-driven reveal over the full 20 seconds.

### 153. Late-night train-station UGC influencer continuity test — Kaan

- **Creator:** [Kaan (@kaanakz)](https://x.com/kaanakz)
- **Published:** Date not reliably exposed; verified 2026-08-22 (the public verification mirror shows a relative three-day timestamp).
- **Original source profile:** [Kaan on X](https://x.com/kaanakz) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving Kaan’s original “Made with Flux 3” wording, attached-video context, and complete visible prompt](https://w.twstalker.com/kaanakz)
- **Model attribution:** Kaan explicitly introduces the attached result with “Made with Flux 3.”
- **Summary:** A late-night European travel-vlog sequence follows the same synthetic influencer through an almost-empty train station as she races for the last train, misses it at the closing doors, processes the awkward failure, and decides to walk home.
- **Workflow/details:** Prompt-led roughly 20-second sequence written as 10 cuts mixing selfie, handheld POV, fixed external, close-selfie, wide, and rear-follow shots. The brief specifies a DV/16 mm-tape camcorder look, realistic hand shake, delayed low-light autofocus, exposure shifts, motion blur, fluorescent station lighting, readable departure-board timing, exact dialogue beats, breathing, station announcements, environmental sound, and strict continuity while avoiding a polished commercial finish.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “STYLE: Realistic late-night European travel vlog. Casual, spontaneous, slightly cinematic but never overly polished.” The complete roughly 20-second / 10-cut prompt remains visible in the verification source.
- **Why included:** Fresh explicit creator-side FLUX 3 attribution plus a fully visible, unusually reproducible prompt. It is a demanding UGC-realism benchmark for one-character identity persistence across ten edits, mixed camera grammar, low-light autofocus/exposure behavior, text-in-scene, train-door timing, natural dialogue, breathing, ambience, and an understated narrative payoff.

### 154. Gen Z street interviews in 1964 time-travel vignette — ΛRMIN

- **Creator:** [ΛRMIN (@Arminn_Ai)](https://x.com/Arminn_Ai)
- **Published:** 2026-08-19 (based on the current public verification mirror’s relative three-day timestamp at verification).
- **Original source profile:** [ΛRMIN on X](https://x.com/Arminn_Ai) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving ΛRMIN’s original wording, explicit FLUX 3 attribution, attached-video context, same-creator follow-up, and engagement](https://w.twstalker.com/Arminn_Ai)
- **Model attribution:** ΛRMIN explicitly captions the original attached video “Made with FLUX 3” and later describes the same idea as “Having a blast with FLUX 3.”
- **Summary:** A Gen Z interviewer is dropped into 1964 and runs wild street interviews, combining contemporary short-form interview behavior with a mid-1960s setting as an anachronistic time-travel comedy.
- **Workflow/details:** Creator-posted FLUX 3 video built around a 1964 street-interview premise. The accessible verification source preserves the attached-video post and a same-creator follow-up but does not expose duration, resolution, seed, reference media, exact dialogue, audio settings, or post-production, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — the creator explicitly says “prompt below 👇” and later says the prompt is in the quoted post, but the accessible verification source does not expose the prompt text; no missing wording has been reconstructed.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, attached-video context, and a strong public signal (about 11K views and 80 likes in the preserved snapshot). The concept is a distinctive benchmark for period styling, temporal/anachronistic world consistency, human performance, dialogue/street-interview staging, and comedic readability from a compact premise.

### 155. Meerkat-detail 4K upscaler benchmark vs. Topaz and Flash VSR — Dennis Schöneberg

- **Creator:** [Dennis Schöneberg](https://www.linkedin.com/in/dennis-schoeneberg)
- **Published:** 2026-08-21 (based on the secondary verification page’s relative “1 day ago” timestamp at verification).
- **Original source:** Dennis Schöneberg’s LinkedIn creator post; the direct activity URL is not exposed by the accessible public index.
- **Verification source:** [Secondary LinkedIn profile page directly embedding and quoting Schöneberg’s original creator post](https://nz.linkedin.com/in/zhenjie-zhao-b27907275/zh-cn)
- **Model attribution:** Schöneberg explicitly identifies the tested model as “FLUX 3 Video Upscale,” tags `#FLUX3`, and compares its Creative result against Topaz Astra 2, Topaz Starlight Precise 2, and Flash VSR.
- **Summary:** A 400% zoom on a tiny meerkat in a garden compares how four video upscalers reconstruct fine subject detail. Schöneberg reports that FLUX 3 Creative recovers a recognizable head and posture while the competing upscalers mostly produce distorted mutations.
- **Workflow/details:** Schöneberg built ComfyUI nodes for the new BFL upscaling API and ran a four-way comparison. He records 480p+ input support, 1.5×/2×/3× scaling up to 4K, Precise mode at 4 steps for faster identity-preserving output, and Creative mode at 8 steps for stronger repair/detail synthesis. LinkedIn’s resolution limits are why he presents a 400% crop of the small subject.
- **Prompt provenance:** `not_provided` — this is a video-super-resolution benchmark and the creator does not publish an exact prompt for the tested clip; none has been inferred.
- **Why included:** Fresh traceable creator-side `#FLUX3` attribution, attached video-comparison context, a concrete ComfyUI/API workflow, and a difficult small-subject reconstruction benchmark against three named competing upscalers. The preserved source also shows 71 reactions, indicating meaningful public interest.

### 156. Stop-sign-pigeon chain-reaction animation benchmark vs. Seedance 2.5 — Framer 🇱🇹

- **Creator:** [Framer 🇱🇹 (@Framer_X)](https://x.com/Framer_X)
- **Published:** 2026-08-22 (based on the secondary verification mirror’s relative 18-hour timestamp at verification).
- **Original source profile:** [Framer on X](https://x.com/Framer_X) — the accessible public index did not expose a stable direct status URL for this comparison.
- **Verification sources:** [Secondary creator-profile mirror preserving Framer’s original wording, explicit Flux 3 vs. Seedance 2.5 attribution, attached-video context, prompt follow-up, and engagement](https://www6.twstalker.com/framer_x) · [Independent secondary page preserving the same comparison prompt and creator attribution](https://renoise.ai/showcase/awesome-seedance-2-5-prompts)
- **Model attribution:** Framer explicitly captions the attached comparison “Flux 3 vs. Seedance 2.5 for AI animation” and says both were tested using variations of the same prompt and the same source image.
- **Summary:** A nervous traffic officer fights a pigeon perched on his STOP sign while surrounding drivers swerve and collide; after the bird leaves and the officer nervously tries to play it off, a final overhead gag ends the sequence.
- **Workflow/details:** Direct FLUX 3 vs. Seedance 2.5 comparison from one source image and a shared multi-cut prompt. The brief coordinates exact spoken dialogue, close/medium/wide cuts, pigeon motion, synchronized traffic chain reactions, character reaction continuity, and layered audio cues including whistle blasts, wings, horns, tire screeches, metallic crashes, and comic impacts. The creator says he tried a few prompt variations; exact provider, duration, resolution, seed, and model-specific settings are not publicly verified.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “The officer nervously squeezes the STOP sign pole with both hands as his eyes dart between the moving cars.” The complete multi-cut prompt remains visible in the verification sources.
- **Why included:** Fresh explicit original-creator Flux 3 attribution, attached comparison video, a visible reusable prompt, same-source-image benchmark design, and a strong public quality signal (about 20K views and 167 likes in the preserved snapshot). The sequence stress-tests animated-character continuity, dialogue, comic timing, bird/prop interaction, multi-vehicle causal motion, rapid cuts, and synchronized sound in one benchmark.

### 157. Single-still rain-soaked alley sprint with believable katana inertia — Mohamed Ali / Amr T.

- **Creator:** [Mohamed Ali](https://eg.linkedin.com/in/mohamedali-linked), collaborating with Amr T.
- **Published:** 2026-08-18 (based on LinkedIn’s public five-day relative timestamp at verification).
- **Original source profile:** [Mohamed Ali on LinkedIn](https://eg.linkedin.com/in/mohamedali-linked) — the public index exposes the creator post on his profile but not a stable direct activity URL.
- **Model attribution:** Mohamed Ali explicitly says the static source image was “ran … through **Flux 3**” and tags `#Flux3` alongside the resulting video post.
- **Summary:** One static image of the collaborators in a rain-soaked alley becomes a physically grounded sprint, with handheld camera shake, shifting wet-asphalt reflections, and a katana on the runner’s back swinging with visible inertia rather than behaving like a rigidly attached prop.
- **Workflow/details:** Image-to-video. The source still was generated with Banana 2, then animated with Flux 3. The creator specifically calls out body weight and urgency, natural handheld shake, reflections that change with movement, and believable secondary motion from the katana. Duration, resolution, seed, reference settings, audio parameters, and post-production are not publicly disclosed.
- **Prompt provenance:** `not_provided` — no exact Flux 3 generation prompt is visible in the verified first-party creator profile, and none has been reconstructed from the footage or description.
- **Why included:** Fresh first-party creator attribution and a concrete reference-image workflow focused on physical plausibility rather than spectacle. It is a useful benchmark for turning one still into coherent high-motion action while preserving scene lighting, reflective surfaces, body weight, camera inertia, and a separately moving carried object.

### 158. Tiny dragon on a real coffee cup with heat, grip, and flame physics — Mohamed Ali

- **Creator:** [Mohamed Ali](https://eg.linkedin.com/in/mohamedali-linked)
- **Published:** 2026-08-18 (based on LinkedIn’s public five-day relative timestamp at verification).
- **Original source profile:** [Mohamed Ali on LinkedIn](https://eg.linkedin.com/in/mohamedali-linked) — the public index exposes the creator post on his profile but not a stable direct activity URL.
- **Model attribution:** Mohamed Ali explicitly says the composited still was brought to life with **Flux 3** and tags `#Flux3` on the video post.
- **Summary:** A real coffee-cup photograph is augmented with a tiny photoreal dragon, then animated so the creature flexes its wings, grips the rigid cup handle, builds up a flame, and produces visible heat distortion near the coffee while remaining integrated into the original scene.
- **Workflow/details:** Real photograph → Google Nano Banana 2 for the dragon and photoreal composite → Flux 3 for motion and sound. The creator highlights micro-shadows and lighting integration in the source composite, then calls out wing-flex before takeoff, weight and tension in the claws on the handle, progressive flame ignition, heat ripples, rigid-object interaction, and generated motion/sound. He explicitly says he is not sharing the process breakdown for this post; duration, resolution, seed, exact prompt, model-side settings, and post-production therefore remain unclaimed.
- **Prompt provenance:** `not_provided` — no exact Flux 3 generation prompt is visible in the verified first-party source, and nothing has been inferred from the resulting animation.
- **Why included:** A fresh, traceable creator example with a clearly documented multimodal production path and unusually fine-grained physical interaction. The shot stress-tests micro-scale creature motion, contact with a rigid real-world prop, secondary wing movement, fire build-up, heat refraction, photoreal compositing continuity, and synchronized sound in one compact scene.

### 159. Twenty-second macro mosquito chase with physically thin laser and no hidden cut — Amr T.

- **Creator:** Amr T.
- **Published:** 2026-08-18 (based on the public LinkedIn verification page’s five-day relative timestamp).
- **Original source:** Amr T.’s original LinkedIn creator post; the accessible public index does not expose a stable direct activity URL.
- **Verification source:** [Secondary LinkedIn profile page directly embedding and quoting Amr T.’s original creator post](https://eg.linkedin.com/in/mohamedali-linked)
- **Model attribution:** Amr T. explicitly states that **FLUX 3** followed the brief and tags the creator post `#FLUX3`.
- **Summary:** A mosquito flies through a backyard at night while the camera chases it at macro scale, a dark sensor tracks it, and a thread-thin laser intercepts it; the camera then pulls all the way back to reveal the fixed device that had been hunting the insect.
- **Workflow/details:** One prompt; one continuous 20-second take; no cuts, edits, compositing, or hidden transition. The creator says the same mosquito remains singular, the backyard is not re-rolled, and the device stays fixed while the camera moves with real inertia from extreme macro to a wide orbit. He also says roughly half the prompt was devoted to restraint-oriented negative constraints, explicitly naming no giant beam, no explosion, no holographic HUD, and no floating text; the resulting laser stayed thin and physically believable.
- **Prompt provenance:** `mentioned_not_in_post` — the creator discusses how the prompt was structured and publicly names several negative constraints, but the complete generation prompt is not visible in the verified source, so no full prompt has been copied or reconstructed.
- **Why included:** A high-signal long-take continuity benchmark with explicit original-creator FLUX 3 attribution and unusually concrete evaluation notes. It combines tiny fast subject tracking, macro-to-wide camera travel, fixed-world geometry, single-subject identity, sensor/laser causality, physically restrained VFX, and strict anti-cheat constraints across a full 20 seconds.

### 160. Three-clip minimal-instruction atmospheric montage — Int.Lab

- **Creator:** [Int.Lab (@IntLab0000)](https://x.com/IntLab0000)
- **Published:** Date not reliably exposed; verified 2026-08-23 (current public mirrors place the parent post about four to five days earlier).
- **Original source profile:** [Int.Lab on X](https://x.com/IntLab0000) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving the original “Test (Flux 3)” post, same-creator workflow follow-up, attached-media context, and engagement](https://w.twstalker.com/IntLab0000)
- **Model attribution:** Int.Lab explicitly captions the parent attached-media post “Test (Flux 3).” In a same-creator follow-up about that test, he says the piece combines three video materials generated with Flux.
- **Summary:** Three separately generated FLUX 3 video materials are combined into one short atmospheric piece; the experiment intentionally uses sparse direction and evaluates whether the resulting footage can still carry rich visual information.
- **Workflow/details:** Generate three Flux video materials, combine them externally, and keep the initial instruction intentionally light. Int.Lab says the combination produced an atmosphere he liked and that the experiment was specifically about packing a lot of visual information into the footage with little direction. Duration, resolution, seed, provider, reference inputs, audio settings, exact edit structure, and post-production beyond combining the three clips are not publicly disclosed.
- **Prompt provenance:** `mentioned_not_in_post` — the creator describes using minimal instruction for the experiment but does not expose the exact generation wording, so no prompt text has been reconstructed or inferred.
- **Why included:** Explicit original-creator FLUX 3 attribution, attached-media context preserved by a public secondary source, a concrete three-clip workflow and creator-side quality assessment, plus meaningful public engagement (roughly 30 likes and about 1K views in preserved snapshots). The example is a useful counterpoint to heavily scripted prompts because it tests how much atmosphere and visual density FLUX 3 can generate from deliberately sparse direction before external assembly.

### 161. 400% meerkat-detail FLUX 3 Video Upscale benchmark vs. Topaz/Starlight/Flash VSR — Dennis Schöneberg

- **Creator:** [Dennis Schöneberg](https://de.linkedin.com/in/dennis-schoeneberg)
- **Published:** 2026-08-21 (based on LinkedIn’s public two-day relative timestamp at verification).
- **Original source:** [Dennis Schöneberg’s LinkedIn creator activity page](https://de.linkedin.com/in/dennis-schoeneberg) — the public index exposes the original creator post on-profile but not a stable direct activity permalink.
- **Model attribution:** Schöneberg explicitly identifies the test as **FLUX 3 Video Upscale**, tags `#FLUX3`, and reports the shown result from **FLUX 3 Creative**.
- **Summary:** A 400%-zoomed tiny-detail comparison uses a meerkat in a garden to pit FLUX 3 Video Upscale against Topaz Astra 2, Topaz Starlight Precise 2, and Flash VSR; Schöneberg reports that FLUX 3 Creative preserves a recognizable head and posture while the competing outputs mutate the subject more heavily.
- **Workflow/details:** Schöneberg built ComfyUI nodes for the new API and ran the same difficult tiny-detail target across the named upscalers. He documents FLUX Video Upscale as accepting source video from 480p, regenerating up to native 4K at 1.5×/2×/3×, with Precise at 4 steps for fidelity/identity and Creative at 8 steps for stronger repair/detail generation. The LinkedIn upload is a 400% zoom-in because the platform would not show the full-resolution comparison fairly.
- **Prompt provenance:** `not_provided` — no text prompt for the source clip or upscale pass is visible in the verified creator post.
- **Why included:** A fresh, primary creator-side technical benchmark with named competitors, concrete mode/step settings, ComfyUI workflow context, and a deliberately unforgiving tiny-subject reconstruction target rather than a generic launch reel.

### 162. Mumbai colony vlog with a neighborhood leopard — Rahul Nanda

- **Creator:** [Rahul Nanda (@rahulnanda86)](https://x.com/rahulnanda86)
- **Published:** 2026-08-18 (based on the public verification mirror’s relative five-day timestamp at verification).
- **Original source profile:** [Rahul Nanda on X](https://x.com/rahulnanda86) — the accessible public index did not expose a stable direct status URL for this video.
- **Primary corroboration:** [Rahul Nanda’s public LinkedIn profile](https://in.linkedin.com/in/rahulnanda86) preserves the same vlog post in his creator activity.
- **Verification source:** [Secondary public mirror preserving a retweet of Rahul’s original creator wording, explicit Flux 3 attribution, video description, and engagement](https://twstalker.com/bag_of_ideas)
- **Model attribution:** Rahul explicitly says, “Made using @bfl_ai Flux 3 video!” and states that he made the video himself.
- **Summary:** A vlog-style young woman casually shows viewers around her residential colony in Mumbai and reveals a neighborhood leopard, using an everyday phone-video premise to push synthetic footage toward ordinary social-media realism.
- **Workflow/details:** Creator-generated Flux 3 video. Rahul specifically calls out the acting, sound, and camera movements as the details that made the clip feel real to him. The verified sources do not disclose duration, resolution, input/reference mode, seed, exact generation settings, audio workflow, or post-production, so none are inferred.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified public sources, and nothing has been reconstructed from the video description.
- **Why included:** Explicit original-creator Flux 3 attribution, creator-side confirmation that he made the clip, primary LinkedIn corroboration, and a strong public quality signal (about 264K views and 1K likes in the preserved mirror snapshot). The scene is a useful realism benchmark because casual vlog acting, handheld camera behavior, environmental sound, everyday residential context, and an unusual animal reveal all have to remain believable enough that the creator says he would have taken it for real footage had he not made it himself.

### 163. Causality-driven iPhone-POV offshore-rig disaster — seeksteve

- **Creator:** [seeksteve (@seeksteve)](https://x.com/seeksteve)
- **Published:** 2026-08-18 (based on the secondary verification mirror’s relative five-day timestamp at verification).
- **Original source profile:** [seeksteve on X](https://x.com/seeksteve) — the accessible public index did not expose a stable direct status URL for this video/tutorial post.
- **Verification source:** [Secondary public mirror preserving a retweet of the original creator post, explicit FLUX 3 wording, prompt text, workflow notes, and video-example context](https://instalker.org/2017_nonsense)
- **Model attribution:** seeksteve explicitly labels the visible generation text “prompt using flux 3” and discusses recent FLUX 3 behavior while explaining the same video example.
- **Summary:** A first-person phone-POV disaster on a doomed offshore rig escalates from rough seas to an erupting giant octopus, storm damage, snapped cables, explosions, structural collapse, and a final underwater plunge.
- **Workflow/details:** Single continuous unbroken POV. The creator front-loads the recording environment, motivates every camera jolt from physical or emotional causes instead of generic shake, sequences the disaster as a causal timeline, mixes specific and vague capture-failure cues, and uses diegetic reactions and breathing with no music. He also says an explicit no-phone/no-hands constraint was added after five undesirable hand-related generations.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt remains visible in the verification source; the complete public prompt remains visible there.
- **Why included:** A traceable original-creator FLUX 3 tutorial with a video example and unusually reusable analysis of causal prompting, camera physics, temporal sequencing, failure-state realism, native audio, and negative-constraint iteration.

### 164. 640p-to-2K 3× upscale benchmark vs. Topaz — Lyss Sky

- **Creator:** [Lyss Sky | Art & Gaming (@LazerLyss)](https://x.com/LazerLyss)
- **Published:** 2026-08-21 (based on the public verification mirror’s relative three-day timestamp at verification).
- **Original source profile:** [Lyss Sky on X](https://x.com/LazerLyss) — the accessible public index did not expose a stable direct status URL for this comparison.
- **Verification source:** [Secondary BFL-team profile mirror preserving Stephen’s retweet of Lyss Sky’s original creator post, explicit FLUX3 attribution, attached comparison media, settings, and quality assessment](https://www.twstalker.com/stephenbtl)
- **Model attribution:** Lyss explicitly identifies the left side as “FLUX3 at 3x upscale” and tags Black Forest Labs’ `@bfl_ai`.
- **Summary:** A side-by-side upscaling comparison takes 640p source footage to a FLUX 3 3× result at 2K/24 fps and compares it with a Topaz/OpenArt result rendered at 4K/60 fps, focusing on natural detail recovery and artifact behavior.
- **Workflow/details:** Same 640p source; FLUX 3 Video Upscale at 3× yielding the creator-reported 2K/24 fps output; comparator is Topaz via OpenArt at 4K/60 fps. The public post does not identify the FLUX upscale mode, step count, prompt steering, or source clip provenance beyond the 640p original, so those are not inferred.
- **Prompt provenance:** `not_provided` — no text prompt or upscale-steering prompt is visible in the verified source.
- **Why included:** Fresh original-creator FLUX3 attribution with attached side-by-side video, concrete input/output resolution and frame-rate telemetry, and a direct third-party quality comparison. Lyss reports the FLUX 3 result as more natural and crisp and specifically calls out the absence of artifacts, making this a useful real-world complement to the existing official and ComfyUI-focused upscaler examples.

### 165. Zero-gravity fight physics benchmark vs. Seedance 2.5 — Atlas Cloud

- **Creator:** [Atlas Cloud (@atlas_cloud_ai)](https://x.com/atlas_cloud_ai)
- **Published:** 2026-08-22 (based on the public verification mirror’s relative two-day timestamp at verification).
- **Original source profile:** [Atlas Cloud on X](https://x.com/atlas_cloud_ai) — the accessible public index did not expose a stable direct status URL for this comparison.
- **Verification source:** [Secondary creator-profile mirror preserving Atlas Cloud’s original post, explicit FLUX 3 vs. Seedance 2.5 attribution, attached-video context, and benchmark description](https://www6.twstalker.com/atlas_cloud_ai)
- **Model attribution:** Atlas Cloud explicitly frames the attached comparison as “FLUX 3 vs Seedance 2.5” and tags `#FLUX3`.
- **Summary:** A fight scene abruptly loses gravity mid-action: fighters, furniture, and debris begin floating while the camera rotates with the room, creating a same-concept stress test against Seedance 2.5.
- **Workflow/details:** Direct two-model comparison centered on a zero-gravity transition. The creator explicitly evaluates motion, character consistency, physics, object interaction, and camera stability. Exact prompt text, duration, resolution, reference inputs, provider settings, and post-production are not disclosed in the verified post, so none are inferred.
- **Prompt provenance:** `not_provided` — the post describes the benchmark scenario but does not identify that prose as the exact generation prompt.
- **Why included:** Fresh original-creator `#FLUX3` comparison with attached video and a technically demanding causal scene: multiple humans and props must transition into weightlessness while retaining identity, object relationships, coherent room geometry, and a rotating camera. It is a useful cross-model physics benchmark rather than a generic beauty shot.

### 166. 360-degree orbit museum-gravity collapse with focal anchoring — LudovicCreator

- **Creator:** [LudovicCreator (@LudovicCreator)](https://x.com/LudovicCreator)
- **Published:** 2026-08-24 (based on the secondary verification mirror’s relative seven-hour timestamp at verification).
- **Original source profile:** [LudovicCreator on X](https://x.com/LudovicCreator) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary creator-profile mirror preserving LudovicCreator’s original wording, explicit FLUX 3 attribution, exact prompt, attached-video context, and engagement](https://w.twstalker.com/LudovicCreator)
- **Model attribution:** LudovicCreator explicitly introduces the visible generation text with “Prompt made with FLUX 3”.
- **Summary:** A grieving curator remains almost frozen at the center of a slow 360-degree museum orbit while the gallery progressively tilts and loses gravity around them: portraits drift from walls, busts slide onto the ceiling, exhibit labels float, and spotlights swing overhead.
- **Workflow/details:** The creator explains the shot as a focal-anchoring and multi-layered-parallax exercise: keep the subject dead center during a continuous 360-degree camera track, distribute motion across near-field, mid-ground, and ceiling planes, use warm track lighting, and specify a 24 mm wide lens with controlled rotation so the environment can deconstruct without losing spatial orientation.
- **Prompt provenance:** `verbatim_in_post` — the complete prompt remains visible in the verification source.
- **Why included:** Fresh explicit creator-side FLUX 3 attribution and a fully visible prompt with unusually reusable camera-direction notes. The scene is a difficult temporal-spatial benchmark: the model must preserve a stable centered subject while executing continuous orbital camera motion, layered parallax, multiple independently moving props, changing gravity cues, and coherent museum geometry.

### 167. Rickshaw driver takes a train to beat traffic — Rahul Nanda

- **Creator:** [Rahul Nanda (@rahulnanda86)](https://x.com/rahulnanda86)
- **Published:** 2026-08-24 (based on the secondary verification mirror’s relative 18-hour timestamp at verification).
- **Original source profile:** [Rahul Nanda on X](https://x.com/rahulnanda86) — the accessible public index did not expose a stable direct status URL for this video.
- **Verification source:** [Secondary public mirror preserving a retweet of Rahul’s original creator wording, explicit Flux 3 attribution, attached-video context, and engagement](https://www.twstalker.com/Shreyas54125712)
- **Model attribution:** Rahul explicitly captions the creator-posted video “Ricshawalla takes a train to beat traffic!! Made using Flux 3.”
- **Summary:** A rickshaw driver tries to beat road traffic by taking the train, turning an immediately legible urban-commute joke into an everyday-realism FLUX 3 video rather than a stylized effects showcase.
- **Workflow/details:** Creator-generated Flux 3 video. The verified source does not disclose duration, resolution, input/reference mode, seed, prompt, native-audio settings, or post-production, so none are inferred.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified public source, and the concise caption is treated as a concept/title rather than a generation prompt.
- **Why included:** Fresh explicit original-creator Flux 3 attribution, traceable creator identity, attached-video context, and a very strong public quality signal (about 193K views and 156 likes in the preserved snapshot). The simple real-world premise is a useful plausibility benchmark for vehicle identity, commuter-space staging, urban motion, and comedic timing without relying on an elaborate visible prompt.

### 168. Twenty-second prompt-adherence benchmark from a 30-second Korean home-video brief — seeksteve

- **Creator:** [seeksteve (@seeksteve)](https://x.com/seeksteve)
- **Published:** 2026-08-24 (based on the secondary verification mirror’s relative 20-hour timestamp at verification).
- **Original source profile:** [seeksteve on X](https://x.com/seeksteve) — the accessible public index did not expose a stable direct status URL for this comparison.
- **Verification source:** [Secondary public mirror preserving a retweet of seeksteve’s original comparison wording, quoted source prompt, explicit Flux 3 attribution, attached-video context, and engagement](https://ww.twstalker.com/bonkuratv)
- **Model attribution:** seeksteve explicitly says he is “testing prompt adherence between seedance 2.5 and flux 3” and states that he adapted the timing from 30 seconds to 20 seconds.
- **Summary:** A controlled prompt-adherence comparison reuses beech’s ultra-realistic candid-home-video concept of an elderly Korean man spending an ordinary late morning in a residential neighborhood, compressing the original 30-second brief into a FLUX 3-compatible 20-second version.
- **Workflow/details:** seeksteve credits the original prompt to [beech (@beechinour)](https://x.com/beechinour) and says he adapted its timing from 30s to 20s for the comparison. The preserved source prompt emphasizes a consistent elderly Korean subject, weathered skin, clothes and posture, plus an authentic low-rise residential neighborhood with alleys, plants, laundry lines, bicycles, utility poles, overhead wires and mature trees. Exact provider settings, resolution, seed, reference media, audio configuration, and any additional edits are not exposed.
- **Prompt provenance:** `mentioned_not_in_post` — the verified source visibly quotes the opening of beech’s original 30-second prompt, but seeksteve’s exact 20-second adapted prompt is not publicly exposed, so no missing wording is reconstructed.
- **Why included:** Fresh explicit creator-side Flux 3 comparison, transparent prompt provenance, a controlled duration adaptation instead of a loosely matched concept, and a strong public quality signal (about 32K views and 324 likes in the preserved snapshot). It is a useful realism/prompt-adherence benchmark for identity, wardrobe, environment persistence, natural human motion, and mundane documentary-video plausibility.

### 169. Architecture prompt-and-video workflow suite with start-frame motion and native ambience — RunDiffusion

- **Creator:** [RunDiffusion](https://www.rundiffusion.com/)
- **Published:** 2026-08-26 (public search index; the guide page itself does not expose a byline date).
- **Original source:** [FLUX 3 Prompt Guide for Architecture and AI Video](https://www.rundiffusion.com/flux-3-prompt-guide)
- **Model attribution:** RunDiffusion explicitly says architecture teams use FLUX 3 on RunDiffusion and presents embedded video outputs inside the guide while its documented workflow selects `Flux 3 Video`.
- **Summary:** A newly published first-party architecture suite demonstrates FLUX 3 across text-to-video, start-frame animation, start-and-end transitions, timestamped motion beats, synchronized ambience and foley, and video continuation. A representative embedded clip begins from an approved adaptive-reuse headquarters courtyard rendering, then slowly dollies toward a lit glass-and-timber atrium as grasses and a reflecting pool move naturally.
- **Workflow/details:** RunDiffusion documents `Flux 3 Video`, `Flux 3 Extend Video`, `Flux 3 Draft Video`, and `Flux 3 Draft Extend Video`; accepted inputs include text, one start image, a start-and-end image pair, or an existing source clip. Most tools support up to 20 seconds, with optional synchronized dialogue, ambience, physical effects, and music. The guide also demonstrates short prompts, labeled fields, timestep prompting, start/end anchors, and continuation workflows.
- **Prompt provenance:** `verbatim_in_post` — “Wide shot of an adaptive-reuse headquarters courtyard in warm evening light. The camera slowly dollies forward along the central stone path toward the illuminated glass-and-timber atrium. Ornamental grasses move lightly and the reflecting pool ripples. Light wind through the grasses and faint water movement.”
- **Why included:** Fresh first-party source with multiple embedded FLUX 3 videos, exact visible prompts, concrete workflow controls, and highly reusable architecture-specific direction. The representative start-frame clip is a subtle but demanding test of geometry/material retention, measured camera motion, vegetation and water physics, reflections, lighting, and scene-matched native ambience rather than spectacle.

### 170. 480p Seedance 2.5 → FLUX 3 Precise 1080p cost-saving upscale workflow — Halim Alrasihi

- **Creator:** [Halim Alrasihi (@HalimAlrasihi)](https://x.com/HalimAlrasihi)
- **Published:** 2026-08-27 (based on public creator-profile mirrors’ relative one-day timestamp at verification).
- **Original source profile:** [Halim Alrasihi on X](https://x.com/HalimAlrasihi) — the accessible public indexes did not expose a stable direct status URL for this video.
- **Verification sources:** [Secondary creator-profile mirror preserving the original wording, follow-up workflow details, and engagement](https://twstalker.com/HalimAlrasihi) · [Secondary public mirror directly preserving a retweet of the original creator post with an attached-video marker](https://www.sotwe.com/bonkuratv)
- **Model attribution:** Halim explicitly calls the finishing model the “new FLUX 3 video upscaler” and identifies the mode as “FLUX 3 precise” while describing this specific clip workflow.
- **Summary:** A low-resolution Seedance 2.5 generation is used as the source, then FLUX 3 Precise reconstructs it to 1080p, demonstrating a practical two-model path aimed at retaining good motion and fine detail while avoiding the cost of repeated native-1080p generations.
- **Workflow/details:** Seedance 2.5 at 480p → FLUX 3 Precise upscale to 1080p. Halim says the source video is 480p, reports roughly one minute for a 7–10 second upscale, and recommends generating or rerolling at 480p or 720p before upscaling because direct Seedance 2.5 1080p generation was nearly 3× more expensive in his workflow. He says he runs FLUX through Black Forest Labs’ official platform. No source-generation prompt, seed, exact FLUX API parameters, or post-processing beyond the upscale is publicly verified.
- **Prompt provenance:** `not_provided` — no exact generation prompt for the Seedance source clip or text steering for the FLUX 3 upscale pass is visible in the verified public sources.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution with attached-video context, a highly reusable cost/quality pipeline, concrete source/output resolution and turnaround notes, and a strong public quality signal (more than 50K views and 500 likes in preserved creator-profile snapshots). Unlike a generic upscaler demo, this documents a pragmatic cross-model production strategy: reroll motion cheaply at low resolution, then spend on FLUX 3 Precise only after choosing a keeper.

### 171. Eight-model seven-reference first-generation benchmark — Tianyu Xu

- **Creator:** [Tianyu Xu](https://www.linkedin.com/in/tianyuxu/)
- **Published:** 2026-08-25
- **Original source:** [Tianyu Xu’s LinkedIn reference-to-video comparison](https://www.linkedin.com/posts/tianyuxu_reference-to-video-comparison-seedance-activity-7497985288783151104-J5ty)
- **Model attribution:** Xu explicitly names **FLUX 3** as one of the eight models in his own reference-to-video comparison and presents its result among the examples in the post.
- **Summary:** A controlled creator-authored benchmark compares Seedance 2.5, WAN 3, FLUX 3, MiniMax H3, Seedance 2.0, Seedance 2.0 Mini, Kling 3 Omni, and Grok Imagine 1.5 on one shared creative setup, making the FLUX 3 output directly comparable with seven current peers.
- **Workflow/details:** Xu states that every model used the same prompt and the same set of seven reference images; each example was the first generated video, with no cherry-picking, no edits, and native audio. The public post does not document any model-specific adaptation of the seven-reference input, so none is inferred.
- **Prompt provenance:** `mentioned_not_in_post` — Xu explicitly says all eight models used the same prompt, but the exact prompt text is not visible in the verified public post and has not been reconstructed.
- **Why included:** Fresh primary creator source with attached comparison media, unambiguous FLUX 3 attribution, strong public engagement, and an unusually rigorous anti-cherry-picking methodology: shared prompt, shared visual inputs, first outputs only, no edits, and native audio across eight current video models.

### 172. Three exact-prompt native-audio production examples — VideoGen

- **Creator:** [VideoGen](https://videogen.io/) — first-party FLUX 3 integration showcase.
- **Published:** 2026-08-27 (public search index; the page itself does not expose a byline date).
- **Original source:** [VideoGen FLUX 3 model page with prompt-to-output examples](https://videogen.io/flux-3)
- **Model attribution:** VideoGen labels the gallery as FLUX 3 examples and explicitly states that the showcased prompts and outputs were generated with FLUX 3 in VideoGen.
- **Summary:** Three first-party examples cover a blacksmith striking glowing steel with event-synced metal, sparks, and bellows ambience; a café close-up with spoken barista dialogue plus espresso-machine and room chatter; and a rainy diner neon-sign shot with buzzing letters and reflected light on wet pavement.
- **Workflow/details:** The page documents FLUX 3 in VideoGen with up to 20-second clips, native dialogue/effects/ambience, 720p output plus 1080p via upscaling, text-to-video, image-to-video, keyframes, continuation, and multi-shot modes, plus a low-cost draft workflow that can be re-rendered at full quality. Clip-specific durations, seeds, and reference settings are not exposed, so none are inferred.
- **Prompt provenance:** `verbatim_in_post` — visible example excerpt: “A blacksmith hammers glowing steel on an anvil in a dim workshop, each strike lands with a sharp metallic ring…” Full exact prompts for all three showcased outputs remain visibly published on the source page.
- **Why included:** Newly surfaced first-party source with multiple explicit FLUX 3 video outputs, exact prompt-to-output mappings, and reproducible model controls. The examples jointly test photoreal materials, fine hand-object motion, dialogue, event-synchronized sound, readable neon text, and wet-surface reflections.

### 173. 1970s neo-noir motel-hallway long-shot with layered audio — ElevenLabs / ElevenCreative

- **Creator:** [ElevenLabs / ElevenCreative](https://elevenlabs.io/) — first-party FLUX 3 integration showcase.
- **Published:** Date not shown; verified 2026-08-29.
- **Original source:** [ElevenLabs Flux 3 Video page with prompt and in-action showcase](https://elevenlabs.io/video/flux-3)
- **Model attribution:** ElevenLabs explicitly presents the hero generation under Flux 3 Video and identifies the showcase as real prompts and real generations produced by the ElevenLabs team.
- **Summary:** A slow handheld tracking shot follows a detective down a midnight motel corridor as practical lights fail and recover, environmental props subtly move, a final door opens onto blue television light, and the character freezes in silhouette.
- **Workflow/details:** The visible brief coordinates camera movement, sequential action, 1970s neo-noir film treatment, lighting changes, prop behavior, and layered audio—damp-carpet footsteps, fluorescent buzz, vending-machine rattle, rain, door creak, and distant TV—with explicit no-music/no-logo/no-extra-people constraints. ElevenLabs also documents optional image or clip references plus text-to-video, image-to-video, and video-reference workflows. No clip-specific duration, seed, or reference settings are exposed.
- **Prompt provenance:** `verbatim_in_post` — visible prompt begins: “Slow handheld tracking shot behind a detective walking down a narrow motel hallway at midnight”. The complete prompt remains visibly published on the first-party page.
- **Why included:** Fresh first-party source with a directly presented FLUX 3 generation and a highly detailed reproducible prompt. It is a strong long-shot continuity test of camera geometry, lighting-state transitions, subtle prop motion, character performance, and precisely layered audiovisual ambience.

### 174. Eight-minute retro-OVA space-horror short “AVERNUS-9” — Iskarioto Dystopian AI Films

- **Creator:** [Iskarioto Dystopian AI Films (@Iskarioto)](https://www.youtube.com/@Iskarioto)
- **Published:** 2026-08-26
- **Original source:** [“AVERNUS-9” | Space Horror Short Film (Flux 3) [4K]](https://youtu.be/6NQl2fjAkyI)
- **Model attribution:** The creator’s original YouTube upload explicitly says “Created with Flux 3 Text2video-audio,” and the creator’s public X/Instagram profiles repeat the FLUX 3 attribution for the same film.
- **Summary:** An approximately eight-minute animated space-horror short built as a retro 1980s OVA/cyberpunk homage, expanding FLUX 3 from a benchmark clip into a sustained narrative audiovisual production.
- **Workflow/details:** Creator-identified FLUX 3 Text2video-audio workflow; the finished film is published in 4K and runs about eight minutes. The verified public sources do not expose clip-level prompts, seeds, reference assets, source render resolution, provider settings, or post-production/editing details, so none are inferred.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified primary sources, and nothing has been reconstructed from the film.
- **Why included:** Fresh original-creator primary source with explicit FLUX 3 attribution and a full-length attached video. The unusually long runtime, cohesive retro-OVA art direction, space-horror staging, and complete audiovisual presentation make it a production-scale quality example rather than a short isolated demo.

### 175. Side-by-side FLUX 3 vs. MiniMax H3 Max timing sample — Design Arena

- **Creator:** [Design Arena (@DesignArena)](https://x.com/DesignArena)
- **Published:** 2026-08-28 (based on the secondary verification mirror’s relative one-day timestamp at verification on 2026-08-29).
- **Original source profile:** [Design Arena on X](https://x.com/DesignArena) — the accessible public indexes did not expose a stable direct status URL for this reply video.
- **Verification source:** [Secondary creator-profile mirror preserving Design Arena’s original comparison caption, attached tweet-video marker, explicit model attribution, reported generation times, and engagement](https://www.sotwe.com/Designarena)
- **Model attribution:** Design Arena explicitly labels one side “Flux 3 Video by @bfl_ai.” In the same thread, the comparison target is identified as MiniMax H3 Max; the reply abbreviates that side as “M3 Max by @fal.”
- **Summary:** A fresh side-by-side benchmark places an actual FLUX 3 Video output next to fal’s H3 Max output, letting viewers inspect the visual results while Design Arena publishes the observed generation time for each sample.
- **Workflow/details:** Attached side-by-side comparison video. Design Arena reports 23.7 seconds for the fal H3 Max/M3 Max sample and 10 minutes 55 seconds for the FLUX 3 Video sample. The public reply does not expose the exact prompt, source frame, duration, resolution, seed, audio settings, queue conditions, or hardware, so the timing is recorded only as this specific sample rather than generalized into a model-wide speed claim.
- **Prompt provenance:** `not_provided` — no exact prompt is visible in the verified source, and none has been inferred from the comparison footage.
- **Why included:** Newly published, traceable benchmark-source attribution with an attached comparison video, explicit FLUX 3 labeling, concrete measured timing, and a strong public signal (about 27K views in the preserved snapshot). It is useful for practical quality-versus-latency evaluation while remaining careful not to overgeneralize from one timed example.

### 176. Commercial-visual pure-T2V benchmark vs. Seedance 2.5 / 2.0 — 铃雨云AIGC

- **Creator:** 铃雨云AIGC
- **Published:** 2026-08-29 (based on ZCOOL’s relative “18 hours ago” timestamp at verification).
- **Original source:** [Creator’s ZCOOL post with embedded comparison video](https://www.zcool.com.cn/work/ZNzQwMTkwMjA%3D.html)
- **Model attribution:** The creator explicitly states that the video compares `FLUX3`, Seedance 2.5, and Seedance 2.0 in a pure text-to-video test.
- **Summary:** A creator-run commercial-visual benchmark compares the three models across fashion advertising, multi-character scenes, character MV, branded shorts, and other production-oriented looks, focusing on face stability, character consistency, clothing/material detail, body motion, interaction, camera movement, shot changes, spatial relationships, composition, and fashion/commercial visual language.
- **Workflow/details:** The entire comparison is pure text-to-video with no reference characters or real-person footage. Seedance 2.5 and 2.0 were each generated three times from prompts in the same direction and the strongest overall take was selected; all shown outputs preserve the original model result with no extra AI repair or local rerendering. FLUX3 was rendered at 1080p, while Seedance 2.5 and 2.0 were rendered at 720p; the creator notes that clip length and generation conditions differ and explicitly does not frame the test as a strict benchmark.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified creator page, so none has been copied or inferred.
- **Why included:** Newly published primary creator source with an embedded video, explicit FLUX3 attribution, unusually transparent comparison methodology, verified output-resolution differences, and candid quality notes. The creator finds FLUX3 especially strong in composition, materials, lighting, fashion aesthetics, and designed-looking pure-T2V results while also documenting weaker stability, character dynamics, controllability, and image-to-video behavior, making the post useful as both a showcase and a production-oriented failure analysis.

### 177. 2K/4K FLUX.3 Video Upscale integration demo — Higgsfield

- **Creator:** [Higgsfield AI (@higgsfield)](https://x.com/higgsfield)
- **Published:** 2026-08-27
- **Original source:** [Higgsfield product changelog](https://www.higgsfield.company/creator-hub/changelog)
- **Secondary verification source:** [Public creator-profile mirror preserving Higgsfield’s original FLUX.3 post and attached tweet video](https://www.sotwe.com/higgsfield)
- **Model attribution:** Higgsfield explicitly announces “FLUX.3 Video Upscale is now on Higgsfield”; its first-party changelog names the feature “FLUX 3 Video Upscaler.”
- **Summary:** Higgsfield’s launch demo presents FLUX.3 Video Upscale as a high-resolution finishing step intended to preserve natural motion and realism while producing 2K or 4K deliverables from an input clip.
- **Workflow/details:** Open Upscale and upload any video; Higgsfield documents 1080p, 2K, and 4K output. Precise mode raises resolution without adding new detail, while Creative mode adds or reworks detail and accepts an optional detail-guidance prompt. The first-party changelog also states that motion remains smooth and audio stays in sync. The verified sources do not expose the demo clip’s input resolution, exact selected output, prompt, seed, or latency, so none are inferred.
- **Prompt provenance:** `not_provided` — no exact prompt for the attached demonstration video is visible. Creative mode generally supports optional prompt steering, but no clip-specific prompt is published.
- **Why included:** Fresh first-party platform release with explicit FLUX.3 attribution, a traceable attached-video announcement preserved by a public creator-profile mirror, strong public engagement (about 23K views and 306 likes in the preserved snapshot), and concrete reproducible output targets and mode behavior. It is a practical production-finishing example rather than a vague model mention.

### 178. French-pronunciation and natural-performance benchmark across 13 video models — Gilles Guerraz

- **Creator:** [Gilles Guerraz](https://fr.linkedin.com/in/gilles-guerraz-iagenerative)
- **Published:** 2026-08-26 (based on LinkedIn’s public relative timestamp at verification on 2026-09-01).
- **Original source:** [Gilles Guerraz’s LinkedIn comparison post with attached video](https://fr.linkedin.com/posts/gilles-guerraz-iagenerative_on-dit-que-le-fran%C3%A7ais-est-une-des-langues-activity-7497903023537438720-IXqo)
- **Model attribution:** Guerraz explicitly lists **Flux 3.0** among the 13 video models in his own comparison and reports it as one of seven models that successfully deliver the requested French line without the pronunciation problems he heard in weaker outputs.
- **Summary:** A same-source-image dialogue benchmark asks 13 current video models to make one character speak a single French sentence, then compares both pronunciation accuracy and the acting choices each model invents when no performance direction is supplied.
- **Workflow/details:** One identical reference image generated with Midjourney 8.2; one English-language prompt; the same requested French sentence for all models. Guerraz evaluates pronunciation separately from acting and notes that many models overplay the delivery when the prompt does not specify performance style. The attached comparison video includes Flux 3.0 alongside MiniMax H3, Veo 3.1, Wan 3.0, Grok Imagine, LTX 2.5 Pro, Pixverse 6, and other current systems. Model-specific resolution, seed, provider settings, and post-processing are not disclosed, so none are inferred.
- **Prompt provenance:** `verbatim_in_post` — the exact requested spoken line is visibly published: “Bien sûr que je sais parler français ! C'est ma langue natale !” The rest of the English generation prompt is described but not fully exposed in the verified page, so no missing wording is reconstructed.
- **Why included:** Fresh primary creator source with an attached comparison video, explicit Flux 3.0 attribution, a controlled same-image/same-instruction methodology, and a high-signal native-audio test that separates pronunciation quality from unscripted performance behavior rather than treating lip-sync as a single aggregate score.

### 179. Same-source, same-prompt sprinter acceleration benchmark across 10 video models — Gilles Guerraz

- **Creator:** [Gilles Guerraz](https://fr.linkedin.com/in/gilles-guerraz-iagenerative)
- **Published:** 2026-08-26 (based on LinkedIn’s public six-day relative timestamp at verification on 2026-09-01).
- **Original source:** [Gilles Guerraz’s LinkedIn sports-motion comparison with attached video](https://fr.linkedin.com/posts/gilles-guerraz-iagenerative_minimax-h3-et-flux-30-ont-ils-surpass%C3%A9-seedance-activity-7491062141974798336-kqeB)
- **Model attribution:** Guerraz explicitly includes **Flux 3.0** among the ten named systems in the comparison and presents its output inside the attached benchmark video.
- **Summary:** A world-class sprinter launches from the blocks in dramatic slow motion before the action abruptly snaps to full real-time speed, creating a difficult benchmark for explosive acceleration, leg drive, body mechanics, temporal speed changes, and physically credible athletic motion.
- **Workflow/details:** Rigorous creator-stated protocol: the same source image from Reve, the same prompt for every model, three generations per model, and only the best result retained for the comparison. The tested set includes Seedance 2.0 Mini/Fast/standard, Kling 3.0/Turbo, Grok Imagine 1.5, MiniMax H3, Pixverse 6, Flux 3.0, and Happy Horse 1.1. Exact Flux 3.0 provider settings, resolution, seed, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — verified visible excerpt: “A world-class sprinter explodes out of the starting blocks. The action begins in dramatic slow motion, capturing the raw power of his first strides”. The complete prompt remains visible in the original creator post; no wording has been inferred from the footage.
- **Why included:** Newly published primary creator source with attached video, explicit Flux 3.0 attribution, an exact visible prompt, and unusually disciplined cross-model methodology. Fast sport motion remains a known generative-video stress case, and this test directly probes the hard transition from stylized slow motion into very high-speed running under identical starting conditions.

### 180. Fifteen-second single-reference image-to-video motion-control test — Simon Hirtz

- **Creator:** Simon Hirtz
- **Published:** 2026-08-26
- **Original source:** [Simon Hirtz’s LinkedIn creator post](https://www.linkedin.com/posts/simon-hirtz-25a011a5_bfl-flux3-i2v-activity-7498315243136307200-c0Od)
- **Model attribution:** Hirtz explicitly tags the attached 15-second image-to-video result `#Flux3` and `#I2V`.
- **Summary:** A single still image is expanded into a 15-second image-to-video sequence, with the experiment centered on whether motion can stay coherent over a longer take while camera behavior and pacing are steered through text.
- **Workflow/details:** Image-to-video from one reference image; 15-second duration. Hirtz says prompt phrasing and rhythm are the control surface for camera and pacing, and candidly notes that both are still imperfect in places while the motion holds longer than he expected from one still. The source does not disclose resolution, seed, exact reference-image provenance, provider settings, audio parameters, or post-production, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — the creator discusses how the prompt is written and how phrasing/rhythm affect camera and pacing, but the exact prompt text is not visible in the verified source.
- **Why included:** Newly published primary creator source with explicit `#Flux3` attribution and a concrete one-frame-to-15-second workflow. It is a useful long-horizon I2V benchmark because it focuses on motion persistence from a single still and provides candid creator-side notes about the relationship between text phrasing, pacing, and camera control rather than presenting an unqualified showcase.

### 181. Twenty-second 1990s ape-sitcom story from one compact prompt — Christopher Fryant

- **Creator:** [Christopher Fryant (@cfryant)](https://x.com/cfryant)
- **Published:** 2026-09-01 (based on the public creator-profile mirror’s relative 12-hour timestamp at verification on 2026-09-02).
- **Original source profile:** [Christopher Fryant on X](https://x.com/cfryant) — the accessible public index did not expose a stable direct status URL for this post.
- **Secondary verification source:** [Public creator-profile mirror preserving Fryant’s original FLUX 3 prompt-share wording, attached-video context, and engagement](https://w.twstalker.com/cfryant)
- **Model attribution:** Fryant explicitly labels the post “FLUX 3 Prompt share” immediately before the generation prompt.
- **Summary:** A stereotypical 1990s sitcom replaces its human cast with apes—chimpanzees, gorillas, and orangutans—while moving from a bar to a living room and carrying one story across the full clip.
- **Workflow/details:** One compact text prompt; 20-second duration; the creator explicitly asks FLUX 3 to maintain narrative continuity from the opening bar scene to the ending living-room scene. No verified resolution, provider, seed, reference media, audio settings, or post-production details are publicly exposed, so none are inferred.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Starts in a bar and ends in a living room. Carry a story throughout, you have 20 seconds.” The full prompt remains visible in the verification source.
- **Why included:** Fresh original-creator FLUX 3 attribution, an exact reusable prompt, a full-duration narrative constraint, and a strong early public signal (about 4K views in the preserved snapshot). The clip stresses genre fidelity, multi-character/species consistency, location transition, story continuity, and comedic readability from deliberately sparse direction.

### 182. SketchUp → Claude → Nano Banana → FLUX 3 start/end-frame ArchViz animation — Jacques Vernet

- **Creator:** [Jacques Vernet](https://fr.linkedin.com/in/jacques-vernet)
- **Published:** Date not exposed; verified 2026-09-02 (LinkedIn exposes only a relative two-to-three-week timestamp).
- **Original source:** [Jacques Vernet’s LinkedIn creator post with embedded workflow video and transcript](https://fr.linkedin.com/posts/jacques-vernet_sketchup-archviz-artificialintelligence-activity-7491785025990897664-Ef73)
- **Model attribution:** Vernet explicitly states that **Flux 3** takes the generated start image and end image to produce a smooth 10-second video animation; the embedded transcript independently repeats that he connects the start/end images to Flux 3 and launches the render.
- **Summary:** A lightweight SketchUp architectural scene is captured from the viewport, converted into photoreal endpoint renders, then animated into a controlled 10-second architectural shot with FLUX 3 rather than relying on a conventional heavy 3D render-and-animation pass.
- **Workflow/details:** Node-graph workflow: dynamic camera-facing 2D vegetation in SketchUp → viewport capture → Claude analyzes the view and generates/optimizes the prompt → Nano Banana produces photoreal HD render(s) → start and end images are connected to FLUX 3 → 10-second animation. The public source does not expose the exact FLUX provider, output resolution, seed, audio settings, or post-production, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — Vernet explicitly shows and describes Claude generating/optimizing the prompt from the image plus a text instruction, but the exact prompt text is not visible in the post or transcript.
- **Why included:** Primary creator source with an embedded workflow video/transcript, explicit Flux 3 attribution, a defined start/end-frame workflow and duration, and an unusually reproducible ArchViz production chain. It demonstrates FLUX 3 as the animation stage inside a practical SketchUp-to-photoreal pipeline while keeping architectural motion anchored to approved endpoint frames.

### 183. One-image, one-prompt 20-second premium headphones commercial — Alessandro Bagnuoli

- **Creator:** [Alessandro Bagnuoli](https://it.linkedin.com/in/alessandrobagnuoli89)
- **Published:** Date not exposed; verified 2026-09-03 (LinkedIn’s public creator profile showed the post as 3 days old).
- **Original source:** [Alessandro Bagnuoli’s LinkedIn creator profile containing the original post](https://it.linkedin.com/in/alessandrobagnuoli89) — the public index exposes the post on-profile but not a stable direct activity permalink.
- **Model attribution:** Bagnuoli explicitly describes the tutorial as the “full FLUX 3 workflow on Aristotto AI” and tags the post `#FLUX3`.
- **Summary:** “AURA ONE” is a 20-second premium headphones spot developed from one photorealistic source image, moving through an urban setting, product interaction, and a closing hero shot.
- **Workflow/details:** One image → one prompt → one output. Bagnuoli explicitly says there are no keyframes and no multiple references, keeping the workflow intentionally simple and repeatable for first-time users. The verified public source does not expose the exact FLUX 3 resolution, seed, provider-side settings, or post-production, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — the creator confirms that one prompt drives the workflow, but the exact prompt text is not visible in the verified public source and has not been reconstructed.
- **Why included:** Newly published primary creator evidence with explicit FLUX 3 attribution and a concrete tutorial/video workflow. The example is unusually reusable for commercial production because it demonstrates a complete 20-second product ad from a single still and a single prompt, without keyframes or multiple-reference scaffolding, while still targeting setting continuity, product interaction, and a final hero composition.

### 184. Water, smoke, reflections, motion, and skin-detail stress reel — Fuzzbucket AI

- **Creator:** [Fuzzbucket AI](https://www.linkedin.com/company/fuzzbucket)
- **Published:** 2026-08-31 (based on LinkedIn’s public relative three-day timestamp at verification on 2026-09-03).
- **Original source:** [Fuzzbucket AI’s first-party LinkedIn company page with the attached FLUX-3 video](https://www.linkedin.com/company/fuzzbucket) — the public index exposes the creator post on-profile but not a stable direct activity permalink.
- **Model attribution:** Fuzzbucket explicitly says the entire attached video was generated with **FLUX-3 inside Fuzzbucket** and prefixes the post `#FLUX-3`.
- **Summary:** A first-party platform reel deliberately pushes FLUX-3 through visually difficult material cues—water, smoke, reflections, fast motion, and fine skin detail—rather than using a single safe beauty shot.
- **Workflow/details:** Generated end-to-end with FLUX-3 inside Fuzzbucket. The creator explicitly identifies water, smoke, reflections, motion, and skin detail as the stress targets. The verified public post does not disclose the exact prompt, clip duration, resolution, seed, reference media, audio settings, or post-production, so none are inferred.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified first-party source.
- **Why included:** Fresh first-party creator/platform attribution with an attached video and an unusually broad visual stress target in one reel. It is useful as a quality benchmark because reflective surfaces, volumetric smoke, fluid appearance, human skin, and motion are common temporal failure modes, and the post explicitly says the goal was to push the model rather than show “safe test shots.”

### 185. Fifteen-second MiniDV urban-dinosaur documentary long take — DennisVisuals

- **Creator:** [DennisVisuals (@DtheW1995)](https://x.com/DtheW1995)
- **Published:** 2026-09-01 (based on the secondary verification mirror’s relative two-day timestamp at verification on 2026-09-03).
- **Original source profile:** [DennisVisuals on X](https://x.com/DtheW1995) — the accessible public index did not expose a stable direct status URL for the video/prompt thread.
- **Secondary verification source:** [Public creator-profile mirror preserving DennisVisuals’ original wording, explicit Flux 3 attribution, attached tweet-video marker, and complete visible prompt](https://www.sotwe.com/DtheW1995)
- **Model attribution:** DennisVisuals explicitly opens the attached-video post “Jurassic City Documentary Style made with Flux 3,” and the prompt itself is labeled `FLUX 3`.
- **Summary:** A calm, early-2000s wildlife-documentary encounter unfolds from inside an open-top safari jeep on a quiet American city avenue: a realistic dinosaur approaches, stops beside the vehicle, curiously sniffs the reporter and passengers, then departs between parked cars while the handheld cameraman keeps filming.
- **Workflow/details:** One continuous 15-second MiniDV-style take with no cinematic music. The prompt time-codes four phases (0–2.5s, 2.5–5s, 5–10.5s, 10.5–15s), specifies mild handheld shake, imperfect optical zoom, slow autofocus, exposure changes, washed colors, interlaced motion and tape compression, natural city/vehicle/creature ambience, English dialogue, and strict continuity for one jeep, reporter, cameraman, passenger group, dinosaur appearance/scale, and camera position inside the vehicle.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “FLUX 3 — 15-second ultra-realistic early-2000s wildlife documentary footage, recorded on a consumer MiniDV camera...” The complete prompt remains visibly preserved in the verification source.
- **Why included:** Fresh explicit original-creator FLUX 3 attribution, attached-video context, and a fully visible, highly reproducible prompt. The clip is a demanding realism benchmark for creature scale and body weight, gentle human-creature proximity, contact-free interaction, long-take spatial continuity, intentionally imperfect consumer-camera behavior, dialogue, environmental sound, and a coherent release beat without relying on spectacle or rapid cuts.

### 186. Agentic 10-second FLUX 3 portrait-to-premium-ad production chain — Jean-Louis VIRETTI

- **Creator:** Jean-Louis VIRETTI
- **Published:** 2026-09-03 (based on LinkedIn’s public relative 16-hour timestamp at verification).
- **Original source:** [Jean-Louis VIRETTI’s LinkedIn creator post with the attached video and workflow breakdown](https://fr.linkedin.com/posts/jean-louis-viretti-112698131_ia-hermesagent-openai-activity-7500919484896079872-Y4MU)
- **Model attribution:** VIRETTI explicitly says the central cinematic shot was generated with **FLUX 3 via FAL.ai**.
- **Summary:** A fictional portrait of “Chiara” is animated into a restrained 10-second cinematic loft shot, then used as the centerpiece of a polished 16-second vertical premium-ad capsule with branded opening/closing slides, French narration, original music, and final delivery QA.
- **Workflow/details:** Start from one 9:16 `gpt-image-2` portrait → generate a 10-second FLUX 3 shot on fal.ai → assemble a 16-second edit with 0–3s opening slide, 3–13s FLUX 3 video, and 13–16s closing slide → add French narration with Gemini Flash TTS Zephyr and an original 120 BPM electro-organic bed → export/QC at 1080×1920, 24 fps, H.264 video and AAC stereo audio. VIRETTI says the complete agentic chain ran through Hermes Agent v0.20.4 in about 55 minutes and that he did not intervene in the process.
- **Prompt provenance:** `not_provided` — the first-party post does not expose the exact FLUX 3 generation prompt; the separately visible French narration script is not treated as a video-generation prompt.
- **Why included:** Fresh primary creator source with an attached video, explicit FLUX 3/fal.ai attribution, unusually concrete end-to-end production telemetry, and a reproducible one-portrait-to-finished-ad workflow. The example is useful beyond a demo clip because it documents how a generated shot survives art direction, voice, music, edit timing, delivery codecs, and QA inside an automated production chain.

### 187. Six-basic-emotions performance benchmark across eight video models — Tianyu Xu

- **Creator:** [Tianyu Xu](https://www.linkedin.com/in/tianyuxu/)
- **Published:** 2026-09-03 (based on LinkedIn’s public relative 15-hour timestamp at verification on 2026-09-04).
- **Original source:** [Tianyu Xu’s LinkedIn six-emotion comparison](https://www.linkedin.com/posts/tianyuxu_the-6-basic-emotions-in-15-seconds-seedance-activity-7500875545929383950-pI3q)
- **Model attribution:** Xu explicitly lists **FLUX 3** among the eight video models in his own 15-second comparison, alongside Seedance 2.5, Gemini Omni 1.1 Flash, WAN 3, MiniMax H3, Seedance 2.0, Seedance 2.0 Mini, and Kling 3.
- **Summary:** A 15-second performance benchmark compares current video models across six basic emotions in sequence—surprise, fear, sadness, anger, disgust, and happiness—making expression quality, transition control, and overacting directly comparable.
- **Workflow/details:** The post fixes the evaluation concept to the same six-emotion sequence and reports Xu’s qualitative observation that all tested models have strengths while some overact; discussion on the original post focuses on subtle versus exaggerated facial performance. Exact prompt wording, source/reference media, provider settings, resolution, seed, audio setup, and any model-specific adaptation are not publicly disclosed, so none are inferred.
- **Prompt provenance:** `not_provided` — the visible emotion sequence and comparison caption describe the benchmark but are not labeled as the exact generation prompt.
- **Why included:** Fresh primary creator source with explicit FLUX 3 attribution and a clear 15-second cross-model video-performance target. Six consecutive affect changes are a high-signal facial-animation stress test because the model must preserve one performance while making each emotion readable without collapsing into exaggerated or unstable expression.

### 188. Five-second adaptive-reuse courtyard camera-motion demo — RunDiffusion

- **Creator:** [Adam Stewart / RunDiffusion](https://learn.rundiffusion.com/flux-3-video-tools/)
- **Published:** 2026-09-04
- **Original source:** [Flux 3 Video Tools Are Now Available on RunDiffusion](https://learn.rundiffusion.com/flux-3-video-tools/)
- **Model attribution:** RunDiffusion explicitly identifies the embedded clip as a **Flux 3 Video** example on its first-party launch page for FLUX 3 video tools.
- **Summary:** A five-second architectural shot makes a restrained forward dolly through an adaptive-reuse headquarters courtyard while keeping motion limited to environmental details such as landscape and water.
- **Workflow/details:** First-party RunDiffusion example. The page states that Flux 3 Video can start from a text prompt, a Start Frame, or paired Start/End Frames; Flux 3 Extend Video continues an existing clip; Draft Video and Draft Extend Video provide faster 720p previews; all four tools support 5–20-second clips with optional native audio, while the full tools support 720p or 1080p output. The showcased embedded video is 5 seconds long.
- **Prompt provenance:** `verbatim_in_post` — “A slow forward dolly through an adaptive-reuse headquarters courtyard, with motion limited to landscape and water.”
- **Why included:** Fresh first-party source with an embedded FLUX 3 output, exact publication date, visible verbatim prompt, and concrete production controls. The restrained architecture shot is a useful quality test because measured camera motion, water/landscape movement, reflections, and geometry retention must remain coherent without relying on spectacle.

### 189. Thirty-four fully directed 20-second films with published prompts and measured structure — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Date not shown; verified 2026-09-06.
- **Original source:** [Finished films — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/finished-films)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`, and the published take metadata identifies the showcased films as FLUX.3 generations.
- **Summary:** A first-party stress-test suite presents 34 returned twenty-second films across thrillers/action, drama/romance, animation/puppets, and period/comedy/documentary, testing multi-shot structure, multilingual dialogue and subtitles, single-take choreography, timed music and silence, and broadcast-style editing grammar.
- **Workflow/details:** Martini attempted 37 fully directed films and received 34 outputs. Every film is 20.04 seconds, 21:9, 1440×608, 24 fps, and rendered in draft mode. Prompts run 1,973–4,151 characters and specify time-coded shot lists, dialogue, lens choices, lighting, sound beds, second-timed music cues, and grade. The report says 27 of 32 multi-shot briefs returned the requested four-shot structure; its single-take `Service` example registers zero cuts and 480/480 unique frames. Martini says the published takes are straight out of the model, with nothing cut, graded, or retouched.
- **Prompt provenance:** `verbatim_in_post` — all showcased prompts are printed in full. Verified excerpt from `Rain Line`: “A 20-second hand-drawn 2D anime sequence, fully directed. Dialogue in Japanese with English subtitles.”
- **Why included:** An unusually rigorous first-party source combines many attached FLUX.3 outputs with exact prompts, verified dimensions/frame rate, timed shot and audio direction, measured structural outcomes, and explicit no-post-processing provenance, making it highly reproducible and useful for judging narrative control rather than only surface aesthetics.

### 190. Twenty-second no-cut wolf chase with FPV, barrel roll, transformation, and native audio — Yuval Avidani

- **Creator:** [Yuval Avidani (@yuvalav)](https://x.com/yuvalav)
- **Published:** Date not exposed; verified 2026-09-08 (the public creator-profile mirror shows the post as three days old).
- **Original source profile:** [Yuval Avidani on X](https://x.com/yuvalav) — the accessible public index did not expose a stable direct status URL for this post.
- **Secondary verification source:** [Public creator-profile mirror preserving Yuval’s original wording, full prompt, explicit Flux 3 Video attribution, and video-post context](https://www.instalker.org/yuvalav)
- **Model attribution:** Yuval explicitly labels the post “Claude Fable 5.1 + Flux 3 Video” and tags Black Forest Labs `@bfl_ai`.
- **Summary:** A grey wolf sprints through an ice valley under a giant golden moon, transitions into a low FPV chase through an ice tunnel and moonlit pine forest, passes through a 90-degree barrel-roll slow-motion snow helix, whips up a cliff into the clouds, then transforms into molten gold on the rim of the moon as a shockwave writes “YUV AI” across the sky.
- **Workflow/details:** One 20-second, time-coded prompt explicitly asks for one continuous shot with no cuts and continuously forward momentum. Camera language changes from a static frontal approach to a low FPV chase, tunnel passage, 90-degree barrel roll, cliff whip, cloud-top run, and moon reveal. The creator presents the setup as “Claude Fable 5.1 + Flux 3 Video”; the public post does not further separate their roles, so no additional agentic workflow is inferred. The prompt also specifies an audio arc—accelerating paws and wind, silence during the tunnel blink, bass drop, heartbeat during the roll and hold, rising howl, choir swell, one massive final hit, then silence. “8k” appears only inside the prompt as a requested quality term and is not treated as verified output resolution.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Opener, one continuous shot, the camera never cuts, momentum always forward, no speech, RED camera, anamorphic lens, rich natural color. a grey wolf with pale amber eyes and thick winter fur.” The complete 0–20 second prompt, including the audio plan and final “YUV AI” typography cue, remains visible in the secondary verification source.
- **Why included:** Fresh explicit original-creator Flux 3 Video attribution, an attached-video creator post preserved by a public mirror, and a fully visible highly reproducible time-coded prompt. The sequence is an unusually demanding long-horizon benchmark for fast animal motion, continuous camera choreography, speed ramps, tunnel/cloud transformations, environmental continuity, synchronized native audio, and legible end-card typography without a cut.

### 191. Fifteen-second pterosaur attack on an expedition plane in one found-footage take — DennisVisuals

- **Creator:** [DennisVisuals (@DtheW1995)](https://x.com/DtheW1995)
- **Published:** 2026-09-05
- **Original post:** [View on X](https://x.com/DtheW1995/status/2096144016089780321)
- **Secondary verification source:** [Public creator-post mirror preserving the original post, full prompt, attached-video context, and same-thread Flux 3 attribution](https://jilbab.twstalker.com/DtheW1995/status/2096144016089780321)
- **Model attribution:** DennisVisuals follows the exact video/prompt post in the same creator thread with “Made with Flux 3.”
- **Summary:** A handheld passenger camera inside a low-flying twin-engine expedition aircraft over a misty tropical jungle records multiple pterosaurs attacking the plane: one slams the wing, another grabs the wing strut, the largest repeatedly strikes and finally breaks a side window, and the damaged aircraft drops toward the treetops before an abrupt cut.
- **Workflow/details:** One continuous 15-second found-footage take from inside the aircraft, with no external camera angles. The prompt is time-coded into five action beats (0–2s, 2–5s, 5–8s, 8–11s, 11–15s) and explicitly coordinates turbulence-driven handheld shake, propeller wash, aircraft banking, cabin inertia, progressive window cracking and breakage, wind-driven papers/clothing, warning alarms, pilot dialogue, engine/wind/metal-impact audio, and negative constraints against smooth stabilization, teleportation, impossible camera movement, duplicated creatures, excessive gore, and cartoon/cheap-CGI appearance. Resolution, seed, reference media, provider, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “Ultra-realistic 15-second found-footage sequence filmed from inside a small, low-flying twin-engine expedition aircraft above a misty tropical jungle.” The complete five-beat prompt remains visible in the secondary verification source.
- **Why included:** Fresh explicit original-creator Flux 3 attribution, attached-video verification, and a fully visible highly reproducible prompt. The sequence is a difficult single-take benchmark for fast creature motion, aircraft aerodynamics, camera/body inertia, progressive physical damage, cabin-object causality, native sound, and viewpoint continuity under violent motion.

### 192. Viral frog-woman smartphone-realism test with unusually candid micro-expressions — Bennett Waisbren

- **Creator:** [Bennett Waisbren (@BennettWaisbren)](https://x.com/BennettWaisbren)
- **Published:** 2026-09-08.
- **Original source:** [Bennett Waisbren’s X creator post](https://x.com/BennettWaisbren/status/2097448865150775623)
- **First-party workflow verification:** [Bennett Waisbren’s Patreon post](https://www.patreon.com/BennettWaisbren/posts/658-637-views-in-168984946)
- **Model attribution:** Waisbren says in the original X post that **Flux 3** “came out ahead” for this piece, and in his first-party breakdown says he tested the concept in Seedance before trying **Flux 3** and selecting the Flux render.
- **Summary:** A creepy human-animal “frog woman” hybrid is staged as an impossible creature found beside a pond, picked up, and casually filmed on an old phone. Waisbren chose the Flux 3 take because tiny facial expressions, twitches, and attitude changes made the performance feel observed rather than rigidly directed.
- **Workflow/details:** The creator first tested the idea in Seedance, which he describes as the more reliable tool in his current workflow, then tried Flux 3 and selected a Flux result for its candid smartphone realism and micro-expression behavior. His public first-party excerpt reports 658,637 combined Instagram/Facebook views in five hours and 57 minutes. The exact image-generation stages, Flux 3 prompt, settings, and final selection details are present only in the locked portion of the Patreon post and are therefore deliberately excluded.
- **Prompt provenance:** `mentioned_not_in_post` — the creator states that the complete Flux 3 prompt and settings are in the locked portion of his first-party Patreon post. Because those details are paywalled, they are not copied, reconstructed, or inferred here.
- **Why included:** A fresh primary-source Flux 3 example with a public video post plus a traceable first-party explanation of why the render won a real creator-side A/B test. It targets a difficult realism regime—an uncanny human-animal subject, subtle facial micro-performance, casual handheld-phone plausibility, and found-footage immediacy—and pairs that qualitative evidence with an unusually strong early audience signal.

### 193. Four-model same-reference product benchmark with human-lifestyle rank flip — Lisa Anugwom Narh

- **Creator:** [Lisa Anugwom Narh, MSML](https://www.linkedin.com/in/lisanarh)
- **Published:** 2026-09-08 (based on LinkedIn’s public relative two-day timestamp at verification).
- **Original source:** [Lisa Anugwom Narh’s LinkedIn creator post linking the full comparison video](https://www.linkedin.com/posts/lisanarh_i-tested-4-ai-video-models-the-winner-changed-activity-7500712963683561472-jdh8)
- **Model attribution:** Narh explicitly lists **Flux 3** as one of the four tested video models, alongside Seedance 2.5, Grok Imagine 1.5, and Wan 2.7, in the original creator post for the linked video.
- **Summary:** A controlled fictional-product comparison holds the reference image and assignment constant across four current video models, then adds a human lifestyle sequence and observes that the ranking changes, making the FLUX 3 output part of a production-oriented benchmark rather than an isolated showcase.
- **Workflow/details:** Same fictional product, same reference image, same assignment. Narh tracks prompt accuracy, visual quality, product consistency, motion, human intervention, and credit cost. She says the experiment ran inside OpenArt, HeyGen was used in the production workflow, and additional AI-assisted editing was incorporated into the finished piece. The full linked video documents the actual generations, scores, credit costs, and the point where adding a human lifestyle sequence changes the model ranking. No model-specific seed, resolution, settings, or exact per-model generation parameters are publicly visible in the verified LinkedIn post, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — the creator explicitly says the models received the same creative assignment and reference setup, but the exact shared prompt wording is not visible in the verified public LinkedIn source and has not been reconstructed.
- **Why included:** Fresh primary creator source linking the full video, explicit Flux 3 attribution, controlled same-input methodology, actual model generations, and production-relevant evaluation dimensions including consistency, motion, human intervention, and credit cost. The human-sequence rank flip is especially useful because it shows model choice can depend on shot type rather than supporting a generic “best model” claim.

### 194. Same-prompt six-model TV-studio motion benchmark — NoMa Studio AI

- **Creator:** [NoMa Studio AI](https://es.linkedin.com/posts/nomastudioai_ia-aivideo-seedance-activity-7502833669741654016-oU4D)
- **Published:** Date not exposed; verified 2026-09-10 (LinkedIn’s public index shows a relative one-day timestamp).
- **Original source:** [NoMa Studio AI’s LinkedIn creator post with the attached six-model comparison](https://es.linkedin.com/posts/nomastudioai_ia-aivideo-seedance-activity-7502833669741654016-oU4D)
- **Model attribution:** NoMa explicitly pairs `FLUX` with `FLUX 3 Video` in the six-model benchmark and publishes FLUX-specific settings and results.
- **Summary:** Six image/video model families receive the same TV-studio motion brief. FLUX 3 preserves texture and illuminated typography especially well but returns an almost static shot rather than the requested dolly/subject movement, making this a controlled failure-analysis benchmark rather than a cherry-picked showcase.
- **Workflow/details:** One prompt is reused word-for-word across all six families; each video model runs at its lowest offered resolution and maximum duration. For FLUX 3 Video, NoMa reports 720p for 20 seconds. The common brief tests a hand sweep, step-forward and head turn, a slow dolly-in, sequin/tulle motion, stable mirror reflection and background lettering, exactly one microphone, plus room-tone/heel ambience.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “She sweeps her open raised hand across her body, lowers it, steps forward once and turns her head to the lens…” The full 466-character prompt remains visible in the creator’s first comment.
- **Why included:** Newly published primary-source comparison with attached media, explicit FLUX 3 attribution, exact per-model settings, and a controlled identical-prompt methodology. It is especially useful because it documents both a concrete FLUX 3 strength—texture/text stability—and a concrete failure mode—camera and subject-motion compliance—under matched inputs.

### 195. Twenty-second FPV Arabian-horse shamshir chase with continuous camera choreography — Mohammed Magdy Alzahran

- **Creator:** Mohammed Magdy Alzahran (@Malzahran2)
- **Published:** Date not exposed; verified 2026-09-10 (LinkedIn’s public index showed a relative one-week timestamp).
- **Original source:** [Mohammed Magdy Alzahran’s LinkedIn creator post](https://www.linkedin.com/posts/malzahran_flux3-activity-7496603243737759744-hne2)
- **Secondary verification source:** [Flux3 public prompt gallery preserving the creator attribution and prompt](https://flux3.co.kr/en/video-prompts)
- **Model attribution:** Alzahran explicitly tags the attached generation `#Flux3` and writes `#Flux3 on Runway` in the original creator post.
- **Summary:** A 20-second desert action sequence runs beside a galloping Arabian horse at hyperspeed FPV pace, transitions into a slow orbit as the rider draws a curved shamshir mid-stride, then mixes hoof-level tracking, sand plumes, whip-pans, Dutch angles, hard sun flare, and aggressive focal shifts without abandoning the continuous-action premise.
- **Workflow/details:** The visible brief specifies a 20-second continuous sequence, FPV parallel tracking, a transition into slow orbital camera movement, extreme low-angle hoof-impact coverage, slow-motion sand physics, handheld whip-pans during the sword raise, Dutch angles on the horse turn, harsh midday anamorphic flare, an amber-dune/deep-teal-shadow grade, high contrast, and focal shifts between mane and horizon. The creator identifies Runway as the generation surface. Resolution, seed, reference media, audio settings, and post-production are not publicly disclosed, so none are inferred.
- **Prompt provenance:** `verbatim_in_post` — verified visible excerpt: “20-second continuous sequence. Hyperspeed FPV parallels a galloping Arabian horse transitioning into a slow orbital…” The complete prompt remains publicly visible in the original creator post; no wording has been reconstructed from the video.
- **Why included:** Fresh primary creator source with explicit FLUX 3 attribution, an attached generation, a directly visible reusable prompt, and unusually dense camera choreography. Sustaining horse-and-rider anatomy, blade handling, hoof impacts, sand physics, speed changes, orbiting camera geometry, and focal transitions in one 20-second action passage makes it a strong motion-and-continuity benchmark.

### 196. Twenty-second reactive 3D decision-tree cube world in one continuous orbit — Umesh

- **Creator:** [Umesh (@umesh_ai)](https://x.com/umesh_ai)
- **Published:** 2026-09-11
- **Original post:** [View on X](https://x.com/umesh_ai/status/2097920399078264833)
- **Prompt source:** [Creator’s prompt reply on X](https://x.com/umesh_ai/status/2097920401867489707)
- **Secondary verification source:** [Public creator-profile mirror preserving the original wording and full prompt thread](https://site.twstalker.com/umesh_ai)
- **Model attribution:** Umesh explicitly writes “Generated using Flux 3 on Runway” and labels the workflow `Prompt (I2V)`.
- **Summary:** A man traverses a minimalist sage-green void of floating ivory cubes; every footstep causally spawns new cube pathways along distinct three-dimensional axes until the frame becomes an expanding architectural decision tree.
- **Workflow/details:** Image-to-video on Runway. The prompt time-codes a full 20-second sequence (0–4s, 4–9s, 9–15s, 15–20s), requires one continuous shot with no cuts, and directs a slow orbit with subtle elevation changes. Visual controls include a muted sage-green/ivory palette, soft volumetric light, long shadows, film grain, realistic movement, smooth cube animation, a 35mm lens, and an Escher-inspired spatial illusion. Resolution, seed, audio settings, and post-production are not disclosed.
- **Prompt provenance:** `verbatim_in_post` — “A lone man moves through a minimalist sage-green void populated by soft-edged ivory cubes. Every cube he steps on generates a new set of cube pathways that extend into completely different directions in three-dimensional space.” The complete time-coded prompt remains visible in the creator’s prompt reply and public verification mirror.
- **Why included:** Fresh primary-source FLUX 3 attribution plus a directly visible reusable prompt. Requiring every footstep to trigger new geometry on a different 3D axis while a continuously orbiting/elevating camera preserves human motion, object permanence, depth, and causality makes this a strong long-horizon spatial-control benchmark.

### 197. Official FLUX 3 prompt-based video-edit showcase with surgical object, text, dialogue, and event changes — Black Forest Labs

- **Creator:** [Black Forest Labs (@bfl_ai)](https://x.com/bfl_ai)
- **Published:** 2026-09-11
- **Original source:** [FLUX Video Edit first-party showcase](https://bfl.ai/video-edit)
- **Official announcement:** [Black Forest Labs on LinkedIn](https://ir.linkedin.com/company/bflai) — the public company page preserves the fresh launch update, though the index does not expose a stable direct activity permalink.
- **Model attribution:** Black Forest Labs’ official announcement explicitly says “FLUX 3 Video now has fast, precise editing.” The linked first-party product page documents FLUX Video Edit as a separate editing tool built on the same FLUX model family.
- **Summary:** BFL’s interactive before/after showcase edits one source video through targeted instructions: replacing fish with lobsters, changing an apron color, adding a seagull, rewriting crate text, adding snow, removing a bucket, replacing a character or setting, restyling the footage, changing or translating dialogue with lip-sync, and altering the action while leaving unmentioned shot details intact.
- **Workflow/details:** Prompt-based video-to-video editing through `/v1/flux-tools/video-edit-v1`. The first-party page documents MP4 inputs up to 15 seconds / 50 MiB, 1–4096-character prompts, output at the source clip’s length and aspect ratio, 24 fps, and up to 720p. Source audio is preserved unless the prompt changes it; dialogue can be rewritten or translated with synchronized lips. BFL reports roughly 50 seconds for a 10-second edit and pricing of $0.03 per output second. The same tool supports localized object/character edits, background replacement, in-scene text changes, colors/materials/effects, restyling, event changes, and stacked or sequential edits.
- **Prompt provenance:** `verbatim_in_post` — “Replace the mackerel with lobsters.” Additional short edit prompts are also visibly published in the first-party showcase.
- **Why included:** Newly published first-party BFL source with explicit FLUX 3 attribution, embedded source/edited video comparisons, exact prompt-to-output examples, and unusually concrete API constraints, latency, and price. It is a high-signal temporal-consistency benchmark because the edit must change only the requested object, text, dialogue, setting, or event while preserving the surrounding motion, framing, timing, and untouched scene content.

### 198. Fifteen-second same-prompt four-model T2V benchmark at 1080p — MayorkingAI

- **Creator:** [MayorkingAI (@MayorKingAI)](https://x.com/MayorKingAI)
- **Published:** 2026-09-10
- **Original post:** [View on X](https://x.com/MayorKingAI/status/2097733280540115187)
- **Secondary verification source:** [Public creator-profile mirror preserving the original post and follow-up](https://w.twstalker.com/MayorKingAI)
- **Model attribution:** MayorkingAI explicitly lists **Flux 3 1080p** as one of the four generated video outputs in the original comparison post.
- **Summary:** A controlled text-to-video benchmark runs one shared prompt through Seedance 2.5, MiniMax H3, Flux 3, and Wan 3.0 Prime, producing 15-second clips for side-by-side evaluation.
- **Workflow/details:** Text-to-video; same prompt across all four models; 15-second outputs; Seedance 2.5 at 1080p, MiniMax H3 at 2K, Flux 3 at 1080p, and Wan 3.0 Prime at 1080p; all generated in Magnific. In a public follow-up, the creator says he prefers Flux 3. No model-specific seed, aspect ratio, audio settings, or post-processing are disclosed, so none are inferred.
- **Prompt provenance:** `mentioned_not_in_post` — the creator explicitly says all four generations use the same prompt, but the prompt text is not visible in the verified public source and has not been reconstructed.
- **Why included:** Fresh primary creator source with an attached four-model comparison, explicit Flux 3 attribution, a controlled same-prompt and same-duration methodology, verified output resolutions, and a creator-side quality preference for Flux 3. It is useful as a practical cross-model benchmark rather than a standalone cherry-picked showcase.

### 199. First-party FLUX 3 Video Edit integration with exact prompt and output — fal

- **Creator:** [fal (@fal)](https://x.com/fal)
- **Published:** 2026-09-11
- **Original post:** [View on X](https://x.com/fal/status/2098086929875026391)
- **First-party model example:** [fal FLUX 3 Edit Video endpoint](https://fal.ai/models/blackforestlabs/flux-3/edit-video)
- **Model attribution:** fal explicitly announces “FLUX 3 Video Edit is now live on fal”; its first-party endpoint identifies `blackforestlabs/flux-3/edit-video` as Black Forest Labs’ FLUX.3 video model.
- **Summary:** fal’s launch demo presents one-prompt video editing for character swaps, background rebuilds, restyling, dialogue rewrites/translations with matching lip-sync, color/material/effect changes, and event changes. The linked model page also publishes a separate prompt-to-output edit example.
- **Workflow/details:** Video-to-video on fal using a natural-language prompt plus a source video. The public endpoint accepts MP4, MOV, WebM, M4V, and GIF inputs or a video URL. The displayed first-party example returns seed `3972454174` and a directly downloadable MP4; fal lists pricing at $0.03 per generated second for 720p output.
- **Prompt provenance:** `verbatim_in_post` — “Replace sushi with a meat” appears exactly as written on fal’s first-party model page.
- **Why included:** Fresh first-party platform launch with an attached announcement video, explicit FLUX 3 attribution, an exact prompt, an actual output file, and reproducible endpoint/input/pricing details. It is distinct from the BFL #197 showcase because fal publishes a different prompt/output pair for its own newly launched integration rather than reusing the mackerel-to-lobsters example.

### 200. Ten-second two-stage dragon-and-background FLUX 3 Video Edit — DΞV

- **Creator:** [DΞV (@junwatu)](https://x.com/junwatu)
- **Published:** 2026-09-11
- **Original post:** [View on X](https://x.com/junwatu/status/2098201196087685377)
- **Secondary verification source:** [Public creator-profile mirror preserving the original wording, attached tweet video, exact prompt, cost, and quoted BFL launch context](https://www.sotwe.com/junwatu?lang=en)
- **Model attribution:** DΞV calls the test “Flux Video Edit” while directly quoting Black Forest Labs’ launch post that explicitly identifies the tool as **FLUX 3 Video**; the creator test is therefore traceably tied to FLUX 3 Video Edit without inferring model attribution from the footage itself.
- **Summary:** One existing dragon clip is edited in two temporally distinct stages: the dragon becomes bright blue for the first five seconds, then the background changes to a city scene for the last five seconds.
- **Workflow/details:** Prompt-guided video-to-video edit; 10-second source/output; one natural-language instruction drives two time-scoped changes. DΞV reports the run cost **$0.33**. No verified resolution, seed, source-generation details, provider endpoint, or post-production are publicly disclosed, so none are inferred.
- **Prompt provenance:** `verbatim_in_post` — “Change the dragon into a bright blue dragon for the first 5 seconds, then change the background to a city scene for the last 5 seconds.”
- **Why included:** Fresh original-creator post with an attached video, traceable FLUX 3 attribution through the quoted Black Forest Labs first-party launch, an exact reproducible prompt, and concrete duration/cost telemetry. It is a high-signal temporal-editing test because one prompt asks the model to apply two different edits to separate halves of the same clip while preserving the underlying motion over time.

### 201. Surgical denim-jacket recolor with motion-preserving source/output pair — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] editing guide with paired source/edited video and request code](https://runware.ai/docs/models/bfl-flux-video-edit-fast/guides/editing-video)
- **Supporting first-party model source:** [Runware FLUX Video Edit [fast] model page](https://runware.ai/docs/models/bfl-flux-video-edit-fast)
- **Model attribution:** Runware identifies the tool as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly identifies this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** A studio fashion clip is edited with one five-word instruction that changes a denim jacket to deep burgundy while preserving the woman’s hair, white top, gray backdrop, floor shadow, turn speed, and the exact moment she settles.
- **Workflow/details:** Video-to-video from one source clip plus `positivePrompt`, with no mask, keyframe, or extra reference required. The source supplies duration, aspect ratio, and audio; output is normalized to 24 fps and capped at 720p, with clips up to 15 seconds. Runware lists $0.03 per output second and about 51 seconds per request, and exposes the returned output-video URL in the example response.
- **Prompt provenance:** `verbatim_in_post` — “Make the denim jacket deep burgundy.”
- **Why included:** Newly published first-party Runware integration with an actual source/edited pair, exact prompt, model ID, request/response code, price, and output constraints. It is a clean temporal-consistency test because the model must make one local color edit while leaving motion, timing, framing, lighting, subject details, and untouched scene content intact; it is distinct from the existing BFL, fal, and DΞV edit entries because Runware publishes its own separate prompt/output pair and API example.

### 202. Dialogue rewrite and lip-synced returns-policy edit — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] dialogue, on-screen text and localization guide with paired source/edited videos and request code](https://runware.ai/docs/models/bfl-flux-video-edit-fast/guides/dialogue-and-localization)
- **Model attribution:** Runware identifies the model as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly identifies this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** A presenter’s existing sixty-day returns-policy take is rewritten to ninety days with free postage. The spoken sentence and mouth motion change while the same gesture, framing, room, voice, pauses, and settle timing are retained; the same first-party guide also demonstrates dialogue translation and in-scene text localization.
- **Workflow/details:** Video-to-video from one source clip plus `positivePrompt`; the documented request exposes the source MP4 and returned edited MP4. The replacement line must fit the original speech timing because the model does not extend the clip. Runware documents source clips up to 15 seconds, output at 24 fps and up to 720p while retaining source duration and aspect ratio, with unmentioned motion, camera work, timing, framing, and audio preserved.
- **Prompt provenance:** `verbatim_in_post` — `Make her say "Our returns window is now ninety days, and postage is free."`
- **Why included:** Newly published first-party source with paired before/after videos, an exact prompt, model ID, request/response code, and directly linked source/output files. It is a demanding temporal-editing benchmark because speech and lip-sync must change while body timing and shot continuity remain fixed, and it adds a localization/dialogue-editing use case materially distinct from the jacket-recolor example already catalogued.

### 203. Rotating sneaker material swap with preserved lighting and contact shadow — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] replacement/addition guide with source/output videos and request code](https://runware.ai/docs/models/bfl-flux-video-edit-fast/guides/replacing-and-adding)
- **Model attribution:** Runware identifies the endpoint as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** A rotating white-leather sneaker is changed to tan suede while the gum-rubber sole, turntable motion, key light, and contact shadow stay fixed, turning one packshot into a materially different colorway without reshooting it.
- **Workflow/details:** Video-to-video from one source clip plus `positivePrompt`, with no mask or image/style reference. Runware recommends naming material rather than color alone and explicitly preserving parts inside the replaced object; the same guide publishes tan-suede, navy-canvas, and olive-nubuck variants. Source clips can be up to 15 seconds, with output at 24 fps and up to 720p while retaining source duration and aspect ratio. The code example exposes both a source MP4 and returned edited MP4.
- **Prompt provenance:** `verbatim_in_post` — “Change the white leather upper to tan suede, and keep the gum rubber sole.”
- **Why included:** Newly published first-party source with an actual source/output pair, exact prompt, model ID, and working request example. It is a clean temporal/material-consistency benchmark because the model must change surface reflectance and texture while preserving the rotation, lighting direction, contact shadow, sole geometry, framing, and timing; it is materially distinct from the existing Runware jacket-recolor and dialogue-edit entries.

### 204. Midday-to-golden-hour relighting with preserved camera and scene geometry — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] changing-the-setting guide with paired source/edited video and request code](https://runware.ai/docs/models/bfl-flux-video-edit-fast/guides/changing-the-setting)
- **Model attribution:** Runware identifies the endpoint as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** An interior shot is relit from midday to golden hour: low warm sunlight rakes through the window and long soft shadows appear across the floor while the sofa and camera geometry remain unchanged.
- **Workflow/details:** Video-to-video from one source clip plus `positivePrompt`. The guide shows a direct “Midday” → “Golden hour” source/output pair and explains that setting edits can relight a clip, change season, or swap the background while preserving unmentioned subject motion, camera work, timing, framing, and audio. Runware documents source clips up to 15 seconds and output at 24 fps and up to 720p while retaining source duration and aspect ratio.
- **Prompt provenance:** `verbatim_in_post` — “Make it golden hour, with low warm sunlight raking through the window and long soft shadows across the floor.”
- **Why included:** Newly published first-party source with a paired before/after result, exact prompt, model ID, and working request/response code. It is a clean temporal-consistency benchmark for changing global illumination and environmental state without disturbing the sofa/camera geometry, motion, framing, or timing, and is materially distinct from the jacket-recolor, dialogue-rewrite, and sneaker-material edits already catalogued.

### 205. Multi-object kitchen-counter removal with background reconstruction — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] removing-objects guide with paired source/edited videos and request code](https://runware.ai/docs/models/bfl-flux-video-edit-fast/guides/removing-objects)
- **Model attribution:** Runware identifies the endpoint as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** A moving kitchen shot removes a stainless dish rack, yellow spray bottle, and open cereal box from the counter while reconstructing the pale quartz surface and marble backsplash and leaving the chrome faucet, sink, lemons, eucalyptus, cookbooks, and small jar untouched.
- **Workflow/details:** Video-to-video from one source clip plus `positivePrompt`, with no mask. The guide publishes a direct source-to-cleared pair and explains that removal prompts should name both the target and the surface that continues behind it so the fill remains stable across frames. It also demonstrates static-object and moving-person removals, explicit whole-clip temporal scope, and working request code with a returned edited-video URL. Runware documents source clips up to 15 seconds, output normalized to 24 fps and capped at 720p while retaining source duration and aspect ratio.
- **Prompt provenance:** `verbatim_in_post` — “Remove three things from the counter: the stainless dish rack holding plates, the yellow plastic spray bottle, and the open cardboard cereal box.” The complete prompt remains visible in the first-party source.
- **Why included:** Newly published first-party source with an actual before/after video pair, exact prompt excerpt, model ID, working request/response example, and explicit background-reconstruction guidance. It is a strong temporal-consistency benchmark because three foreground objects must disappear while a moving shot preserves camera motion, daylight, surrounding props, surface geometry, and stable fill across every frame; it adds a removal/reconstruction use case distinct from the recolor, dialogue, material-swap, and relighting edits already catalogued.

### 206. Whole-frame style transfer with preserved performance and camera motion — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] restyling guide with source/output videos and request code](https://runware.ai/docs/models/bfl-flux-video-edit-fast/guides/restyling)
- **Model attribution:** Runware identifies the endpoint as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** One filmed performance is re-rendered into multiple visual media—flat-vector animation, cel-shaded anime, watercolor, film-stock looks, technical line drawing, and blockout-to-photoreal treatments—while preserving the source shot’s performance timing and camera move.
- **Workflow/details:** Video-to-video from one source clip plus `positivePrompt`. Runware publishes source/output URLs and working request code for a cel-shaded anime restyle, explains that camera path, framing, timing, blocking, gestures, duration, and audio survive the restyle, and recommends naming the medium, its marks, and its palette; flatter hard-edged styles generally remain more stable across frames. The model page documents source clips up to 15 seconds, 24 fps output, and up to 720p while retaining source duration and aspect ratio.
- **Prompt provenance:** `verbatim_in_post` — “Restyle the whole shot as cel-shaded anime, with hard-edged shadow blocks, clean ink linework and desaturated flat backgrounds.” Additional exact vector, watercolor, 16mm, background-replacement, line-drawing, and blockout-to-photoreal prompts are visible in the same first-party guide.
- **Why included:** Newly surfaced first-party source with an actual source/output pair, exact prompt, model ID, working request/response code, multiple controlled style variants, and candid temporal-stability guidance. It adds a whole-frame style-persistence benchmark distinct from the local recolor, dialogue, material-swap, relighting, and object-removal edits already catalogued.

### 207. Subterranean water-infrastructure documentary title sequence with anchored graphics and typography — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] API examples — Municipal Water Documentary Title Sequence](https://runware.ai/docs/models/bfl-flux-video-edit-fast/examples)
- **Model attribution:** Runware identifies the request as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** A daylight treatment-plant walking shot is transformed into a night-time subterranean brutalist reservoir while preserving the engineer, walking pace, machinery, continuous camera move, timing, and natural audio; cyanotype-style infrastructure diagrams are surface-anchored to the concrete and a mineral-deposit title resolves on the far wall.
- **Workflow/details:** Video-to-video from one source MP4 plus `positivePrompt`. The first-party example exposes the exact source file, exact edited MP4, API request, task UUID, and a reported cost of `$0.1813`. The prompt explicitly stages a nearly black opening, passing maintenance lights, progressively stronger cyan reflections, temporally consistent mist/ripples/reflections, surface-bound engineering projections, and a final correctly spelled `BENEATH THE CITY` / `A DOCUMENTARY SERIES` environmental title while retaining source motion and audio.
- **Prompt provenance:** `verbatim_in_post` — “Transform this source clip into a tense prestige-documentary title sequence about the vast water infrastructure hidden beneath a city. Preserve the original continuous camera move, the engineer's identity, walking pace, body motion, rotating machinery, framing, timing and natural audio.” The complete prompt remains visible in the first-party API example.
- **Why included:** Newly surfaced first-party source/output pair with an exact prompt, model ID, cost, direct files, and working API request. It is a demanding combined benchmark for large-scale environment replacement, subject/action preservation, temporally stable atmosphere/reflections, surface-anchored motion graphics, and legible in-world typography within one continuous shot.

### 208. Temporal widescreen outpainting of a working ceramics studio — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] API examples — Widescreen Ceramic Workshop Outpaint](https://runware.ai/docs/models/bfl-flux-video-edit-fast/examples)
- **Model attribution:** Runware identifies the request as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** A centered portrait clip with dark side mattes is expanded into a full widescreen ceramics workshop while the artisan, cobalt vessel, kiln, smoke, flickering light, camera position, timing, and audio remain untouched in the original center region.
- **Workflow/details:** Video-to-video outpainting from one source MP4 with no separate mask shown in the published request. The first-party example exposes the source and returned MP4, task UUID, code, and `$0.1813` cost. New left/right areas extend the kiln and soot-darkened wall, shelves, pottery, tools, timber bench, and firebricks while the prompt requires smoke, shadows, firelight, reflections, perspective, lens softness, exposure, grain, and palette to continue coherently throughout the moving shot without seams or added camera motion.
- **Prompt provenance:** `verbatim_in_post` — “Outpaint the centered portrait footage across the full widescreen frame, completely replacing both dark side mattes with a natural continuation of the same working ceramics studio.” The complete prompt remains visible in the first-party API example.
- **Why included:** A distinct first-party source/output example that tests genuine temporal outpainting rather than a local replacement: newly synthesized side regions must stay geometrically, optically, and photometrically coherent with the moving central footage while smoke, reflections, and flickering light propagate seamlessly over time.

### 209. Archival lighthouse restoration and historically restrained colorization — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] API examples — Lighthouse Archive Film Restoration](https://runware.ai/docs/models/bfl-flux-video-edit-fast/examples)
- **Model attribution:** Runware identifies the request as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** Damaged archival lighthouse footage is cleaned of dust, hairs, scratches, chemical blotches, torn-edge artifacts, jitter, gate weave, and exposure flicker, then given restrained period-plausible color while preserving the keeper’s hand-cranking action, rotating Fresnel lens, ocean motion, framing, timing, and audio.
- **Workflow/details:** Video-to-video restoration from a published source MP4. The API example provides request code, the returned MP4, task UUID, and `$0.1813` cost. The prompt asks emulsion-damaged regions to be rebuilt with temporally stable detail, recovers contrast without a digitally sharpened look, applies specific brass/glass/iron/uniform/leather/sea colors, retains authentic fine 16mm grain, and forbids modern objects, invented text, and color pulsing.
- **Prompt provenance:** `verbatim_in_post` — “Restore this damaged archival lighthouse footage for a maritime museum exhibition. Remove dust, hairs, vertical scratches, chemical blotches, torn-edge artifacts, frame jitter, gate weave, and harsh exposure flicker.” The complete restoration/colorization prompt remains visible in the first-party API example.
- **Why included:** Newly surfaced first-party before/after workflow with exact source/output files and a fully public prompt. It is a technically different stress test from object/style edits because defect repair and colorization must remain temporally stable while preserving fine mechanical motion, ocean motion, historical texture, camera geometry, and source audio.

### 210. Persian illuminated-manuscript falconry restyle with preserved flight anatomy — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] API examples — Falconry Exhibition Miniature Reel](https://runware.ai/docs/models/bfl-flux-video-edit-fast/examples)
- **Model attribution:** Runware identifies the request as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly branded this fast, precise editing capability as **FLUX 3 Video**.
- **Summary:** Live-action falconry footage is transformed into an animated Persian illuminated-manuscript miniature while the falconer’s identity/body motion and the hawk’s launch path, wingbeats, anatomy, flight speed, camera movement, framing, timing, and source audio remain fixed.
- **Workflow/details:** Video-to-video restyle from a direct source MP4. The published example exposes the returned MP4, model ID, task UUID, code, and `$0.1813` cost. The prompt specifies opaque mineral pigments and gold leaf on warm ivory paper; lapis, vermilion, turquoise, saffron, decorative gold grasses and cobalt hills; crisp feather silhouettes; subtle paper grain, brush variation, and restrained gold shimmer; and strict temporal constraints against flicker, morphing, duplicated limbs, extra birds, or lettering.
- **Prompt provenance:** `verbatim_in_post` — “Restyle the entire live-action clip as a richly animated Persian illuminated manuscript miniature created with opaque mineral pigments and gold leaf on warm ivory paper.” The complete prompt remains visible in the first-party API example.
- **Why included:** Although it shares the broad restyling category with #206, this is a separate first-party source/output pair with a substantially harder motion target: rapid bird flight and readable wing anatomy must survive a flat historical-painting transformation while subject identity, camera motion, timing, and audio remain unchanged.

### 211. Fifteen-second MiniDV alien-coupon interview with native dialogue — DennisVisuals

- **Creator:** [DennisVisuals (@DtheW1995)](https://x.com/DtheW1995)
- **Published:** 2026-09-12 (based on the public creator-profile mirror’s relative two-day timestamp at verification on 2026-09-14).
- **Original source profile:** [DennisVisuals on X](https://x.com/DtheW1995) — the accessible public index did not expose a stable direct status URL for this post.
- **Secondary verification source:** [Public creator-profile mirror preserving DennisVisuals’ original wording, explicit FLUX 3 prompt label, attached tweet-video marker, and complete visible prompt](https://www.sotwe.com/DtheW1995)
- **Model attribution:** DennisVisuals’ post presents the attached video with a generation prompt explicitly beginning `FLUX 3`, while the same public creator feed also preserves the adjacent creator attribution “Made with Flux 3.”
- **Summary:** A nervous early-2000s TV reporter interviews a biologically believable alien beside its landed spacecraft; after a serious question about why it came to Earth, the alien deadpans that it only wants to redeem a McDonald’s Chicken McNuggets coupon, turning documentary realism into a precisely timed absurdist reveal.
- **Workflow/details:** One continuous 15-second consumer-MiniDV-style take with no cinematic polish. The prompt time-codes four beats, keeps one reporter, one alien, one cameraman, and one spacecraft, and deliberately asks for shoulder-held shake, imperfect zoom, slow autofocus, exposure pumping, washed color, interlaced DV motion, tape noise, wet-field ambience, spacecraft hum, English dialogue, alien-only lip-sync, an awkward coupon close-up, and an authentic tape-style ending. Negative constraints prohibit impossible camera angles, duplicates, morphing, teleportation, cartoon CGI, extra crowds, subtitles, changing props, and other continuity breaks.
- **Prompt provenance:** `verbatim_in_post` — “FLUX 3 — 15-second ultra-realistic early-2000s television documentary footage, filmed on a consumer MiniDV camera by one physically present cameraman.” The complete prompt is publicly visible in the secondary verification source; no wording has been reconstructed from the video.
- **Why included:** Fresh creator-side FLUX 3 attribution, an attached video, and a fully visible highly reproducible prompt. The clip is a strong long-take realism benchmark for reporter/alien/spacecraft identity, prop continuity, dry comic timing, consumer-camera imperfections, English speech and lip-sync, subtle creature breathing/blinking, environmental audio, and a single reachable handheld viewpoint.

### 212. Multi-pedestrian removal plus localized pigeon insertion around a fountain — Black Forest Labs

- **Creator:** [Black Forest Labs](https://bfl.ai/)
- **Published:** Date not shown; verified 2026-09-14.
- **Original source:** [Black Forest Labs FLUX 3 video prompting overview](https://docs.bfl.ai/guides/prompting_video_overview)
- **Model attribution:** Black Forest Labs’ first-party FLUX 3 video prompting guide presents the clip as a FLUX Video Edit example; BFL’s official launch announcement explicitly states that **FLUX 3 Video** now has fast, precise editing.
- **Summary:** An existing fountain shot is edited so all pedestrians disappear and a flock of pigeons appears around the fountain, while unmentioned source details are intended to remain as filmed.
- **Workflow/details:** Video-to-video FLUX Video Edit from one source clip plus one natural-language instruction. BFL says to send the source clip as `video` and the instruction as `prompt`; its first-party tool documentation says everything the prompt does not mention stays as shot, including length, framing, camera, timing, and audio. The endpoint supports MP4 inputs up to 15 seconds / 50 MiB and returns 24 fps output up to 720p.
- **Prompt provenance:** `verbatim_in_post` — “Remove all the pedestrians and add a flock of pigeons around the fountain.”
- **Why included:** Fresh first-party BFL documentation with an explicit edited clip and an exact reproducible prompt. It combines removal of multiple moving people, temporal background reconstruction, and localized insertion of a new flock in one instruction while preserving the rest of the shot; the exact source URL and prompt were not already present in the README.

### 213. Human-animation reference to anime restyle with facial-motion preservation — Justine Moore

- **Creator:** [Justine Moore (@venturetwins)](https://x.com/venturetwins)
- **Published:** 2026-09-11
- **Original source profile:** [Justine Moore on X](https://x.com/venturetwins) — the accessible public search index did not expose a stable direct status URL for this post.
- **Secondary verification source:** [Communeify AI Daily, directly quoting the original creator post and preserving the attached-video marker](https://www.communeify.com/ja/blog/ai-daily-2026-09-12/)
- **Model attribution:** Moore explicitly says **“FLUX 3 Edit”** and states that the attached result was produced from a human animation reference.
- **Summary:** A human-animation reference from *KPop Demon Hunters* is restyled into anime while preserving the source performance’s facial detail and motion, turning the clip into a direct test of motion-conditioned stylization rather than unconstrained generation.
- **Workflow/details:** Video-to-video edit: use the original human animation as the motion/reference clip and instruct FLUX 3 Edit to turn it into anime. Moore specifically frames facial detail and motion retention as the failure mode she has seen in other models; no duration, resolution, seed, provider, or further edit settings are publicly verified in the preserved source.
- **Prompt provenance:** `mentioned_not_in_post` — the creator says she asked the model to turn the reference into anime, but the verified source does not present an exact prompt block or quote, so no verbatim prompt has been reconstructed.
- **Why included:** Newly published original-creator test with explicit FLUX 3 attribution and an attached video, preserved by a credible secondary source that directly quotes the post. It is a focused animation-pipeline benchmark for retaining facial performance and body motion through a strong style transformation, materially distinct from the local object/color/relighting edits already catalogued.

### 214. FHD snowy-forest fox and rain-soaked street-musician native-audio demos — Pixazo API

- **Creator:** [Deepak Joshi / Pixazo API](https://www.pixazo.ai/)
- **Published:** Publication date not shown; first-party page last updated 2026-09-08.
- **Original source:** [Pixazo API FLUX 3 launch guide with embedded generated clips](https://www.pixazo.ai/blog/introducing-flux-3-api-on-pixazo-api)
- **Model attribution:** Pixazo explicitly identifies the page and every embedded showcase clip as generated with the Black Forest Labs Flux 3 API from a text prompt alone, with sound generated together with the video.
- **Summary:** Two distinct embedded FHD examples show a lone fox moving through a snowy forest at golden hour under a slow tracking camera, and a street musician performing beneath a rain-soaked streetlight while music, rain, and reflections stay part of the same generated moment.
- **Workflow/details:** Text-to-video on Pixazo API; both accepted showcase clips are labeled FHD and 24 fps with 10-second timecodes and native generated audio. Pixazo documents FLUX 3 text-to-video, keyframes-to-video, and video-to-video modes, with HD/FHD output and up to 20-second clips. The page’s separate Clip 01 ramen-shop example was not added because that exact prompt/example is already represented in #146.
- **Prompt provenance:** `mentioned_not_in_post` — Pixazo states the fox clip is a one-prompt generation and that every showcased clip comes from text-only prompting, but it does not expose the exact API prompt text for the fox or street-musician renders; their visible descriptions are therefore not presented as verbatim prompts.
- **Why included:** First-party embedded FLUX 3 outputs with explicit attribution, concrete FHD/24 fps/native-audio details, and two materially different quality tests: controlled wildlife/camera motion in snow and coherent night music/rain/reflection ambience. The exact source URL and content are not already present in the README.

### 215. 1920×1088 ceramic-dripper recolor with automatic 720p source normalization — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party platform documentation example.
- **Published:** 2026-09-09
- **Original source:** [Runware FLUX Video Edit [fast] source-video preparation guide with source/output video](https://runware.ai/docs/models/bfl-flux-video-edit-fast/guides/source-video)
- **Model attribution:** Runware identifies the tool as Black Forest Labs’ `bfl:flux@video-edit-fast`; Black Forest Labs’ official launch announcement explicitly identifies this fast, precise video-editing capability as **FLUX 3 Video**.
- **Summary:** A 1920×1088 source clip of a ceramic dripper is edited to a deep matte forest green, while the returned edited video demonstrates the model’s production-resolution behavior by automatically normalizing the high-resolution input to a 720p output envelope.
- **Workflow/details:** Video-to-video from `inputs.video` plus `positivePrompt`; no separate width, height, duration, or resolution control is exposed for this endpoint. Runware documents a hard 0.7–15-second input window, 50 MiB limit, minimum 160×160 input, rejection rather than trimming for clips over 15 seconds, 24 fps output, and automatic downscaling for source footage above 720p while otherwise inheriting source duration/aspect ratio and preserving unmentioned timing/framing/motion/audio.
- **Prompt provenance:** `verbatim_in_post` — “Change the ceramic dripper to a deep matte forest green.”
- **Why included:** Newly published first-party source/output example with an exact visible prompt and unusually useful source-preparation telemetry. It is a practical temporal-editing benchmark because a local color/finish change must remain stable while the pipeline also handles a 1920×1088 source at the documented 720p output boundary; this resolution-normalization behavior is not covered by the existing Runware edit examples.

### 216. Five-language 15-second room scenes with script-format prompting — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-15.
- **Original source:** [Multilingual scenes — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/multilingual)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; all 32 showcased takes are FLUX.3 generations, and the source states that every take is straight out of the model with no cutting, grading, or retouching.
- **Summary:** A systematic multilingual stress test runs eight one-person code-switch clips and twenty-four multi-speaker room scenes, scaling from two through five spoken languages in one generated scene while keeping the videos directly inspectable with their prompts.
- **Workflow/details:** All 32 takes delivered at 21:9, 1440×608. The eight one-person code-switch tests run 10–15 seconds from short 131–232-character prompts; the twenty-four room scenes all run 15 seconds from 680–1,003-character script-style prompts, with six tests each at two, three, four, and five languages. Martini reports that five-language scenes remain viable, that four to six dialogue lines per 15-second room leave enough space for acting, that speaker-label script formatting stages reliably, and that requested subtitles are substantially more reliable than signs, notebooks, or whiteboards.
- **Prompt provenance:** `verbatim_in_post` — visible script/dialogue excerpt: “呢個 take 好啲，but I need more rain, 再嚟一次，action!” The source states that every complete prompt is printed in full.
- **Why included:** Newly surfaced first-party primary-source report with embedded FLUX.3 outputs, exact output dimensions/durations, published prompts, explicit no-post-processing provenance, and a controlled language-count sweep. It is a high-signal native-dialogue benchmark for code-switching, speaker assignment, multilingual turn-taking, subtitle generation, scene staging, and timing rather than a single cherry-picked clip, and its source URL was not already present in the README.

### 217. Quantified multi-keyframe timing and interpolation stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-15.
- **Original source:** [Keyframes — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/keyframes)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; the report publishes direct FLUX.3 takes, exact pinned-frame schedules, and full prompts, and states that every take is straight out of the model with nothing cut, graded, or retouched.
- **Summary:** A controlled keyframe benchmark tests whether FLUX.3 can hit two, three, four, five, or ten pinned images at exact timecodes across 5-, 10-, 15-, and 20-second clips, including loops, hard-cut requests, uneven timing, and metamorphosis.
- **Workflow/details:** Martini analyzes 53 takes and measures 49 of them against exact pin-time frames at 24 fps using normalized grayscale correlation. First and last pins score median 0.96/0.97, while interior pins score 0.61; 44% of interior pins land on the pinned image at the pinned second, 23% are near, and 33% miss. Four pins land 70% of interior targets versus 39% for ten pins. Dense mid/late pin clusters tend to rush the story early, spacing below roughly one second causes cuts rather than interpolation, and the source recommends four or five pins while treating first/last anchors as the most reliable targets.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt from `The Vessel`: “One object lives and dies on a potter's wheel in a single meditative shot.” The complete prompt and ten exact pin times remain visible in the source.
- **Why included:** Newly surfaced first-party FLUX.3 report with embedded outputs, exact timecoded keyframes, visible prompts, reproducible dimensions/durations, quantitative frame-level scoring, and explicit no-post-processing provenance. It is unusually useful for keyframe scheduling and interpolation strategy rather than only visual-quality judging.

### 218. Seventy-take causality, reflection, and counting stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-15.
- **Original source:** [Physics and logic — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/physics-and-logic)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; it publishes 70 direct FLUX.3 takes with prompts and says the takes are straight out of the model with no cutting, grading, or retouching.
- **Summary:** A systematic benchmark tests FLUX.3 on causal chains, mirrors/reflections, and numerical bookkeeping, covering 30 chain-reaction clips, 20 reflection clips, and 20 quantity/count clips.
- **Workflow/details:** Martini inspects every take frame by frame, using contact strips plus targeted full-resolution checks. Fourteen of 30 chain-reaction takes complete every requested beat, with seven-step chains sometimes outperforming shorter ones; a recurring failure is a small object that must arrive at a precise target near the payoff. The report finds 12 of 20 mirror tests hold correctly, while failures often treat the reflection as scenery rather than recomputing the subject. Counting is weaker at larger quantities: examples include ten named coins becoming thirteen and twelve balloons becoming fifteen, and Martini recommends keeping count targets at eight or below and arranging them in visually constrained layouts.
- **Prompt provenance:** `verbatim_in_post` — verified excerpt: “A ball topples dominoes that trip a lever that drops a marble into a teacup.” The report also publishes the complete seven-step breakfast-machine prompt whose full causal sequence lands.
- **Why included:** Newly surfaced first-party FLUX.3 benchmark with direct videos, exact prompts, frame-by-frame analysis, quantitative/categorical outcomes, and candid failure modes. It provides reproducible evidence about physical causality, optical reflection, and object-count consistency rather than a cherry-picked aesthetic demo.

### 219. Thirty-second beach shark-rescue long take with telephoto continuity — DennisVisuals

- **Creator:** [DennisVisuals (@DtheW1995)](https://x.com/DtheW1995)
- **Published:** 2026-09-15 (same-day relative timestamp on the public creator-profile mirror at verification; exact X timestamp not exposed).
- **Original source profile:** [DennisVisuals on X](https://x.com/DtheW1995) — the accessible public index did not expose a stable direct status URL for this post.
- **Secondary verification source:** [Public creator-profile mirror preserving the original creator wording, explicit Flux 3 attribution, attached tweet-video marker, and complete visible prompt](https://www.sotwe.com/dthew1995)
- **Model attribution:** DennisVisuals explicitly ends the post with “Made with Flux 3.”
- **Summary:** A 30-second raw beach-telephoto rescue scene follows an elderly couple stranded offshore on a Techhalla hydrobike as an approaching shark closes in; a military RHIB races over, physically positions itself between shark and hydrobike, rescues both elders, and returns them to shallow water while the beach crowd reacts.
- **Workflow/details:** One strict unbroken 30-second take filmed conceptually from the sand through a long telephoto lens, with deliberate zoom hunting, focus slips, phone/telephoto compression, wind on the microphone, and no polished camera language. The prompt is fully time-coded from 0–30 seconds and specifies the shark’s approach, RHIB entry and blocking maneuver, two-person extraction, hydrobike interaction, retreat to shore, crowd reaction, native ambience/dialogue, and strong physical/continuity negatives. No verified seed, resolution, provider, reference media, or post-production settings are publicly disclosed.
- **Prompt provenance:** `verbatim_in_post` — “Raw amateur/paparazzi beach footage, harsh midday sun, hot haze, blown highlights, crushed shadows, dirty sensor, rolling shutter, imperfect autofocus.” The complete 0–30 second prompt remains visible in the secondary verification source; no wording has been reconstructed.
- **Why included:** Same-day original-creator FLUX 3 attribution preserved by a public mirror, attached-video verification, and a complete highly structured prompt. It is a difficult long-take benchmark for distance-to-subject continuity, telephoto camera recovery, shark/RHIB/couple spatial geometry, rescue causality, physically plausible boat interaction, two-person extraction, crowd reaction, and native audio without cuts or hidden transitions.

### 220. Thirty-nine-take on-screen typography, subtitles, and dynamic-state stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-15.
- **Original source:** [On-screen text — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/on-screen-text)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; it publishes direct FLUX.3 takes with full prompts and states that every take is straight out of the model with nothing cut, graded, or retouched.
- **Summary:** A controlled 39-take evaluation tests title cards, dated archival graphics, scorebugs, lower thirds, departure boards, end credits, subtitles, and other on-screen typography, measuring exact character fidelity, temporal stability, historical-date accuracy, and whether changing numeric state remains correct over time.
- **Workflow/details:** Martini planned 40 takes and analyzed 39, split between 20 archival mini-documentaries and 20 broadcast-graphics packages, reviewing the clips frame by frame. At 21:9 and 1440×608 draft resolution, even 4%-frame-height subtitles remained readable. Across the graphics set, 132 of 145 requested strings rendered exactly; 69 of 74 dated title cards matched the historical record. A six-row airport departure board held all 35 requested fields exactly and changed only the two instructed Oslo fields, while dynamic arithmetic/state remained a clear failure mode: clocks, score totals, countdowns, and seat counts could update incorrectly even when surrounding labels stayed perfect. Requested overlay text was much more reliable than incidental signage inside the scene.
- **Prompt provenance:** `verbatim_in_post` — “An airport departure board, 12 seconds, with exactly specified typography.” The complete departure-board, end-credit, subtitle, boxing-graphic, archival-title, and other prompts are printed in full on the first-party report.
- **Why included:** Newly surfaced first-party FLUX.3 report with embedded video takes, exact prompts, frame-by-frame measurements, explicit no-post-processing provenance, and unusually actionable production guidance. It provides high-signal evidence for spelling, tables/lists, subtitles, temporal text stability, and the specific boundary between static text fidelity and dynamic numeric-state failure; the exact source URL was not already represented in the README.

### 221. Seventy-eight-take capture-format and contradiction stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-15.
- **Original source:** [Formats — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/formats)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; all 78 returned takes are direct FLUX.3 generations, and the source states that every take is straight out of the model with nothing cut, graded, or retouched.
- **Summary:** A controlled 39-pair A/B benchmark tests whether capture and genre-format cues such as CCTV, bodycam, silent film, VHS, noir, IMAX, newsreel, slow cinema, broadcast, and instructional footage keep their visual grammar when the second prompt deliberately contradicts location, framing, behavior, sound, or edit rhythm.
- **Workflow/details:** Aspect ratio and duration were left on AUTO so the model’s own format choices were measurable. Martini analyzed 78 returned takes with contact sheets and A/B frame strips, plus container resolution/duration, ffmpeg scene-cut counts, volume/silence measurements, and motion-energy. Twenty clips auto-selected 1088×800 around capture formats such as CCTV, VHS, newsreel, and noir while most other clips stayed 1280×704; explicit frame instructions could override this, including 1440×608 anamorphic and 704×1280 vertical outputs. Of 39 contradictions, 28 landed clearly, while edit pacing was notably stubborn: a request for a hard cut every second produced zero detected cuts. Silence requests were measurable wins, while more semantic audio contradictions were less reliably verifiable.
- **Prompt provenance:** `verbatim_in_post` — “A submarine documentary: tension in the sonar room — but staged as a sunlit pastoral picnic.” The report prints every full prompt.
- **Why included:** Newly surfaced first-party FLUX.3 source with embedded direct outputs, full prompts, explicit no-post-processing provenance, and unusually reproducible measurements. It isolates a production-critical behavior: format tokens can silently control aspect ratio, runtime, camera grammar, and edit cadence more strongly than later contradictory instructions; the exact source URL was not already represented in the README.

### 222. Three-anchor seaweed-farm music video with native vocal, music, and ambience — Runware

- **Creator:** [Runware](https://runware.ai/) — first-party FLUX 3 model-gallery example.
- **Published:** Publication date not shown; verified 2026-09-15.
- **Original source:** [Runware FLUX 3 Video model page with the “Use example” gallery](https://runware.ai/models/bfl-flux-3-video)
- **Model attribution:** Runware explicitly identifies the page as FLUX 3 Video and the model as `bfl:flux@3-video`; the seaweed-farm clip appears as one of the page’s prompt-to-output examples.
- **Summary:** A 12-second blue-hour music-video segment on a working seaweed farm keeps the same singer, orange oilskin coat, coastal location, cyan-and-amber grade, and tactile 16mm texture across a wide tidal-flat view, a lip-synced medium close-up, and a final overhead composition.
- **Workflow/details:** The visible prompt uses three supplied visual anchors and time-codes the progression at 0–5s, 5–10s, and 10–12s: slow dolly toward the singer, transition to a medium close-up while tracking backward, then a rapid rise to an overhead view. It asks for accurate lip-sync plus synchronized audio combining an intimate female lead vocal, a restrained 96 BPM electronic-folk arrangement, and wind, water, coat movement, and footsteps. Runware reports a cost of `$3.4921` for this example.
- **Prompt provenance:** `verbatim_in_post` — “Create a polished 12-second music-video segment for an original electronic-folk single set on a working seaweed farm at blue hour.” The complete prompt remains visible in the first-party source.
- **Why included:** First-party prompt/output evidence with explicit FLUX 3 attribution, a visible reproducible prompt, multi-anchor temporal control, native sung vocal plus music and ambience, precise camera choreography, and cost telemetry in one production-style example.

### 223. 129-take additive prompt-length ladder with measurable quality plateau — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-15.
- **Original source:** [Prompt length — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/prompt-length)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; it publishes 129 direct FLUX.3 takes with their prompts and states that every take is straight out of the model with nothing cut, graded, or retouched.
- **Summary:** A controlled 129-take study grows the same scene briefs from roughly 500 to 4,700 characters in ten additive rungs to measure how long FLUX.3 keeps following new instructions and when additional prompt detail stops materially improving the film.
- **Workflow/details:** Martini expands each prompt rung by rung so prior sentences remain verbatim while new detail is added. A major cohort uses seven fixed headings—ACTION, SETTING, SUBJECT, DIALOGUE, CAMERA & LIGHT, SOUND & MUSIC, and GRADE—while companion ladders compare animation beat lists, screenplay format, timecode blocks, shot lists, prose, vertical phone footage, and tag-style prompts. The report finds that FLUX.3 still obeys instructions buried beyond 3,600 characters and reads to roughly 4,700, but the biggest visible gain arrives by about 1,400 characters; after roughly 2,400, added detail is usually texture rather than a better film. Prompt structure matters more than sheer length for edit grammar: timecode blocks produced one continuous take at every tested length, shot lists stayed around 3–5 shots, and prose accumulated more cuts as prompts grew.
- **Prompt provenance:** `verbatim_in_post` — “ACTION — A short-order cook makes one last meal on the diner's final night.” The source prints every complete prompt in full.
- **Why included:** Newly surfaced first-party FLUX.3 report with 129 direct videos, exact additive prompt ladders, published prompts, and explicit no-post-processing provenance. It replaces prompt-length folklore with a reproducible controlled benchmark and gives practical thresholds for descriptive density, runtime pressure, and prompt structure before longer writing stops paying off.

### 224. Sixty-take sound-event, beat-sync, and dialogue-only audiovisual stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-16.
- **Original source:** [Sound and dialogue — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/sound-and-dialogue)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; it publishes 60 direct FLUX.3 takes with full prompts and states that every take is straight out of the model with nothing cut, graded, or retouched.
- **Summary:** A controlled 60-take evaluation tests whether native sound can causally drive visible action, whether cuts and movement can follow musical beats, and how much scene construction FLUX.3 invents when given dialogue lines without any setting, camera, or lighting instructions.
- **Workflow/details:** Three bins of 20 takes, all 21:9 and 5–10 seconds, with audio generated in the same pass as the picture. Martini measures RMS audio envelopes at 100 Hz, per-frame picture motion and brightness, and ffmpeg scene cuts, then compares the signals against within-clip null baselines. In the off-screen-sound bin, audio rises a median +4.13 dB in the half-second before the strongest picture motion, positive in 16 of 19 measurable takes versus +0.11 dB at random times. Beat-synced cutting does not hold: 12 of 20 music-bin takes remain single-shot, and existing cuts land no closer to audio onsets than chance. Dialogue-only prompts still invent locations, props, coverage, and often cuts near line boundaries; lighting/color changes can align tightly to musical events, while requested silence is unreliable.
- **Prompt provenance:** `verbatim_in_post` — “A woman reads at a kitchen table. Off-screen, a door slams hard. She flinches and looks up toward the sound.” Every complete prompt in the report is printed in full.
- **Why included:** Newly surfaced first-party FLUX.3 report with direct video takes, exact prompts, explicit no-post-processing provenance, quantitative audio/video timing analysis, and candid failure modes. It gives unusually actionable guidance for sound-as-cause prompting, reaction timing, dialogue-driven coverage, beat-sync limits, silence failures, and in-model audiovisual planning; the exact source URL was not already represented in the README.

### 225. 120-take 5/10/15/20-second duration ladder with narrative scaling — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-16.
- **Original source:** [Duration — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/duration)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; it publishes 120 direct FLUX.3 takes with their prompts and states that every take in the stress-test run is a single model generation with nothing cut, graded, or retouched.
- **Summary:** Thirty scene briefs are each rendered at 5, 10, 15, and 20 seconds to test whether longer FLUX.3 generations merely stretch the same idea or actually develop more story; the result is a controlled duration ladder rather than a set of unrelated showcase clips.
- **Workflow/details:** 120 takes at 21:9, 1440×608, 24 fps, all with audio. Twenty-eight of thirty scenes form clean four-rung ladders; where the model obeys the requested duration, outputs land at 121, 241, 361, and 481 frames. Spoken content scales from 16.4 words at 5s to 54.2 at 20s while speech rate stays broadly flat, and distinct dialogue beats grow from 2.5 to 7.0. Twenty-two of twenty-six analyzable 20s takes introduce at least one new dialogue line after the 15-second mark, while 26 of 29 twenty-second takes preserve a no-cut instruction. Martini’s core finding is that longer takes usually add new beats and late payoffs instead of simply slowing down a five-second idea.
- **Prompt provenance:** `verbatim_in_post` — “A white gallery. A critic in an expensive coat stands before a completely blank canvas.” The complete prompt and every other prompt in the report remain printed in full on the first-party source.
- **Why included:** Newly surfaced first-party FLUX.3 report with 120 directly inspectable videos, exact prompts, fixed resolution/frame rate, synchronized audio, and controlled duration as the only intended variable. It gives unusually actionable evidence for choosing 5/10/15/20-second runtimes, planning late narrative turns, and understanding when continuous-shot instructions survive the full 20-second window; the exact source URL was not already present in the README.

### 226. Fifty-take prompt-format equivalence and noun-retention stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-16.
- **Original source:** [Prompt style — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/prompt-style)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; all 50 takes are direct FLUX.3 outputs, with every prompt published in full and no cutting, grading, or retouching.
- **Summary:** Five identical scene concepts are each rewritten in ten prompt dialects—plain prose, timestamps, shot list, screenplay, cinematography spec, keywords, no-camera prose, technique-only wording, SFX/dialogue markup, and labelled fields—to isolate whether format itself materially changes the generated film.
- **Workflow/details:** Fifty takes, with prompts only 139–313 characters long. Martini finds eight of ten prompt styles broadly interchangeable as long as the prompt keeps the concrete nouns for who, where, and what happens. Technique-only prompts fail hardest when story nouns disappear. Numbered shot lists and labelled fields land all five intended payoffs, but cuts are driven more by scene content than by formatting; timestamps are the one dialect that reliably pins duration.
- **Prompt provenance:** `verbatim_in_post` — “A woman sprints down the pier steps toward the last ferry as it pulls away. The gap of black water widens. She throws her bag, leaps, and the deckhand catches her arm as the horn sounds.”
- **Why included:** First-party direct videos, full prompts, controlled single-variable design, and explicit no-post-processing provenance make this unusually reusable evidence that concrete scene nouns matter more than fashionable prompt syntax.

### 227. Eighty-three-take century-spanning era and anachronism stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-16.
- **Original source:** [Eras — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/eras)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; all 83 reported takes are direct FLUX.3 outputs with full published prompts and no cutting, grading, or retouching.
- **Summary:** Four everyday scenes are swept through film eras from 1901 to 2020, then extended into future dates, retro-future depictions, and mixed-era collisions to measure how period words alter not just grade but frame shape, editing grammar, production design, and camera language.
- **Workflow/details:** Aspect ratio was left on AUTO; 77 takes were inspected frame by frame with ffmpeg and all 83 were reviewed on the sheet. FLUX.3 usually chose 1088×800 from 1901–2004, 1280×704 for 2013, and 704×1280 for 2020; a 2004 flip-phone football clip independently went vertical because the phone was held upright. 1929 newsreel prompts generated period title cards and internal cuts. Recent-era distinction weakens after roughly 1996; future years alone contribute little, while named future objects/mechanisms work far better. Anachronistic collisions succeeded in 17 of 19 returned tests.
- **Prompt provenance:** `verbatim_in_post` — “A 1929 newsreel with title cards of a football match.”
- **Why included:** The first-party benchmark exposes structural era knowledge—container, edit rhythm, set dressing, and capture medium—with measurable failures and practical prompting guidance, rather than merely showing a period-color grade.

### 228. Forty-five-take reroll variance and prompt-detail consistency stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-16.
- **Original source:** [Variance — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/variance)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; it publishes the direct FLUX.3 takes with their prompts as part of the same unedited stress-test suite.
- **Summary:** Four concepts—a bartender, sprinkler, newsroom, and octopus—are each rendered repeatedly from one-line, paragraph, and full-brief prompt versions to measure what remains stable across rerolls and what still changes even as direction becomes more detailed.
- **Workflow/details:** FLUX.3 draft, 21:9, sound on; four rerolls were planned for each prompt level, with 45 delivered files. Longer prompts strongly stabilize location, light, look, and props, but do not lock casting, lens choice, runtime, or narrative ending. In the octopus example, the long brief produces closer visual matches yet fewer clean escapes than the shorter paragraph because the extra action list consumes the available clip time.
- **Prompt provenance:** `verbatim_in_post` — “A 1987 local news report about a runaway parade balloon.”
- **Why included:** A reproducible reroll methodology turns subjective “seed variance” into production guidance: added detail buys visual consistency, but not necessarily story completion, making the report highly useful for selection and reroll strategy.

### 229. Ninety-nine-take seven-language casting, location, and signage stress test — Martini

- **Creator:** [Martini](https://www.martini.film/)
- **Published:** Publication date not shown; verified 2026-09-16.
- **Original source:** [Languages — FLUX.3 stress test](https://www.martini.film/models/flux-3/reports/languages)
- **Model attribution:** Martini explicitly labels the report `model FLUX.3`; the report publishes 99 direct FLUX.3 takes and their prompts as part of the same unedited stress-test suite.
- **Summary:** Fifteen scene concepts are translated across English, Cantonese, Spanish, Japanese, Korean, Arabic, and French while keeping the underlying scenario fixed, measuring how prompt language changes casting, location, set dressing, signage, and visual assumptions even when the requested action is the same.
- **Workflow/details:** 105 takes were planned and 99 delivered, with fourteen complete seven-language comparison sets. Every clip is 10 seconds and 21:9 except one 15-second output. Casting tracks prompt language in 12 of 14 comparable scenes; streets and homes often shift culturally, while institutional interiors change much less. English is not neutral—it invokes its own visual priors. Fully directed 676–862-character prompts narrow language-driven differences, and supplied Arabic or Chinese sign copy can render cleanly in the demonstrated examples.
- **Prompt provenance:** `verbatim_in_post` — “A street food stall at evening rush hour: steam, shouted orders, and regulars who don't need to say what they want.”
- **Why included:** Direct first-party videos, complete prompt translations, and a controlled language-only sweep make this a rare reproducible benchmark for multilingual visual priors, casting, location steering, and signage rather than just speech generation.

### 230. Five-mode FLUX.3 workflow suite with full prompts and embedded outputs — Scenario

- **Creator:** [Scenario](https://www.scenario.com/) — first-party FLUX.3 integration documentation.
- **Published:** Publication date not shown; verified 2026-09-16 (the first-party page showed “Last updated 2 days ago”).
- **Original source:** [FLUX.3 Video: The Essentials](https://help.scenario.com/articles/2415759054-flux-3-video-the-essentials)
- **Model attribution:** Scenario explicitly identifies the family as Black Forest Labs’ `FLUX.3 Video` and publishes named model IDs for Text to Video, Image to Video, First and Last Frame, Keyframes, and Extend, with embedded outputs for each workflow.
- **Summary:** Scenario’s first-party guide pairs exact prompts with direct FLUX.3 outputs across a 1080p sci-fi text-to-video shot and lower-resolution Draft comparison, a dragon image-to-video animation, a 20-second 21:9 chariot first/last-frame transition, a 15-second 2:1 four-keyframe samurai kata, and a dragon continuation shot.
- **Workflow/details:** Full models expose 720p/1080p, clips run 5–20 seconds, audio is generated by default, and supported aspect ratios range from 21:9 to 9:16. Keyframes are pinned by frame index at 24 fps; Scenario recommends Draft for iteration and full models for finals, timed action beats, explicit audio, compositionally consistent supplied frames, and continuity language in first/last-frame and keyframe prompts. The page notes no fixed seed control and recommends source clips under roughly 15 seconds for Extend.
- **Prompt provenance:** `verbatim_in_post` — “A samurai sword kata following the four keyframes, with a slow arcing camera.” The complete 15-second four-beat samurai prompt, plus complete prompts for the other embedded examples, is visibly published in the first-party source.
- **Why included:** Newly updated first-party platform documentation with direct embedded FLUX.3 outputs, exact model IDs, concrete resolution/duration/aspect-ratio controls, full reproducible prompts, and multiple distinct input modes. It is unusually useful as a practical workflow reference because it shows prompt-to-output evidence for draft/final iteration, single-image animation, exact endpoint framing, timed multi-keyframe choreography, and seamless continuation on one verified page.

### 231. Blind five-prompt FLUX 3 benchmark suite across consistency, audio, adherence, aesthetics, and physics — OpenArt Arena

- **Creator:** [OpenArt Arena](https://openart.ai/arena/leaderboard) / OpenArt AI — primary generation and independent benchmark source.
- **Published:** 2026-09-16
- **Original source:** [OpenArt Arena Video Leaderboard — sample prompts and generations](https://openart.ai/arena/leaderboard)
- **Supporting methodology:** [OpenArt Arena methodology](https://openart.ai/arena/methodology)
- **Model attribution:** The leaderboard explicitly labels each embedded sample as **Flux 3 Video — Black Forest Labs** and places it alongside same-brief outputs from the other evaluated video models.
- **Summary:** Five directly embedded FLUX 3 outputs stress identity consistency across a three-scene wardrobe/location sequence, English shouted dialogue and audio quality, a simple cowboy-dance instruction, reference-identity cinematic parade aesthetics, and a timed argument/push/fall/splash micro-drama for physics and motion.
- **Workflow/details:** OpenArt says it procures creation-use-case prompts, runs every model on the same brief, and admits one output per model by a fixed rule rather than hand-picking. The published FLUX 3 examples are 10s, 5s, 6s, 10s, and 9s respectively. The overall board lists FLUX 3 Video at 720p/1080p with up to 20-second output. Seed values, the actual reference-image assets for the reference-guided examples, and any post-processing are not disclosed on the public page, so none are inferred.
- **Prompt provenance:** `verbatim_in_post` — “Three girls tip their hats to the camera and then start doing a cowboy rodeo dance. No talking.” Four additional complete prompts are visibly published next to their model-by-model generations.
- **Why included:** A newly published primary-source benchmark page with multiple embedded, explicitly model-labeled FLUX 3 videos, full visible prompts, controlled same-brief comparisons, and blind professional judging. It is unusually useful because the same source exposes qualitative outputs and a reproducible evaluation protocol across five distinct failure modes rather than presenting only a curated showreel.

### 232. Twenty-second skincare UGC with expressive dialogue and facial performance — Sher Hassan

- **Creator:** [Sher Hassan](https://pk.linkedin.com/in/thesherhassan)
- **Published:** Exact timestamp not exposed; verified 2026-09-17 (LinkedIn showed the post as approximately 5 hours old).
- **Original source:** [Sher Hassan’s public LinkedIn profile with the original creator post](https://pk.linkedin.com/in/thesherhassan) — the public index exposes the creator post on-profile but not a stable direct activity permalink.
- **Model attribution:** Hassan explicitly says “Flux 3 might be my favourite model for AI UGC right now” and states that he made the skincare clip inside Higgsfield AI.
- **Summary:** A casual talking-to-camera skincare UGC clip focuses on believable presenter delivery rather than cinematic spectacle; Hassan calls out expressive voice performance, comfortable dialogue flow, and facial reactions that stay natural while the subject speaks.
- **Workflow/details:** Flux 3 generated inside Higgsfield AI; 20-second output. Hassan compares the result favorably with Seedance 2.5 for this UGC use case and says the current limitation is room to extend: he would like a 30-second mode plus reference-asset controls that keep the character, product, and setting consistent across a longer scene. No verified resolution, seed, reference assets, or post-production settings are publicly exposed.
- **Prompt provenance:** `not_provided` — no exact generation prompt is visible in the verified first-party source, and nothing has been reconstructed or inferred.
- **Why included:** Fresh first-party creator attribution, explicit Flux 3 labeling, a concrete Higgsfield workflow and verified 20-second duration, plus a strong creator-side quality signal centered on voice expression, conversational timing, and facial performance — exactly the subtle behaviors that often make or break AI UGC realism.

### 233. Single-take violin subject/environment-lock prompting workflow — Higgsfield

- **Creator:** [Higgsfield](https://higgsfield.ai/) — first-party FLUX 3 integration guide.
- **Published:** 2026-08-16; the page was subsequently updated and was re-verified 2026-09-17.
- **Original source:** [Meet Flux 3 on Higgsfield: How It Works and What You Get](https://higgsfield.ai/blog/flux-3-higgsfield)
- **Model attribution:** Higgsfield explicitly identifies the generation model as **FLUX.3 Video** from Black Forest Labs and presents the embedded result inside its step-by-step FLUX 3 workflow.
- **Summary:** A violinist performs inside a white circular rotunda above a ring of deep-blue water while one restrained camera move slowly dollies backward; the prompt deliberately locks the performer’s orientation, the architecture, water geometry, palette, and camera behavior to reduce drift during the take.
- **Workflow/details:** Text-to-video prompt inside Higgsfield’s FLUX 3 workflow. The published brief requests one continuous 16:9 shot and ends with `Total: 7s / 1 shot / 16:9`, while a preceding beat label says `Single continuous shot 5s`; the camera instruction is one straight ground-level dolly back with no pan, orbit, or crane. The guide says creative camera/lighting direction should be written into the prompt, optional synchronized audio is generated in the same pass, and FLUX 3 on Higgsfield also supports image-to-video, continuation, Start/End Frame control, and up to 10 reference frames when those modes are used. The page publishes 720p/1080p pricing for 5- and 20-second generations.
- **Prompt provenance:** `verbatim_in_post` — “single continuous shot, one take no cuts, cinematic oner, cinematic lighting, photorealistic, 35mm film quality”. The complete subject-lock, environment-lock, color-lock, and camera prompt remains visibly published beside the embedded video.
- **Why included:** First-party prompt-to-video evidence with an embedded FLUX 3 result, full visible prompt, explicit model attribution, and unusually reusable anti-drift direction. The clip tests subtle hand/instrument motion, centered human performance, stable architectural geometry, water continuity, color consistency, and a single controlled camera move without relying on rapid cuts or spectacle.

### 234. Storyboard-grid-to-FLUX3 1978 Americana filmmaking workflow — seeksteve

- **Creator:** [seeksteve (@seeksteve)](https://x.com/seeksteve)
- **Published:** 2026-09-14
- **Original post:** [View on X](https://x.com/seeksteve/status/2099333648059367607)
- **Secondary verification source:** [Wikiprompt mirror preserving the creator attribution, source URL, workflow text, FLUX3 model label, and related-video context](https://www.wikiprompt.org/ai-vibe-filmmaking-workflow-with-storyboard-grids)
- **Model attribution:** The preserved creator workflow explicitly states `ai video: FLUX3 at 720p`; the verification page also labels the media `Model FLUX3` and credits seeksteve with the original X source.
- **Summary:** A complete AI-filmmaking pipeline uses five dense 5×5 Midjourney storyboard grids to seed a nostalgic 1978 “great American summer” visual language, then turns storyboard cells into rapid FLUX3 video shots before assembling the footage around an original Suno v6 soundtrack in DaVinci Resolve.
- **Workflow/details:** Creative direction by the creator; five 20–25-shot Midjourney grids spanning nostalgia, contamination of everyday life, fear/grief, and nightmare; FLUX3 at 720p; the prompt asks the model to show a grid for 0.5 seconds and then treat individual cells as separate 0.5–1.2-second shots with randomized durations. Visual language includes “photochemical 35mm handheld footage” and “vintage Cooke Speed Panchro spherical primes.” Music is iterated in Suno v6; DaVinci Resolve 21.1 plus GPT-6 Astra-light handles shot detection, beat matching, and editing, with Python + SciPy used for beat/transition detection, conversion to 24 fps Resolve timeline markers, and FFmpeg verification. In the preserved creator workflow, the storyboard grids are used as visual guidance/aesthetic seeding rather than model-side reference inputs.
- **Prompt provenance:** `verbatim_in_post` — visible workflow excerpt: “idea/creative direction: me, a human … 5×5 storyboard grids: Midjourney … ai video: FLUX3 at 720p … original soundtrack: Suno v6”. The secondary verification source preserves the full workflow text and links the original X post; no prompt wording has been inferred from the video.
- **Why included:** Fresh creator-attributed FLUX3 video workflow with a traceable original X URL, deeply reproducible production details, explicit 720p model usage, shot-duration instructions, soundtrack/editor pipeline, and a distinctive method for converting storyboard grids into fast multi-shot footage. The best currently accessible evidence is a credible secondary page that directly preserves the original creator attribution and workflow, so it is explicitly labeled as secondary verification.

## How updates work

The hourly ChatGPT task checks this README first, searches for newer qualifying sources, rejects duplicates and ambiguous attribution, then appends verified entries here. It reports only when at least one new entry has been successfully committed.

## Contributing

Manual nominations and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Repository text and curation structure are licensed under the [MIT License](LICENSE). Linked post text, prompts, media, creator names, and other third-party material remain the property of their respective authors.
