#!/usr/bin/env python3
"""Check the saved three-context diffusion outputs without editing frozen tools."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
names = ("primary", "contrast_1", "contrast_2")
responses = {
    name: json.loads((root / "responses" / f"{name}_response.json").read_text())
    for name in names
}
baseline = responses["primary"]
for name, response in responses.items():
    assert response["general_et_finding"] == baseline["general_et_finding"], name
    assert response["application_finding"] == baseline["application_finding"], name
    assert response["evidence"] == baseline["evidence"], name
    assert "indeterminate" in response["general_et_finding"].lower(), name
    for factor in (
        "Relative advantage", "Compatibility", "Complexity",
        "Trialability", "Observability"
    ):
        assert factor in response["application_finding"], (name, factor)
    assert len(response["evidence"]) >= 3, name

recommendations = {
    name: response["recommendation_management_implication"]
    for name, response in responses.items()
}
assert len(set(recommendations.values())) == len(names)
assert "6-12 months" in recommendations["primary"]
assert "0-3 months" in recommendations["contrast_1"]
assert "3-6 months" in recommendations["contrast_2"]
print("CONTEXT CONTRAST PASSED: 3 cases; general/application/evidence stable; timing differs")
