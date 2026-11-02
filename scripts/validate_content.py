"""Validate structured portfolio content before build."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    errors: list[str] = []
    profile = load(ROOT / "content" / "profile.json")
    experiences = load(ROOT / "content" / "experiences.json")
    evidence = load(ROOT / "content" / "evidence-register.json")
    project_files = sorted((ROOT / "content" / "projects").glob("*.json"))

    for key in ("name", "email", "github", "linkedin", "cv", "text", "education"):
        if key not in profile:
            errors.append(f"profile.json missing {key}")

    for lang in ("fr", "en"):
        if lang not in profile.get("text", {}):
            errors.append(f"profile.text missing {lang}")
        if lang not in profile.get("cv", {}):
            errors.append(f"profile.cv missing {lang}")

    claim_ids = {c["id"] for c in evidence.get("claims", [])}
    projects = {}
    for path in project_files:
        data = load(path)
        projects[data["id"]] = data
        for lang in ("fr", "en"):
            if lang not in data.get("text", {}):
                errors.append(f"{path.name}: text.{lang} missing")
        for cid in data.get("claim_ids", []):
            if cid not in claim_ids:
                errors.append(f"{path.name}: unknown claim_id {cid}")
            else:
                claim = next(c for c in evidence["claims"] if c["id"] == cid)
                if claim.get("status") == "contradicted" and claim.get("public_allowed"):
                    errors.append(f"contradicted claim marked public: {cid}")

    required = {"square-management", "credit-scoring", "brokerflow"}
    missing = required - set(projects)
    if missing:
        errors.append(f"missing featured projects: {sorted(missing)}")

    if not experiences.get("items"):
        errors.append("experiences.json has no items")

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(" -", err)
        return 1

    print(f"OK: validated profile, {len(experiences['items'])} experiences, {len(projects)} projects, {len(claim_ids)} claims")
    return 0


if __name__ == "__main__":
    sys.exit(main())
