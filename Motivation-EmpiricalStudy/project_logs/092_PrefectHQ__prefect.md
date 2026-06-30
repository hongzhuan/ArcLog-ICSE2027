# Project Log: 92. PrefectHQ/prefect

## Repository Metadata

| Field | Value |
| --- | --- |
| Repository | `PrefectHQ/prefect` |
| GitHub URL | https://github.com/PrefectHQ/prefect |
| Stars | 22634 |
| Forks | 2341 |
| Primary language | Python |
| Repository size (KB) | 224694 |
| Estimated commits | 21651 |
| Matched domains | observability |
| Default branch | main |

## Release-Note Evidence

| Field | Value |
| --- | --- |
| Initial evidence type | github_release |
| Initial evidence URL | https://github.com/PrefectHQ/prefect/releases/tag/3.7.5.dev5 |
| Initial evidence title | 3.7.5.dev5: Nightly Development Release |
| Rich evidence found | yes |
| Rich evidence type | repo_file |
| Rich evidence URL | https://raw.githubusercontent.com/PrefectHQ/prefect/main/.claude/skills/document-changes/SKILL.md |
| Rich evidence title | .claude/skills/document-changes/SKILL.md |
| Rich evidence score | 169.38 |
| Rich heading count | 20 |
| Rich bullet count | 81 |
| Rich text length | 9038 |

## Coding Decisions

| Coding item | Value |
| --- | --- |
| Non-flat / typed or structured release note | yes |
| Strict important vs. routine split | yes |
| Module/component/subsystem organization | yes |
| Both strict split and module organization | yes |
| Both broad structure and module organization | yes |

## Headings Used as Evidence

- Document Changes
- Modes
- Prerequisites
- Workflow
- 1. Determine the diff
- 2. Extract public API surface changes
- 3. Map changes to existing docs
- 4. Produce output
- Report mode (local dev)
- Documentation Changes Report
- `docs/v3/concepts/flows.mdx`
- `docs/v3/how-to-guides/workflows/retries.mdx`
- Missing coverage
- No changes needed
- Edit mode (CI)
- 5. Quality gate (edit mode only)
- 6. Offer next steps (report mode only)
- Important guidelines
- git diff main...HEAD -- 'src/prefect/' 'src/integrations/'
- `docs/v3/get-started/quickstart.mdx` — references checked, all current
