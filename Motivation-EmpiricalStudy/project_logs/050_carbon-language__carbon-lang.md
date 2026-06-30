# Project Log: 50. carbon-language/carbon-lang

## Repository Metadata

| Field | Value |
| --- | --- |
| Repository | `carbon-language/carbon-lang` |
| GitHub URL | https://github.com/carbon-language/carbon-lang |
| Stars | 33839 |
| Forks | 1537 |
| Primary language | C++ |
| Repository size (KB) | 113739 |
| Estimated commits | 5423 |
| Matched domains | compiler;programming-language |
| Default branch | trunk |

## Release-Note Evidence

| Field | Value |
| --- | --- |
| Initial evidence type | github_release |
| Initial evidence URL | https://github.com/carbon-language/carbon-lang/releases/tag/v0.0.0-0.nightly.2026.06.18 |
| Initial evidence title | Nightly build 2026.06.18 |
| Rich evidence found | yes |
| Rich evidence type | repo_file |
| Rich evidence URL | https://raw.githubusercontent.com/carbon-language/carbon-lang/trunk/proposals/p001344-remove-llvm-from-the-repository-and-clean-up-history.md |
| Rich evidence title | proposals/p001344-remove-llvm-from-the-repository-and-clean-up-history.md |
| Rich evidence score | 100.58 |
| Rich heading count | 25 |
| Rich bullet count | 62 |
| Rich text length | 15866 |

## Coding Decisions

| Coding item | Value |
| --- | --- |
| Non-flat / typed or structured release note | yes |
| Strict important vs. routine split | no |
| Module/component/subsystem organization | no |
| Both strict split and module organization | no |
| Both broad structure and module organization | no |

## Headings Used as Evidence

- Remove LLVM from the repository, and clean up history.
- Table of contents
- Problem
- Proposal
- Details
- Implementation
- Patching LLVM
- Updating forks and clones
- Archive your existing fork and clones
- Create a fresh fork and clone
- Porting in-progress branches from your archived clone
- If your old clone is in the `archived-carbon-lang` directory and your new
- clone is in `carbon-lang`, both of them on the `trunk` branch:
- Updating pending PRs
- Review comments may be disrupted
- Rationale
- Alternatives considered
- Do nothing
- Don't rewrite the repository history.
- Go back to submodules
- Rename the repository, and create a new one
- Manually extract and archive some review comments
- git remote set-url origin git@github.com:$USER/archived-carbon-lang.git git@github.com:$USER/carbon-lang.git
- git push --mirror origin
- git commit
