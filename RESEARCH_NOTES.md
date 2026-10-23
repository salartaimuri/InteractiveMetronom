# BeatBloom research brief

## Scope and evidence quality

The supplied `IM-RESEARCH-BIBLIOGRAPHY.pdf` is a reference list, not a systematic review. It contains 21 references labeled as Interactive Metronome research and 179 broader supporting references. The direct references mix randomized trials with pilot studies, case reports, preliminary investigations, dissertations, conference material, and unpublished or company white papers. Association studies about timing, attention, or brain networks do not by themselves demonstrate that metronome training treats a condition.

Every one of the 200 citations has been extracted and classified in `research_catalog.csv`. That catalog records the source section, complete extracted citation, topic, evidence type inferred from the citation, product implication, and review status. It deliberately distinguishes citation-level classification from full-text review because several sources are paywalled, unpublished, incomplete, or grey literature.

This means BeatBloom should be described as a rhythm-practice tool. Clinical efficacy, diagnosis, and condition-specific treatment claims require independent validation of this product.

## Findings relevant to the product

### Motor timing and rehabilitation

- A 2022 systematic review and meta-analysis included 18 prospective studies and reported a moderate positive effect of Interactive Metronome training on motor performance. Effects were reported across athletes, healthy participants, and people with neurological disorders. This supports timing practice as a motor-training mechanism, but does not establish benefits for every diagnosis or cognitive outcome. [Lee et al., 2022](https://pubmed.ncbi.nlm.nih.gov/35762351/)
- A randomized pilot trial of 46 service members with persistent cognitive complaints after blast-related mild-to-moderate TBI compared standard rehabilitation with standard rehabilitation plus 15 Interactive Metronome sessions. Unadjusted group differences favored the added intervention for attention and immediate and delayed memory; the authors explicitly described the findings as preliminary. [Nelson et al., 2013](https://pubmed.ncbi.nlm.nih.gov/24059443/)
- A stroke upper-extremity report involved only two participants receiving 60-minute sessions three times weekly for four weeks. Improvements were observed, but the design cannot establish causality or generalizability. [Beckelhimer et al., 2011](https://pubmed.ncbi.nlm.nih.gov/21309376/)
- More recent rehabilitation evidence supports individualized auditory-motor cueing for specific tasks. In a multi-site randomized trial of 87 people after stroke, a closed-loop rhythmic walking system produced a larger increase in walking speed than walking practice alone, with similar adverse-event counts. This was a sensor-based, individualized gait system and should not be generalized to unsupervised tapping exercises. [Awad et al., 2024](https://pubmed.ncbi.nlm.nih.gov/38332008/)

### ADHD

- The principal pediatric ADHD study randomized 56 boys aged 6-12 to 15 hours of Interactive Metronome training, video-game activity, or no intervention. Outcomes favored the metronome group across attention, motor, language, reading, and parent-report measures. The population included only boys, the study is from 2001, and the unusually large number of outcomes makes replication and modern risk-of-bias assessment important. [Shaffer et al., 2001](https://doi.org/10.5014/ajot.55.2.155)
- Later ADHD evidence includes case reports and very small studies. A two-child case study cannot establish effectiveness, though it may inform feasibility and measurement choices. [Namgung et al., 2018](https://pubmed.ncbi.nlm.nih.gov/29643596/)
- A 2023 systematic review of music-based ADHD studies found only one included interactive-metronome study and concluded that more specific research is needed. [Martin-Moratinos et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10221503/)

### Autism

- The supplied bibliography contains timing and autism theory references but little direct evidence that Interactive Metronome itself improves core autism outcomes.
- A small randomized study of 30 autistic children found that adding rhythmic auditory gait cueing to physical therapy improved measured gross-motor outcomes more than physical therapy alone. It tested a combined, therapist-led program rather than a standalone tapping app. [El Shemy & El-Sayed, 2018](https://pubmed.ncbi.nlm.nih.gov/30154601/)
- A 2024 review describes rhythm and music interventions as promising for sensorimotor regulation and functional engagement in autism, while framing the evidence as emerging. It recommends a strengths-based use of musical abilities. [LaGasse et al., 2024](https://pubmed.ncbi.nlm.nih.gov/39040594/)
- A 2026 randomized proof-of-concept study of 26 autistic children found a finger-tapping rhythm game feasible and engaging, with preliminary rhythm and executive-function signals. The sample and two-week duration mean that efficacy remains uncertain. [Jamey et al., 2026](https://pubmed.ncbi.nlm.nih.gov/42024144/)

## Product rules derived from the evidence

1. **Measure the trained task directly.** Report tap-to-beat error in milliseconds and the number of taps inside a plainly stated practice window. Do not convert this into a diagnostic score.
2. **Use within-person progress.** Compare a child with their own prior sessions rather than population norms. Browser and device latency means results are practice feedback, not clinical measurements.
3. **Keep feedback neutral and immediate.** “Early,” “late,” and “together” describe timing without turning errors into failure.
4. **Allow individualization.** Tempo, duration, sensory intensity, sound, input method, and movement should be selectable. No single setting is appropriate for all ADHD, autistic, or rehabilitation users.
5. **Prefer short, tolerable sessions.** Research protocols are often much longer and clinician-led; a consumer prototype should not reproduce clinical dosage claims.
6. **Treat whole-body and gait work as supervised.** Balance, walking, post-stroke, and assisted-movement exercises should be selected and monitored by a qualified professional.
7. **Do not promise transfer.** Better tapping timing does not automatically mean better attention, reading, communication, executive function, or daily functioning.
8. **Design for future validation.** A research version would need calibrated input hardware, device-latency measurement, preregistered outcomes, adverse-event monitoring, appropriate control conditions, and independent trials.

## Current implementation mapping

| Evidence-informed principle | BeatBloom implementation |
| --- | --- |
| Direct timing feedback | Nearest-beat difference calculated from high-resolution browser timestamps |
| Transparent measure | Mean absolute difference shown in milliseconds |
| Immediate knowledge of performance | Early, late, and together feedback after each input |
| Individualized challenge | 40-100 BPM and 1-5 minute controls with three starting modes |
| Graded knowledge of results | Selectable 120 ms, 80 ms, or 50 ms practice windows, always shown explicitly |
| Motor-learning progression | Optional tempo adaptation in small 5 BPM steps based on the latest eight taps |
| Bilateral coordination | Optional alternating-hand task using distinct F and J inputs |
| Fatigue and regulation | Pause/resume without penalizing or shortening the remaining session |
| Accessible participation | Touch, mouse, and keyboard input; movement can be therapist-selected |
| Sensory choice | Sound control, gentle-visual setting, and reduced-motion support |
| Low-pressure engagement | No failure state, leaderboard, normative ranking, or diagnostic interpretation |
| Privacy | Session summaries stored only in browser local storage |

## Important technical limitation

Browser audio scheduling, display refresh, operating-system input handling, keyboards, touchscreens, and wireless devices add latency. BeatBloom currently measures the time at which the browser receives an input relative to its scheduled beat. It is appropriate for playful practice feedback, but it is not equivalent to calibrated clinical trigger hardware and must not be represented as millisecond-accurate clinical assessment.
