# SemArc Runtime

This directory contains the packaged SemArc runtime used by ArcLog to generate
architecture-level module artifacts. Runtime caches, extracted results, LLM logs,
and previous outputs are intentionally excluded.

The ArcLog pipeline calls `SemArcArcRN.exe` with `--core-outputs-only` and
`--emit-progress`.
