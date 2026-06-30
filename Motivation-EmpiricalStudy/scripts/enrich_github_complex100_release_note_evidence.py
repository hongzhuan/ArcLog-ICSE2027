import csv
import importlib.util
import json
import math
import re
from pathlib import Path
from urllib.parse import quote


BASE = Path("paper-writing/industrial-release-note-structure-study")
PREV_SCRIPT = BASE / "collect_github_top100_release_note_structure.py"
COMPLEX_SCRIPT = BASE / "collect_github_complex100_release_note_structure.py"
IN_CSV = BASE / "github_complex100" / "github_complex100_reviewed_structure_coding.csv"
OUT_DIR = BASE / "github_complex100_rich_evidence"
OUT_CSV = OUT_DIR / "github_complex100_rich_evidence_reviewed_coding.csv"
OUT_JSON = OUT_DIR / "github_complex100_rich_evidence_summary.json"
OUT_MD = OUT_DIR / "summary.md"
ENABLE_EXTERNAL_LINKS = False


BAD_PATH_TOKENS = {
    "release-process", "process", "install", "installation", "quickstart",
    "contributing", "developer", "template", "workflow", "governance",
    "policy", "roadmap",
}

GOOD_FILE_TOKENS = {
    "changelog", "change-log", "changes", "release-notes", "release_notes",
    "releasenotes", "releases", "news", "history",
}


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bullet_count(text):
    return sum(1 for line in text.splitlines() if re.match(r"^\s*([-*+]|\d+\.)\s+", line))


def link_urls(text):
    return re.findall(r"https?://[^\s)>\"]+", text or "")


def path_candidates(paths):
    candidates = []
    for path in paths:
        low = path.lower()
        if not low.endswith((".md", ".rst", ".txt", ".adoc")):
            continue
        if any(tok in low for tok in BAD_PATH_TOKENS):
            continue
        basename = low.rsplit("/", 1)[-1]
        if any(tok in low for tok in GOOD_FILE_TOKENS):
            depth = len(path.split("/"))
            # Accept versioned changelogs under a shallow CHANGELOG/ directory.
            if depth <= 4 or "changelog" in basename or "release" in basename:
                candidates.append(path)
    candidates.sort(key=lambda p: (len(p.split("/")), len(p), p.lower()))
    return candidates[:12]


def score_evidence(prev, complex_mod, text):
    headings = prev.extract_headings(text)
    titles = " | ".join(t for _, t in headings).lower()
    strict = complex_mod.strict_importance_split(headings, text)
    module = complex_mod.module_organization(headings)
    broad = complex_mod.broad_structured(headings)
    bullets = bullet_count(text)
    length_score = min(25, math.log(max(len(text), 1), 1.6))
    score = length_score + min(40, len(headings) * 2) + min(30, bullets / 2)
    if strict:
        score += 35
    if module:
        score += 35
    if broad:
        score += 10
    if any(term in titles for term in ["release process", "install", "download", "verification", "checksums"]):
        score -= 35
    return score, headings, strict, module, broad


def fetch_rich_evidence(prev, complex_mod, row):
    full_name = row["full_name"]
    default_branch = row["default_branch"] or "master"
    evidence_candidates = []

    for rel in prev.get_releases(full_name)[:8]:
        body = rel.get("body") or ""
        title = rel.get("name") or rel.get("tag_name") or "GitHub Release"
        if len(body.strip()) >= 120:
            text = f"# {title}\n\n{body}"
            evidence_candidates.append({
                "type": "github_release",
                "url": rel.get("html_url") or "",
                "title": title,
                "text": text[:250000],
            })
        if ENABLE_EXTERNAL_LINKS:
            for url in link_urls(body)[:2]:
                low = url.lower()
                if any(tok in low for tok in ["release", "changelog", "change-log", "blog", "news"]):
                    try:
                        text = prev.request_text(url)
                        if len(text.strip()) >= 500:
                            evidence_candidates.append({
                                "type": "external_link_from_github_release",
                                "url": url,
                                "title": url,
                                "text": text[:250000],
                            })
                    except Exception:
                        pass

    paths = prev.get_tree_paths(full_name, default_branch)
    for path in path_candidates(paths):
        raw_url = f"https://raw.githubusercontent.com/{full_name}/{quote(default_branch, safe='')}/{quote(path)}"
        try:
            text = prev.request_text(raw_url)
            if len(text.strip()) >= 300:
                evidence_candidates.append({
                    "type": "repo_file",
                    "url": raw_url,
                    "title": path,
                    "text": text[:250000],
                })
        except Exception:
            pass

    best = None
    for ev in evidence_candidates:
        score, headings, strict, module, broad = score_evidence(prev, complex_mod, ev["text"])
        ev.update({
            "score": score,
            "headings": headings,
            "strict": strict,
            "module": module,
            "broad": broad,
            "bullet_count": bullet_count(ev["text"]),
            "text_len": len(ev["text"]),
        })
        if best is None or ev["score"] > best["score"]:
            best = ev
    return best


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    prev = load_module(PREV_SCRIPT, "prev_collector")
    complex_mod = load_module(COMPLEX_SCRIPT, "complex_collector")
    prev.OUT_DIR = OUT_DIR
    prev.CACHE_DIR = OUT_DIR / "cache"
    prev.ensure_dirs()

    rows = list(csv.DictReader(IN_CSV.open(encoding="utf-8-sig")))
    out_rows = []
    for idx, row in enumerate(rows, start=1):
        ev = fetch_rich_evidence(prev, complex_mod, row)
        if not ev:
            out = dict(row)
            out.update({
                "rich_evidence_found": "no",
                "rich_evidence_type": "",
                "rich_evidence_url": "",
                "rich_evidence_title": "",
                "rich_heading_count": 0,
                "rich_headings": "",
                "strict_important_ordinary_split_reviewed": "no",
                "module_component_organization_reviewed": "no",
                "broad_typed_or_structured_reviewed": "no",
                "both_strict_important_and_module_reviewed": "no",
                "both_broad_structure_and_module_reviewed": "no",
            })
        else:
            headings = ev["headings"]
            out = dict(row)
            out.update({
                "rich_evidence_found": "yes",
                "rich_evidence_type": ev["type"],
                "rich_evidence_url": ev["url"],
                "rich_evidence_title": ev["title"],
                "rich_evidence_score": round(ev["score"], 2),
                "rich_heading_count": len(headings),
                "rich_bullet_count": ev["bullet_count"],
                "rich_text_len": ev["text_len"],
                "rich_headings": " | ".join(t for _, t in headings[:50]),
                "strict_important_ordinary_split_reviewed": "yes" if ev["strict"] else "no",
                "module_component_organization_reviewed": "yes" if ev["module"] else "no",
                "broad_typed_or_structured_reviewed": "yes" if ev["broad"] else "no",
                "both_strict_important_and_module_reviewed": "yes" if ev["strict"] and ev["module"] else "no",
                "both_broad_structure_and_module_reviewed": "yes" if ev["broad"] and ev["module"] else "no",
            })
        out_rows.append(out)
        print(f"{idx:03d} {row['full_name']} rich={out['rich_evidence_found']} strict={out['strict_important_ordinary_split_reviewed']} module={out['module_component_organization_reviewed']} type={out.get('rich_evidence_type','')}")

    fields = list(out_rows[0].keys())
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out_rows)

    denom = len(out_rows)
    summary = {
        "review_date": "2026-06-18",
        "accepted_repositories": denom,
        "rich_evidence_found": sum(1 for r in out_rows if r["rich_evidence_found"] == "yes"),
        "strict_important_ordinary_split_yes": sum(1 for r in out_rows if r["strict_important_ordinary_split_reviewed"] == "yes"),
        "module_component_organization_yes": sum(1 for r in out_rows if r["module_component_organization_reviewed"] == "yes"),
        "broad_typed_or_structured_yes": sum(1 for r in out_rows if r["broad_typed_or_structured_reviewed"] == "yes"),
        "both_strict_important_and_module_yes": sum(1 for r in out_rows if r["both_strict_important_and_module_reviewed"] == "yes"),
        "both_broad_structure_and_module_yes": sum(1 for r in out_rows if r["both_broad_structure_and_module_reviewed"] == "yes"),
    }
    for key in [
        "strict_important_ordinary_split_yes",
        "module_component_organization_yes",
        "broad_typed_or_structured_yes",
        "both_strict_important_and_module_yes",
        "both_broad_structure_and_module_yes",
        "rich_evidence_found",
    ]:
        summary[key + "_pct"] = round(summary[key] / denom * 100, 1)

    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    md = [
        "# GitHub Complex-System Top-100 Rich Evidence Review",
        "",
        "This pass reselects the richest release-note evidence for each accepted repository instead of always preferring GitHub Releases. Candidate evidence includes GitHub release bodies, release/changelog files in the repository, and official-looking release/blog/changelog links found in GitHub release bodies.",
        "",
        "| Metric | Count | Percentage |",
        "| --- | ---: | ---: |",
        f"| Accepted repositories | {denom} | - |",
        f"| Rich evidence found | {summary['rich_evidence_found']}/{denom} | {summary['rich_evidence_found_pct']}% |",
        f"| Strict important/ordinary split | {summary['strict_important_ordinary_split_yes']}/{denom} | {summary['strict_important_ordinary_split_yes_pct']}% |",
        f"| Module/component organization | {summary['module_component_organization_yes']}/{denom} | {summary['module_component_organization_yes_pct']}% |",
        f"| Broad typed/structured release note | {summary['broad_typed_or_structured_yes']}/{denom} | {summary['broad_typed_or_structured_yes_pct']}% |",
        f"| Both strict split and module organization | {summary['both_strict_important_and_module_yes']}/{denom} | {summary['both_strict_important_and_module_yes_pct']}% |",
        f"| Both broad structure and module organization | {summary['both_broad_structure_and_module_yes']}/{denom} | {summary['both_broad_structure_and_module_yes_pct']}% |",
        "",
        "Claim boundary: this is a complex-system sample, not a general GitHub sample. The coding is based on the best automatically discovered official release-note evidence and should be manually audited before being used as a final empirical result.",
    ]
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
