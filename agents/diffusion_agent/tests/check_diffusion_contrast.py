#!/usr/bin/env python3
"""Check the saved Theranos contrast and the diagnostic regression."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
names = ("primary", "contrast_1", "contrast_2")
responses = {
    name: json.loads((root / "responses" / f"{name}_response.json").read_text())
    for name in names
}
baseline = responses["primary"]
assert json.loads((root / "cases" / "primary.json").read_text())["organization"].startswith("Theranos")
diagnostic = json.loads((root / "responses" / "diagnostic_primary_response.json").read_text())
assert "early majority" in diagnostic["general_et_finding"].lower()
for name, response in responses.items():
    assert response["general_et_finding"] == baseline["general_et_finding"], name
    assert response["application_finding"] == baseline["application_finding"], name
    assert response["evidence"] == baseline["evidence"], name
    assert response["agent"]["version"] == "0.4-student", name
    assert "indeterminate" in response["general_et_finding"].lower(), name
    assert "early majority" in response["general_et_finding"].lower(), name
    assert "unsupported" in response["general_et_finding"].lower(), name
    assert "cannot show platform penetration" in response["application_finding"], name
    for factor in (
        "Relative advantage", "Compatibility", "Complexity",
        "Trialability", "Observability"
    ):
        assert factor in response["application_finding"], (name, factor)
    assert len(response["evidence"]) >= 6, name

recommendations = {
    name: response["recommendation_management_implication"]
    for name, response in responses.items()
}
assert len(set(recommendations.values())) == len(names)
assert "halted broad clinical expansion immediately" in recommendations["primary"]
assert "withheld further center expansion" in recommendations["contrast_1"]
assert "reject clinical use" in recommendations["contrast_2"]
print("THERANOS CONTRAST PASSED: 3 contexts; evidence stable; decisions differ; overclaim rejected")
