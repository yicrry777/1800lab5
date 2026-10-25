# Emerging Technology Diffusion Agent

Assignment 5, v0.2. This specialist evaluates Rogers' adopter categories, five innovation attributes, diffusion forces, and context-specific pilot timing. It does not make the final adoption decision.

From the repository root:

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

Paste each generated packet from `work/` into ChatGPT to rerun interactively, save its JSON response, and validate again. The saved outputs and detailed source/test record are under `responses/` and `records/`. The case organizations are hypothetical; replace their inputs and supply current original evidence for a real organization.
