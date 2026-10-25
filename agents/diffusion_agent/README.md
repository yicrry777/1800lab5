# Theranos Emerging Technology Diffusion Agent

Assignment 5, v0.4. This is a historical diffusion analysis of Theranos's claimed proprietary micro-volume multi-analyte platform. The primary organization is Theranos; Walgreens and a hypothetical independent clinical laboratory are contrast contexts. The agent distinguishes Theranos-branded service volume from actual use and validation of its proprietary analyzer. It does not propose current clinical deployment by the defunct company.

From the repository root, actually run:

```sh
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/primary.json
python3 tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/contrast_1.json
python3 tools/build_prompt.py --agent agents/diffusion_agent --case agents/diffusion_agent/cases/contrast_2.json
python3 tools/validate_response.py agents/diffusion_agent/responses/primary_response.json
python3 tools/validate_response.py agents/diffusion_agent/responses/contrast_1_response.json
python3 tools/validate_response.py agents/diffusion_agent/responses/contrast_2_response.json
python3 agents/diffusion_agent/tests/check_diffusion_contrast.py
```

To rerun the model interactively, paste each generated `work/` packet into ChatGPT, save its JSON response, and run the validator and contrast check again. The [Agent Record](records/agent_record.md) and [evidence/test record](records/test_and_evidence_record.md) explain the bounded decision and limitations. The earlier ambient-scribe attempt is preserved only in Git history after the user changed the case to Theranos.
