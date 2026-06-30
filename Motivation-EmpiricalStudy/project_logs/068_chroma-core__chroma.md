# Project Log: 68. chroma-core/chroma

## Repository Metadata

| Field | Value |
| --- | --- |
| Repository | `chroma-core/chroma` |
| GitHub URL | https://github.com/chroma-core/chroma |
| Stars | 28467 |
| Forks | 2326 |
| Primary language | Rust |
| Repository size (KB) | 871790 |
| Estimated commits | 4481 |
| Matched domains | database |
| Default branch | main |

## Release-Note Evidence

| Field | Value |
| --- | --- |
| Initial evidence type | github_release |
| Initial evidence URL | https://github.com/chroma-core/chroma/releases/tag/1.5.9 |
| Initial evidence title | 1.5.9 |
| Rich evidence found | yes |
| Rich evidence type | repo_file |
| Rich evidence URL | https://raw.githubusercontent.com/chroma-core/chroma/main/revision_history_function_302b0fcf.plan.md |
| Rich evidence title | revision_history_function_302b0fcf.plan.md |
| Rich evidence score | 136.98 |
| Rich heading count | 40 |
| Rich bullet count | 102 |
| Rich text length | 30614 |

## Coding Decisions

| Coding item | Value |
| --- | --- |
| Non-flat / typed or structured release note | yes |
| Strict important vs. routine split | no |
| Module/component/subsystem organization | yes |
| Both strict split and module organization | no |
| Both broad structure and module organization | yes |

## Headings Used as Evidence

- Revision History Function
- Overview
- Design Goals
- How Version Histories Work
- Architecture
- Input Collection (partial schema -- what the function requires)
- Design
- Resurrection Handling
- Data Model (output collection records)
- Files to Change
- 1. Go constants + migration
- 2. Rust executor implementation
- 3. Registration / dispatch
- 4. API layer (name resolution)
- 5. Python SDK enum
- 6. Codegen (automatic)
- Executor Logic (pseudocode)
- Edge Cases
- Output Collection Schema
- Back-of-Envelope Estimates
- Storage (history collection)
- Memory during compaction
- Throughput
- Configuration (params JSON)
- Thin Facade for Viewing Revisions (Example)
- Reverting to a Previous Version
- Why Record-Only Storage is Cheap
- Test Plan
- Unit Tests (in `revision_history.rs`)
- Integration Test (k8s / Tilt -- following `test_k8s_integration_statistics_function` pattern)
