# Assignment 5 Theranos diffusion evidence and test record

Checked 2026-10-24 (America/New_York). This is a retrospective of 2013–2018. Primary organization: Theranos. The same claimed proprietary platform and retail-testing application are held constant across the Theranos, Walgreens and hypothetical independent-lab cases. Later evidence is labeled hindsight; the recommendations describe what the historical gate should have been and do not assume Theranos still operates.

## Original evidence and limits

| Source | Dated observation | What it does and does not establish |
| --- | --- | --- |
| [FDA HSV-1 decision summary K143236](https://www.accessdata.fda.gov/cdrh_docs/reviews/k143236.pdf) | July 2, 2015 | Substantial equivalence for one specified HSV-1 IgG assay and intended use, including fingerstick specimen. It is not broad multi-analyte clearance. |
| [FDA Form 483](https://www.fda.gov/files/about%20fda/published/Theranos--Inc.--Newark--CA-483-Issued-09-16-2015.pdf) | Inspection Aug 25–Sep 16, 2015 | Nanotainer listing and complaint-handling observations. The form says observations are not a final agency compliance determination. |
| [Walgreens closure notice](https://www.walgreensbootsalliance.com/news-media/press-releases/2016/walgreens-terminates-relationship-with-theranos-will-be-closing-operations-at-all-40-theranos-wellness-centers-in-arizona) | June 12–13, 2016 | Partner terminated service at all 40 Arizona centers, citing voided results and CMS concerns. Center count is service distribution, not analyzer adoption. |
| [Arizona Attorney General 2017 annual report](https://www.azag.gov/sites/default/files/publications/2024-10/2017AnnualReport.pdf) | Describes 2013–2016; report year 2017 | About 1.5 million tests sold to over 175,000 Arizonans; roughly 10% later voided/corrected. These are Arizona service transactions and do not count proprietary-platform runs. |
| [SEC Theranos litigation release](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-24069) | March 19, 2018 | SEC alleged the proprietary analyzer performed only a small number of tests and most patient testing used third-party analyzers. This is a civil allegation; Theranos and Holmes settled without admitting or denying. |
| [DOJ account of trial evidence and verdicts](https://www.justice.gov/usao-ndca/pr/theranos-president-sentenced-more-12-years-fraud-jeopardized-patient-health-and-bilked) | December 2022, describing earlier conduct | Reports analyzer failures, voided analyzer tests, Balwani's conviction and Holmes's investor-fraud conviction. It calls Theranos defunct. Do not misstate Holmes's acquittal on patient-related counts. |

**Weak diffusion claim:** “1.5 million Theranos-branded tests prove the proprietary multi-analyte analyzer reached the early majority.” The Arizona figure has the wrong unit, no national platform denominator and no independent-lab adopter count. The narrow FDA assay decision does not repair this gap. The final agent abstains from a national adopter-stage label. It also treats less invasive, cheaper and faster testing as claims until assay-specific outcomes are verified.

## Actual runs and revision

1. The earlier ambient-scribe scenario remains in Git history but was superseded by the user's Theranos correction. The frozen scaffold was not edited.
2. Created three Theranos case inputs and ran the supplied prompt builder for the v0.3 primary case. Ran the frozen-core checker: **FROZEN CORE INTACT**. Saved an **adversarial diagnostic fixture** at `responses/diagnostic_primary_response.json` that conflates branded service volume and proprietary analyzer use, and overreads FDA clearance. Ran the supplied validator on that file: **VALIDATION PASSED**. This demonstrates that structural validation alone cannot detect the evidentiary error; the fixture is not asserted to be a spontaneous model failure.
3. Revised the student-editable instructions to v0.4: source type and date checks, service/platform denominator separation, narrow FDA scope, historical-vs-hindsight distinction and no patient rollout without independent validation.
4. Ran `python3 tools/build_prompt.py` separately for `cases/primary.json`, `cases/contrast_1.json` and `cases/contrast_2.json`. All three packets were generated in ignored `work/`. Analyzed each in this ChatGPT/Codex session and saved the structured outputs in `responses/`.
5. A temporary local response-writing helper initially failed on an apostrophe; because the shell continued, its subsequent validators checked stale output. I corrected the helper, reran it with `set -e`, then confirmed each response says agent version `0.4-student` and concerns Theranos. Only that successful rerun counts as the revised output test.
6. On the corrected files, ran `python3 tools/validate_response.py` separately for all three responses: **VALIDATION PASSED** three times. Ran `python3 agents/diffusion_agent/tests/check_diffusion_contrast.py`: **THERANOS CONTRAST PASSED: 3 contexts; evidence stable; decisions differ; overclaim rejected**. Ran `python3 tools/check_frozen_core.py`: **FROZEN CORE INTACT**. Ran `git diff --check`: no whitespace errors. The exact runnable commands are in the agent README.

The contrast script checks saved outputs for invariant general/application/evidence fields, all five Rogers factors, dated evidence presence, context-specific management actions, and absence of the diagnostic overclaim. It cannot establish that future model runs will always reason correctly. Human review checked that each cited original source supports its attributed claim and its limits.

## Context comparison and independent judgment

| Context | What stayed stable | Historical timing implication |
| --- | --- | --- |
| Theranos, innovating supplier | No demonstrated broad independent use of the proprietary platform; service counts cannot measure it | Halt broad clinical expansion at the 2015–2016 gate; immediately begin independent, nonclinical assay-by-assay validation and remediation |
| Walgreens, distribution partner | Same external evidence and Rogers-factor assessment | Withhold further center expansion; suspend affected testing as concerns emerged and transition customers. It actually closed the 40 Arizona centers in June 2016 |
| Hypothetical conservative independent lab | Same external evidence and Rogers-factor assessment | Reject patient use at the 2015 screen; only document review or nonclinical bench testing if full data and device access become available |

**Decision:** The technology did not earn a defensible broad diffusion-stage classification. The strongest signal of reach is the branded retail service network, which is not a signal of proprietary analyzer adoption. The most important inhibitor is failure to establish and transparently verify assay-specific performance compatible with clinical-lab practice. The Adoption Agent should inherit a strict separation between service uptake and validated device use, the narrow scope of the FDA decision, and a no-patient-use gate without independent validation.

## AI use and verification

ChatGPT/Codex assisted with factor mapping, adversarial test design, responses, revision and code checks. Numerical and consequential historical claims were checked against the original FDA, Walgreens, Arizona, SEC and DOJ materials above. The saved responses are representative model-assisted analyses in this session; the package does not call an external model API and did not process live patient data.
