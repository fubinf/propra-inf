"""Merge the per-environment reports of the check-example-programs job into one report."""
import re, os

ENVIRONMENTS = [
    ("debian:bookworm", "python3.11", "debian-bookworm"),
    ("debian:trixie",   "python3.13", "debian-trixie"),
    ("ubuntu:24.04",    "python3.12", "ubuntu-24.04"),
]

def parse_block_stats(text):
    """Parse stats from the Block-Level Statistics section only."""
    m = re.search(r'### Block-Level Statistics\n(.*?)(?=\n###|\n##|\Z)', text, re.DOTALL)
    if not m:
        return {}
    section = m.group(1)
    result = {}
    for label, key in [
        ("Total @PROT_SPEC blocks", "total"),
        ("Passed",  "passed"),
        ("Failed",  "failed"),
        ("Manual",  "manual"),
        ("Skip",    "skip"),
    ]:
        mm = re.search(rf'\*\*{re.escape(label)}:\*\* (\d+)', section)
        result[key] = int(mm.group(1)) if mm else 0
    return result

def extract_section(text, heading):
    """Return the content between '## heading' and the next '## ' or '### ' heading."""
    pattern = rf'## {re.escape(heading)}\n(.*?)(?=\n#{{2,3}} |\Z)'
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else ""

reports = {}
for container, python_ver, artifact_id in ENVIRONMENTS:
    path = f"/tmp/artifacts/program-check-reports-{artifact_id}/program_test_report.md"
    if os.path.exists(path):
        with open(path) as f:
            reports[artifact_id] = (container, python_ver, f.read())
    else:
        reports[artifact_id] = (container, python_ver, None)

out = []
out.append("# Program Check Report\n\n")
out.append(
    "This report describes the results of running `sedrila maintainer check-programs` in\n"
    "several different environments as described below.  \n"
    "https://sedrila.readthedocs.io/en/latest/maintainers/#4-program-testing-check-programs  \n"
    "Manual and passed tests are listed only once if all environments agree "
    "(execution times are ignored in that comparison). Failed tests are always listed per environment.\n\n"
)

# --- Environment summary table ---
out.append("## Environment Summary\n\n")
out.append("| Environment | Python | Blocks total | Failed | Manual | Skip | Passed |\n")
out.append("|-------------|--------|-------------:|-------:|-------:|-----:|-------:|\n")
for artifact_id, (container, python_ver, text) in reports.items():
    if text is None:
        out.append(f"| `{container}` | {python_ver} | — | — | — | — | *(no report)* |\n")
        continue
    s = parse_block_stats(text)
    status = "FAIL" if s.get("failed", 0) > 0 else "ok"
    out.append(
        f"| [{status}] `{container}` | {python_ver}"
        f" | {s.get('total', 0)}"
        f" | {s.get('failed', 0)}"
        f" | {s.get('manual', 0)}"
        f" | {s.get('skip', 0)}"
        f" | {s.get('passed', 0)} |\n"
    )
out.append("\n")
out.append(
    "*Blocks* are `@PROT_SPEC` blocks.  \n"
    "*Manual* blocks are not run, see Manual Tests below.  \n"
    "*Skip* blocks have no `@PROT_SPEC` or say `skip=1`: "
    "they are not run and not counted as failures.  \n"
    "`[FAIL]` means at least one block failed.  \n"
    "`no report` means the job produced no report.\n\n"
)

# --- Failed tests (all environments) ---
has_failures_section = False
for artifact_id, (container, python_ver, text) in reports.items():
    if not text:
        continue
    failed_table  = extract_section(text, "Failed Tests")
    failed_detail = extract_section(text, "Failed Tests Detail")
    if not failed_table and not failed_detail:
        continue
    if not has_failures_section:
        out.append("## Failed Tests (All Environments)\n\n")
        out.append("Expected and actual output are cut off after 500 characters.\n\n")
        has_failures_section = True
    out.append(f"### `{container}` ({python_ver})\n\n")
    if failed_table:
        out.append(failed_table + "\n\n")
    if failed_detail:
        out.append("#### Detail\n\n")
        out.append(failed_detail + "\n\n")

if not has_failures_section:
    out.append("## Failed Tests\n\n*No failures across all environments.*\n\n")

def normalize_for_compare(content):
    """Strip execution times so they don't cause false inequality."""
    return re.sub(r'\d+\.\d+s', 'Xs', content)

def append_section_deduped(heading, section_name, note=""):
    """Append a section; if all environments have identical content, show only once."""
    entries = []
    for artifact_id, (container, python_ver, text) in reports.items():
        if not text:
            continue
        content = extract_section(text, section_name)
        if content:
            entries.append((container, python_ver, content))
    if not entries:
        return
    out.append(f"## {heading}\n\n")
    if note:
        out.append(note + "\n\n")
    all_identical = len(set(normalize_for_compare(c) for _, _, c in entries)) == 1
    if all_identical:
        out.append("*(identical across all environments)*\n\n")
        out.append(entries[0][2] + "\n\n")
    else:
        for container, python_ver, content in entries:
            out.append(f"### `{container}` ({python_ver})\n\n")
            out.append(content + "\n\n")

# --- Manual tests (all environments) ---
append_section_deduped(
    "Manual Tests", "Manual Tests",
    note="A test is listed here if at least one of its `@PROT_SPEC` blocks is manual "
         "(`manual=` in the block, reason shown in the table). "
         "Such blocks are not run in CI and must be checked by hand. "
         "The Blocks column shows what happened to the other blocks of the test.")

# --- Passed tests (all environments) ---
append_section_deduped("Passed Tests", "Passed Tests")

merged = "".join(out)

summary_path = os.environ.get("GITHUB_STEP_SUMMARY", "/tmp/merged_report.md")
with open(summary_path, "w") as f:
    f.write(merged)

with open("/tmp/merged_report.md", "w") as f:
    f.write(merged)

print("Merged report written.")
