#!/usr/bin/env python3
"""
Adjust @LINK_SPEC comments for links that the linkchecker reports as 403-related.

Usage: adjust-linkspec-403.py reportfile

The reportfile contains rows of the "Failed Links" table of a `sedrila maintainer check-links` report:
    | Status | URL | File | Line | Error |
Only rows whose Error is "HTTP 403" or "Expected HTTP 403, got 200" are processed:
- "HTTP 403": ensure the link has a LINK_SPEC with `status=403`
  (extend an existing spec, or insert a new comment directly before the link).
- "Expected HTTP 403, got 200": remove `status=403` from the link's LINK_SPEC
  (and the whole comment if nothing else remains in it).
Stand-alone: it deliberately does not import sedrila; the link-syntax regexes are copied below.
File paths are taken relative to the current directory. Files are modified in place; use git to review.
"""
import collections
import re
import sys
import urllib.parse

ERR_ADD = "HTTP 403"
ERR_REMOVE = "Expected HTTP 403, got 200"
# The following patterns and MAX_DISTANCE are copies from sedrila/mech/linkchecker.py (class LinkExtractor);
# keep them in sync with it.
SPEC_RE = re.compile(r'<!--\s*@LINK_SPEC:\s*(.*?)\s*-->')
MD_LINK_RE = re.compile(r'\[([^\]]*)\]\(((?:[^)(]|\((?:[^)(])*\))*)\)')
HREF_RE = re.compile(r'\[HREF::([^\]]+)\]')
MAX_DISTANCE = 2  # a @LINK_SPEC must be on the link's line or at most this many lines above it
NEW_SPEC = "<!-- @LINK_SPEC: status=403 -->"


def warn(file: str, lineno: int, msg: str):
    print(f"WARNING {file}:{lineno}: {msg}", file=sys.stderr)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    jobs = collections.defaultdict(set)  # file -> {(line, url, action)}
    with open(sys.argv[1], encoding='utf-8') as f:
        for row in f:
            cols = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cols) != 5 or cols[4] not in (ERR_ADD, ERR_REMOVE) or not cols[3].isdigit():
                continue
            jobs[cols[2]].add((int(cols[3]), cols[1], cols[4]))
    for file, entries in sorted(jobs.items()):
        process_file(file, entries)


def process_file(file: str, entries: set):
    try:
        with open(file, encoding='utf-8', newline='') as f:
            lines = f.read().split('\n')  # keeps any \r at line ends
    except OSError as exc:
        print(f"WARNING {file}: cannot read: {exc}", file=sys.stderr)
        return
    # Bottom to top, right to left: edits then never invalidate line numbers or positions still to be used.
    def sortkey(entry):
        lineno, url, _ = entry
        pos = lines[lineno - 1].find(url) if 1 <= lineno <= len(lines) else 0
        return lineno, pos
    changed = 0
    for lineno, url, action in sorted(entries, key=sortkey, reverse=True):
        if not 1 <= lineno <= len(lines):
            warn(file, lineno, f"line does not exist; skipping {url}")
            continue
        changed += adjust(file, lines, lineno, url, action)
    if changed:
        with open(file, 'w', encoding='utf-8', newline='') as f:
            f.write('\n'.join(lines))
        print(f"{file}: {changed} change(s)")


def blank_specs(line: str) -> str:
    """Replace LINK_SPEC comments by spaces (same positions), as the extractor does before finding links."""
    return SPEC_RE.sub(lambda m: ' ' * len(m.group(0)), line)


def external_links(line: str) -> list[tuple[int, str]]:
    """(start position, url) of all external links in line, in text order."""
    found = [(m.start(), m.group(2)) for m in MD_LINK_RE.finditer(line)]
    found += [(m.start(), m.group(1)) for m in HREF_RE.finditer(line)]
    return sorted((s, u) for s, u in found if urllib.parse.urlparse(u).scheme in ('http', 'https'))


def adjust(file: str, lines: list[str], lineno: int, url: str, action: str) -> int:
    """Apply one action; return 1 if lines was modified, else 0."""
    idx = lineno - 1
    line = lines[idx]
    candidates = [start for start, u in external_links(blank_specs(line)) if u == url]
    if not candidates:
        warn(file, lineno, f"link {url} not found on this line (file changed since the report?); skipping")
        return 0
    if len(candidates) > 1:
        warn(file, lineno, f"link {url} occurs {len(candidates)} times on this line; ambiguous, skipping")
        return 0
    link_start = candidates[0]
    spec = find_governing_spec(lines, idx, link_start)  # (line index, match) or None
    if action == ERR_ADD:
        return add_status(file, lines, idx, link_start, spec, lineno)
    return remove_status(file, lines, spec, lineno, url)


def find_governing_spec(lines: list[str], idx: int, link_start: int):
    """Find the @LINK_SPEC that applies to the link at (idx, link_start), mirroring the extractor:
    on the same line before the link or at most MAX_DISTANCE lines above, with no other link in between."""
    best = None  # (line index, match)
    for i in range(max(0, idx - MAX_DISTANCE), idx + 1):
        for m in SPEC_RE.finditer(lines[i]):
            if i < idx or m.end() <= link_start:
                best = (i, m)
    if best is None:
        return None
    i, m = best
    # any other external link between the spec and our link would consume the spec:
    for j in range(i, idx + 1):
        text = blank_specs(lines[j])
        for start, _ in external_links(text):
            after_spec = j > i or start >= m.end()
            before_link = j < idx or start < link_start
            if after_spec and before_link:
                return None
    return best


def split_parts(raw: str) -> list[str]:
    return [p.strip() for p in raw.split(',') if p.strip()]


def status_of(part: str):
    """Return the status value if part is a status=... entry, else None."""
    if '=' not in part:
        return None
    key, value = part.split('=', 1)
    return value.strip().strip('"\'') if key.strip().lower() == 'status' else None


def make_spec(parts: list[str]) -> str:
    return f"<!-- @LINK_SPEC: {', '.join(parts)} -->"


def add_status(file, lines, idx, link_start, spec, lineno) -> int:
    if spec is None:
        line = lines[idx]
        if line[:link_start].strip():
            warn(file, lineno, f"non-blank content before the link: {line[:link_start].strip()!r}")
        lines[idx] = line[:link_start] + NEW_SPEC + line[link_start:]
        return 1
    spec_idx, m = spec
    parts = split_parts(m.group(1))
    statuses = [status_of(p) for p in parts if status_of(p) is not None]
    if statuses == ['403']:
        warn(file, spec_idx + 1, "LINK_SPEC already has status=403; nothing to do")
        return 0
    if statuses:
        warn(file, spec_idx + 1, f"LINK_SPEC has conflicting status={statuses[0]}; skipping")
        return 0
    lines[spec_idx] = lines[spec_idx][:m.start()] + make_spec(parts + ['status=403']) + lines[spec_idx][m.end():]
    return 1


def remove_status(file, lines, spec, lineno, url) -> int:
    if spec is None:
        warn(file, lineno, f"no LINK_SPEC found for {url}; nothing to remove")
        return 0
    spec_idx, m = spec
    parts = split_parts(m.group(1))
    remaining = [p for p in parts if status_of(p) != '403']
    if len(remaining) == len(parts):
        warn(file, spec_idx + 1, f"LINK_SPEC has no status=403 (it is: {m.group(0)}); skipping")
        return 0
    line = lines[spec_idx]
    if remaining:
        lines[spec_idx] = line[:m.start()] + make_spec(remaining) + line[m.end():]
        return 1
    before, after = line[:m.start()], line[m.end():]
    if not before.strip() and not after.strip():
        del lines[spec_idx]  # comment alone on its line: delete the line, so no blank line splits the paragraph
    else:
        lines[spec_idx] = before + after
    return 1


if __name__ == '__main__':
    main()
