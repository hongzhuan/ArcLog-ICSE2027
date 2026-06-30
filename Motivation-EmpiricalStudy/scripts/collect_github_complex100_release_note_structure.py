import csv
import importlib.util
import json
import os
import re
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


BASE_DIR = Path("paper-writing/industrial-release-note-structure-study")
PREV_SCRIPT = BASE_DIR / "collect_github_top100_release_note_structure.py"
OUT_DIR = BASE_DIR / "github_complex100"
CACHE_DIR = OUT_DIR / "cache"
TARGET_ACCEPTED = 100
PER_PAGE = 100
PAGES_PER_QUERY = 3

BASE_QUERY = "stars:>1000 size:>50000 archived:false fork:false"
MIN_SIZE_KB = 50_000
MIN_COMMITS = 2_000

ALLOWED_LANGUAGES = {
    "C", "C++", "Go", "Java", "Rust", "Python", "TypeScript", "JavaScript",
    "Scala", "Kotlin", "C#", "PHP", "Ruby", "Dart", "Swift", "Erlang",
    "Elixir", "Clojure", "Objective-C", "Lua",
}

DOMAIN_QUERIES = [
    ("database", "topic:database"),
    ("storage", "topic:storage"),
    ("distributed-systems", "topic:distributed-systems"),
    ("cloud-native", "topic:cloud-native"),
    ("kubernetes", "topic:kubernetes"),
    ("container", "topic:container"),
    ("devops", "topic:devops"),
    ("networking", "topic:networking"),
    ("proxy", "topic:proxy"),
    ("web-server", "topic:webserver"),
    ("observability", "topic:observability"),
    ("monitoring", "topic:monitoring"),
    ("message-queue", "topic:message-queue"),
    ("data-processing", "topic:data-processing"),
    ("big-data", "topic:big-data"),
    ("compiler", "topic:compiler"),
    ("programming-language", "topic:programming-language"),
    ("runtime", "topic:runtime"),
    ("operating-system", "topic:operating-system"),
    ("kernel", "topic:kernel"),
    ("security", "topic:security"),
    ("cryptography", "topic:cryptography"),
    ("blockchain", "topic:blockchain"),
    ("machine-learning-system", "topic:machine-learning"),
    ("ml-infrastructure", "topic:mlops"),
    ("server", "topic:server"),
    ("search-engine", "topic:search-engine"),
]

COMPLEX_DOMAIN_TERMS = {
    "database", "storage", "distributed", "cloud", "kubernetes", "container",
    "devops", "network", "proxy", "server", "observability", "monitoring",
    "queue", "stream", "data", "compiler", "runtime", "kernel", "operating",
    "security", "crypto", "blockchain", "machine-learning", "mlops", "search",
    "engine", "infrastructure", "platform",
}

STRICT_IMPORTANCE_TERMS = [
    "highlight", "highlights", "notable", "major", "breaking", "incompatible",
    "security", "migration", "upgrade", "deprecation", "deprecated",
    "compatibility", "important", "what's new", "whats new",
]

ORDINARY_TERMS = [
    "bug fix", "bug fixes", "fixes", "fixed", "changelog", "commits",
    "minor", "other changes", "other", "misc", "documentation", "docs",
    "maintenance", "dependencies", "contributors",
]

MODULE_TERMS = [
    "api", "abi", "server", "client", "core", "runtime", "compiler",
    "storage", "database", "network", "proxy", "gateway", "scheduler",
    "controller", "operator", "driver", "drivers", "plugin", "plugins",
    "connector", "connectors", "sql", "query", "parser", "engine",
    "frontend", "backend", "auth", "security", "tls", "ssl", "http",
    "grpc", "kubernetes", "docker", "container", "linux", "windows",
    "macos", "android", "ios", "dashboard", "ui", "cli", "sdk",
    "library", "libraries", "package", "build", "install", "deployment",
    "distributed", "cluster", "node", "worker", "manager", "storage",
    "filesystem", "cache", "stream", "model", "serving", "inference",
]

GENERIC_TYPE_HEADINGS = {
    "added", "changed", "fixed", "removed", "features", "feature", "bug fixes",
    "fixes", "enhancements", "improvements", "documentation", "docs",
    "tests", "maintenance", "dependencies", "chores", "refactor",
}


def load_prev():
    spec = importlib.util.spec_from_file_location("top100_collector", PREV_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.OUT_DIR = OUT_DIR
    module.CACHE_DIR = CACHE_DIR
    return module


def ensure_dirs():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


def request_json(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ArcRN-github-complex100-release-note-study/0.1",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    with urlopen(req, timeout=40) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def search_domain_candidates():
    all_repos = {}
    for domain, domain_query in DOMAIN_QUERIES:
        for page in range(1, PAGES_PER_QUERY + 1):
            q = f"{BASE_QUERY} {domain_query}"
            url = "https://api.github.com/search/repositories?" + urlencode({
                "q": q,
                "sort": "stars",
                "order": "desc",
                "per_page": str(PER_PAGE),
                "page": str(page),
            })
            try:
                data = request_json(url)
            except Exception as exc:
                print(f"search failed {domain} page {page}: {type(exc).__name__}")
                continue
            for repo in data.get("items", []):
                item = all_repos.setdefault(repo["full_name"], repo)
                domains = set(item.get("_matched_domains", []))
                domains.add(domain)
                item["_matched_domains"] = sorted(domains)
            print(f"{domain} page {page}: unique candidates={len(all_repos)}")
            time.sleep(0.2)
    return sorted(all_repos.values(), key=lambda r: r.get("stargazers_count", 0), reverse=True)


def estimate_commit_count(full_name: str, default_branch: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ArcRN-github-complex100-release-note-study/0.1",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/repos/{full_name}/commits?sha={quote(default_branch, safe='')}&per_page=1"
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=40) as response:
            link = response.headers.get("Link", "")
            match = re.search(r"[?&]page=(\d+)>;\s*rel=\"last\"", link)
            if match:
                return int(match.group(1))
            data = json.loads(response.read().decode("utf-8", errors="replace"))
            return len(data)
    except Exception:
        return None


def is_non_software(prev, repo):
    reason = prev.is_likely_non_software(repo)
    if reason:
        return reason
    language = repo.get("language")
    if language not in ALLOWED_LANGUAGES:
        return f"language_not_allowed:{language or 'none'}"
    text = " ".join([
        repo["full_name"].lower(),
        (repo.get("description") or "").lower(),
        " ".join(repo.get("topics") or []).lower(),
        " ".join(repo.get("_matched_domains", [])).lower(),
    ])
    if not any(term in text for term in COMPLEX_DOMAIN_TERMS):
        return "no_complex_system_domain_signal"
    return None


def heading_titles(headings):
    return [title for _, title in headings]


def low(text):
    return text.lower()


def strict_importance_split(headings, text):
    titles = [low(t) for t in heading_titles(headings)]
    joined = "\n".join(titles)
    has_important = any(term in joined for term in STRICT_IMPORTANCE_TERMS)
    has_ordinary = any(term in joined for term in ORDINARY_TERMS)
    return has_important and has_ordinary


def broad_structured(headings):
    titles = [low(t).strip(" :-") for t in heading_titles(headings)]
    if len(titles) >= 4:
        return True
    return sum(1 for t in titles if t in GENERIC_TYPE_HEADINGS) >= 2


def module_organization(headings):
    titles = [low(t).strip(" :-") for t in heading_titles(headings)]
    module_hits = 0
    for title in titles:
        if title in GENERIC_TYPE_HEADINGS:
            continue
        if any(term in title for term in MODULE_TERMS):
            module_hits += 1
    if module_hits >= 2:
        return True
    concrete = [
        t for t in titles
        if len(t) > 2
        and t not in GENERIC_TYPE_HEADINGS
        and not re.fullmatch(r"v?\d+(\.\d+){1,4}.*", t)
        and "what's changed" not in t
        and "new contributors" not in t
    ]
    return len(concrete) >= 6 and module_hits >= 1


def main():
    ensure_dirs()
    prev = load_prev()
    prev.OUT_DIR = OUT_DIR
    prev.CACHE_DIR = CACHE_DIR
    prev.ensure_dirs()

    candidates = search_domain_candidates()
    accepted = []
    excluded = []
    candidate_rows = []

    for idx, repo in enumerate(candidates, start=1):
        row = {
            "candidate_rank": idx,
            "full_name": repo["full_name"],
            "html_url": repo["html_url"],
            "stars": repo["stargazers_count"],
            "forks": repo.get("forks_count", ""),
            "language": repo.get("language") or "",
            "size_kb": repo.get("size") or "",
            "default_branch": repo.get("default_branch") or "",
            "description": repo.get("description") or "",
            "topics": ";".join(repo.get("topics") or []),
            "matched_domains": ";".join(repo.get("_matched_domains") or []),
        }
        candidate_rows.append(row)

        if len(accepted) >= TARGET_ACCEPTED:
            continue

        reason = is_non_software(prev, repo)
        if reason:
            excluded.append({**row, "reason": reason})
            continue
        if int(repo.get("size") or 0) < MIN_SIZE_KB:
            excluded.append({**row, "reason": "size_below_threshold"})
            continue

        commit_count = estimate_commit_count(repo["full_name"], repo.get("default_branch") or "master")
        if commit_count is None or commit_count < MIN_COMMITS:
            excluded.append({**row, "commit_count_estimate": commit_count or "", "reason": "commit_count_below_threshold_or_unknown"})
            continue

        try:
            evidence = prev.fetch_release_note_evidence(repo)
        except Exception as exc:
            excluded.append({**row, "commit_count_estimate": commit_count, "reason": f"evidence_fetch_failed:{type(exc).__name__}"})
            continue
        if evidence is None:
            excluded.append({**row, "commit_count_estimate": commit_count, "reason": "no_release_note_evidence_detected"})
            continue

        headings = prev.extract_headings(evidence["evidence_text"])
        hits = prev.keyword_hits(evidence["evidence_text"])
        important = strict_importance_split(headings, evidence["evidence_text"])
        module = module_organization(headings)
        broad = broad_structured(headings)
        accepted_row = {
            "sample_rank": len(accepted) + 1,
            **row,
            "commit_count_estimate": commit_count,
            "evidence_type": evidence["evidence_type"],
            "evidence_url": evidence["evidence_url"],
            "evidence_title": evidence["evidence_title"],
            "heading_count": len(headings),
            "headings": " | ".join(heading_titles(headings)[:40]),
            "important_terms": ";".join(hits["important_terms"]),
            "ordinary_terms": ";".join(hits["ordinary_terms"]),
            "module_terms": ";".join(hits["module_terms"]),
            "strict_important_ordinary_split_reviewed": "yes" if important else "no",
            "module_component_organization_reviewed": "yes" if module else "no",
            "broad_typed_or_structured_reviewed": "yes" if broad else "no",
            "both_strict_important_and_module_reviewed": "yes" if important and module else "no",
            "both_broad_structure_and_module_reviewed": "yes" if broad and module else "no",
        }
        accepted.append(accepted_row)
        print(f"accepted {len(accepted):03d}: {repo['full_name']} commits={commit_count} domains={accepted_row['matched_domains']}")

    def write_csv(path, rows):
        if not rows:
            return
        fields = list(rows[0].keys())
        with path.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    write_csv(OUT_DIR / "github_complex_candidates.csv", candidate_rows)
    write_csv(OUT_DIR / "github_complex100_reviewed_structure_coding.csv", accepted)
    write_csv(OUT_DIR / "github_complex_excluded.csv", excluded)

    denom = len(accepted) or 1
    summary = {
        "collection_date": "2026-06-18",
        "target_accepted": TARGET_ACCEPTED,
        "candidate_repositories": len(candidates),
        "accepted_repositories": len(accepted),
        "excluded_repositories_seen": len(excluded),
        "base_query": BASE_QUERY,
        "min_size_kb": MIN_SIZE_KB,
        "min_commits": MIN_COMMITS,
        "strict_important_ordinary_split_yes": sum(1 for r in accepted if r["strict_important_ordinary_split_reviewed"] == "yes"),
        "module_component_organization_yes": sum(1 for r in accepted if r["module_component_organization_reviewed"] == "yes"),
        "broad_typed_or_structured_yes": sum(1 for r in accepted if r["broad_typed_or_structured_reviewed"] == "yes"),
        "both_strict_important_and_module_yes": sum(1 for r in accepted if r["both_strict_important_and_module_reviewed"] == "yes"),
        "both_broad_structure_and_module_yes": sum(1 for r in accepted if r["both_broad_structure_and_module_reviewed"] == "yes"),
    }
    for key in [
        "strict_important_ordinary_split_yes",
        "module_component_organization_yes",
        "broad_typed_or_structured_yes",
        "both_strict_important_and_module_yes",
        "both_broad_structure_and_module_yes",
    ]:
        summary[key + "_pct"] = round(summary[key] / denom * 100, 1)

    (OUT_DIR / "github_complex100_reviewed_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    domain_counts = {}
    for row in accepted:
        for d in row["matched_domains"].split(";"):
            if d:
                domain_counts[d] = domain_counts.get(d, 0) + 1

    md = [
        "# GitHub Complex-System Top-100 Release Note Structure Study",
        "",
        "## Sampling Protocol",
        "",
        "- Source: GitHub REST Search API.",
        f"- Base query: `{BASE_QUERY}`.",
        f"- Additional complexity filters: repository size >= {MIN_SIZE_KB} KB and estimated commits >= {MIN_COMMITS}.",
        "- Candidate repositories are collected from system-domain topic queries, including database, storage, distributed systems, cloud-native, containers, networking, compilers/runtimes, operating systems/kernels, observability, data processing, security/cryptography, blockchain, and ML infrastructure.",
        "- Non-software repositories, books, tutorials, awesome lists, roadmaps, and repositories without release-note evidence are excluded.",
        "- Evidence priority: GitHub Releases first, then repository changelog/news/release-note files.",
        "",
        "## Results",
        "",
        "| Metric | Count | Percentage |",
        "| --- | ---: | ---: |",
        f"| Accepted repositories | {len(accepted)} | - |",
        f"| Strict important/ordinary split | {summary['strict_important_ordinary_split_yes']}/{denom} | {summary['strict_important_ordinary_split_yes_pct']}% |",
        f"| Module/component organization | {summary['module_component_organization_yes']}/{denom} | {summary['module_component_organization_yes_pct']}% |",
        f"| Broad typed/structured release note | {summary['broad_typed_or_structured_yes']}/{denom} | {summary['broad_typed_or_structured_yes_pct']}% |",
        f"| Both strict split and module organization | {summary['both_strict_important_and_module_yes']}/{denom} | {summary['both_strict_important_and_module_yes_pct']}% |",
        f"| Both broad structure and module organization | {summary['both_broad_structure_and_module_yes']}/{denom} | {summary['both_broad_structure_and_module_yes_pct']}% |",
        "",
        "## Domain Coverage",
        "",
    ]
    for domain, count in sorted(domain_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        md.append(f"- {domain}: {count}")
    md.extend([
        "",
        "## Claim Boundary",
        "",
        "This sample is intentionally scoped to large complex software systems. It should not be described as representative of all GitHub repositories. It is suitable for motivating ArcRN's target scenario: complex systems whose release notes often require importance layering and module/component-oriented organization.",
    ])
    (OUT_DIR / "summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
