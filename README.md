# OpenHPC Governance

This repository holds the governance documentation of the
[OpenHPC](https://openhpc.community) project. It was moved here from the
[OpenHPC wiki](https://github.com/openhpc/ohpc/wiki) in October 2026.

| Document | Content |
| --- | --- |
| [GOVERNANCE.md](GOVERNANCE.md) | Governance overview: Governing Board and Technical Steering Committee (TSC) |
| [TSC.md](TSC.md) | Current TSC members (generated from [tsc.yaml](tsc.yaml)) |
| [tsc.yaml](tsc.yaml) | Machine-readable TSC roster, current and all previous terms |
| [TSC-Election-Process.md](TSC-Election-Process.md) | TSC membership, participation and selection process |
| [TSC-Meetings.md](TSC-Meetings.md) | Meeting schedule, call details and slides of past meetings |
| [history/](history/) | TSC membership lists of previous terms |
| [meetings/](meetings/) | Slides of past TSC meetings |

The [OpenHPC Project Charter](https://charter.openhpc.community/) is the
authoritative document for the proceedings of the Governing Board and the TSC.

## Updating the TSC roster

Edit `tsc.yaml` and regenerate `TSC.md`:

```
./scripts/render-tsc.py
```

`./scripts/render-tsc.py --check` verifies that `TSC.md` matches `tsc.yaml`.
A GitHub Actions workflow runs this check on every push and pull request,
so a pull request that edits `tsc.yaml` must also include the regenerated
`TSC.md`.

## License

The contents of this repository are licensed under the
[Apache License 2.0](LICENSE).
