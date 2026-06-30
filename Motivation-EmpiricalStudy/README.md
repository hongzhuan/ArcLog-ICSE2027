# Motivation Empirical Study

This folder contains the local appendix data for the Motivation empirical study used in the ArcRN ICSE 2027 paper draft.

## Study Purpose

The study checks whether release notes in large complex software systems are commonly more structured than a flat commit or PR list. The supported paper claim is: complex-system release notes often highlight important changes and organize changes by modules, components, or subsystems.

## Dataset Construction

The candidate pool was collected from GitHub repositories that satisfy these filters:

- non-fork and non-archived repositories;
- at least 1,000 stars;
- repository size of at least 50 MB;
- an estimated commit count of at least 2,000;
- topic, language, or repository evidence indicating a complex software-system domain;
- traceable official release-note, changelog, or release artifact evidence.

This produced 1,697 candidate repositories. From these candidates, 100 large complex software systems spanning multiple system domains were selected for repository-level release-note structure coding.

## Coding Rules

Each accepted repository was coded from an official release-note or changelog artifact. The coding fields are:

- `broad_typed_or_structured_reviewed`: whether the artifact uses a non-flat structure, typed sections, or any explicit release-note organization beyond a plain list.
- `strict_important_ordinary_split_reviewed`: whether the artifact explicitly separates important/high-impact changes from routine or ordinary changes.
- `module_component_organization_reviewed`: whether the artifact organizes release contents by module, component, subsystem, service, platform area, or equivalent system unit.
- `both_strict_important_and_module_reviewed`: whether both the important-vs-routine split and module/component organization appear.
- `both_broad_structure_and_module_reviewed`: whether both a non-flat/typed structure and module/component organization appear.

## Results

| Metric | Count | Denominator | Percentage |
| --- | ---: | ---: | ---: |
| Accepted repositories with traceable rich evidence | 100 | 100 | 100.0% |
| Non-flat / typed or structured release note | 94 | 100 | 94.0% |
| Important-vs-routine split | 49 | 100 | 49.0% |
| Module/component/subsystem organization | 59 | 100 | 59.0% |
| Both important split and module organization | 38 | 100 | 38.0% |
| Both non-flat structure and module organization | 59 | 100 | 59.0% |

## Folder Structure

- `data/repository_coding.csv`: final 100-repository coding table.
- `data/candidate_collection_stats.csv`: numeric counts for candidate collection and accepted-sample construction.
- `data/exclusion_reason_counts.csv`: aggregate counts by exclusion reason.
- `data/summary_metrics.csv`: numeric result metrics only.
- `data/domain_counts.csv`: matched domain counts for the accepted 100 repositories.
- `data/project_log_index.csv`: index from each accepted repository to its project log.
- `project_logs/`: one evidence log per accepted repository.
- `scripts/`: data collection and enrichment scripts.
- `workbook/motivation_empirical_study_data.xlsx`: Excel workbook containing data sheets only. Explanatory text is intentionally kept in this README rather than in workbook sheets.

## Claim Boundary

The study is used as motivation evidence, not as a benchmark or ground truth for release-note generation quality. The percentages support the observation that structured release notes are common in large complex systems; they do not claim that every project always uses the same release-note structure across all versions.
