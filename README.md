# ArcLog Artifact Package

This package contains the anonymized data and source code for ArcLog. The
package is organized to expose only the final audited artifacts needed to
inspect the experiment data and run the method on a repository/version pair.

## Directory Layout

```text
ArcLog-ICSE 2027/
  Data/
    Ground Truth/
    Result/
      ArcLog Release Notes/
      RQ1/
      RQ2/
      RQ3/
      RQ4/
  ArcLog-source code/
  Motivation-EmpiricalStudy/
  Motivation-EmpiricalStudy.zip
```

## Data

- `Data/Ground Truth/<version-pair>/gt_entries.jsonl` stores the audited
  ground-truth entries for each version pair.
- `Data/Ground Truth/<version-pair>/ground_truth.md` stores the rendered
  Markdown version of the same ground truth.
- `Data/Result/ArcLog Release Notes/<version-pair>/final_release_note_traceable.md`
  stores ArcLog's final traceable release note for each version pair, including
  commit and pull-request links.
- `Data/Result/RQ1/` stores the final RQ1 result tables.
- `Data/Result/RQ2/` stores the final RQ2 result tables.
- `Data/Result/RQ3/` stores the final RQ3 result tables.
- `Data/Result/RQ4/` stores the final RQ4 result tables.

The data directory intentionally excludes intermediate logs, temporary model
outputs, batch scripts, private repositories, and previous experiment snapshots.

## Motivation Empirical Study

- `Motivation-EmpiricalStudy/` stores the author-verified appendix data for the
  Motivation section's empirical observation about release-note structure in
  large complex software systems.
- The study starts from 1,697 GitHub candidate repositories and records the
  manually checked coding results for 100 selected large complex software
  systems.
- `Motivation-EmpiricalStudy/README.md` contains the study purpose, dataset
  construction criteria, coding rules, result metrics, folder structure, and
  claim boundary.
- `Motivation-EmpiricalStudy/data/` contains data-only CSV files, including the
  final 100-repository coding table, numeric summary metrics, domain counts,
  candidate-collection counts, exclusion-reason counts, and project-log index.
- `Motivation-EmpiricalStudy/project_logs/` contains one evidence log for each
  accepted repository.
- `Motivation-EmpiricalStudy/workbook/motivation_empirical_study_data.xlsx`
  contains the same data in an Excel workbook with data sheets only; explanatory
  text is kept in the README.
- `Motivation-EmpiricalStudy.zip` is the compressed copy of this directory for
  transfer and archival.

## Source Code

- `ArcLog-source code/README.md` describes how to configure and run ArcLog.
- `ArcLog-source code/requirements.txt` lists the Python dependencies.
- `ArcLog-source code/scripts/` contains runnable entry points and environment
  checks.
- `ArcLog-source code/third_party/` contains the packaged ENRE-CPP and SemArc
  tools required by ArcLog.

