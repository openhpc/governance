#!/usr/bin/env python3
"""Render TSC.md from tsc.yaml.

Usage: ./scripts/render-tsc.py [--check]

With --check the script exits non-zero if TSC.md is out of date instead
of rewriting it (useful in CI).
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ROLE_NAMES = {
    "project-lead": "Project Lead",
    "interim-project-lead": "Interim Project Lead",
    "technical-lead": "Technical Lead",
    "maintainer": "Maintainer",
    "end-user-representative": "End-User/Site Representative",
    "component-development-representative": "Component Development Representative",
    "testing-coordinator": "Testing Coordinator",
    "member": "Member",
}


def render(data):
    current, *previous = data["terms"]
    out = [
        "# OpenHPC Technical Steering Committee",
        "",
        "<!-- Generated from tsc.yaml by scripts/render-tsc.py. Do not edit. -->",
        "",
        f"Current term: **{current['term']}** ({current['start']} to {current['end']}).",
        "",
        "The TSC is the technical governing body of OpenHPC; see",
        "[GOVERNANCE.md](GOVERNANCE.md) for its responsibilities and",
        "[TSC-Election-Process.md](TSC-Election-Process.md) for how members",
        "are selected. The machine-readable source for this list is",
        "[tsc.yaml](tsc.yaml).",
        "",
        "## Members",
        "",
        "| Name | Affiliation | Roles |",
        "| --- | --- | --- |",
    ]
    for m in sorted(current["members"], key=lambda m: m["name"].split()[-1]):
        roles = ", ".join(ROLE_NAMES.get(r, r) for r in m["roles"])
        out.append(f"| {m['name']} | {m['affiliation']} | {roles} |")
    support = current.get("linux-foundation-support", [])
    if support:
        out += ["", "## Linux Foundation Support", ""]
        for s in support:
            out.append(f"* {s['name']} ({s['role']})")
    out += ["", "## Previous Terms", ""]
    for t in previous:
        out.append(f"* [{t['term']}](history/TSC-{t['term']}.md)")
    return "\n".join(out) + "\n"


def main():
    data = yaml.safe_load((ROOT / "tsc.yaml").read_text())
    text = render(data)
    target = ROOT / "TSC.md"
    if "--check" in sys.argv[1:]:
        if target.exists() and target.read_text() == text:
            return 0
        print("TSC.md is out of date; run scripts/render-tsc.py", file=sys.stderr)
        return 1
    target.write_text(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
