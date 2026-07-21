#!/usr/bin/env python3
"""
Remove superfluous empty lines from the submission section of task files.

Concretely: walk a directory tree, find files matching a filename glob, and in
each file's

    [SECTION::submission::...]
    ...
    [ENDSECTION]

block remove every empty line that sits immediately before or after a line of
the form [INCLUDE::/_include/*.md]. Empty lines that are not adjacent to such an
INCLUDE line (e.g. between paragraphs of prose) are left alone. For instance

    [SECTION::submission::program,information]

    [INCLUDE::/_include/Submission-Quellcode.md]

    Bearbeite die folgenden Punkte:

    - erster Punkt

    [INCLUDE::/_include/Submission-Markdowndokument.md]

    [ENDSECTION]

becomes

    [SECTION::submission::program,information]
    [INCLUDE::/_include/Submission-Quellcode.md]

    Bearbeite die folgenden Punkte:

    - erster Punkt
    [INCLUDE::/_include/Submission-Markdowndokument.md]
    [ENDSECTION]

--------------------------------------------------------------------------------
Adapting this script to a similar rewriting task
--------------------------------------------------------------------------------
The generic engine below (find_block / rewrite_file / walk) walks a tree, finds
at most one block per file (delimited by a start and end regexp), checks a
condition on that block, and rewrites the block if the condition holds. To adapt
it, change only the "task-specific block definition" section:

  * BLOCK_START / BLOCK_END  regexps that identify the delimiting lines
  * INCLUDE_BOUNDS           whether the block passed to the check/rewrite
                             functions includes its start/end lines or not
  * block_needs_rewrite()    the condition
  * rewrite_block()          returns (new_lines, report_metric)

Lines carry their trailing "\n"; the rest of the file is preserved byte-for-byte.
"""

import fnmatch
import os
import re
import sys

DEFAULT_MAX = 9999

USAGE = """\
usage: helper_rewrite_files.py <tree> <pattern> [<max>]

  <tree>     directory to walk recursively
  <pattern>  filename glob (must contain '*' or '?', quote it!), matched against basenames
  <max>      max number of files to rewrite (default 9999)

Walks through <tree>, looking for files with local names <pattern>.
Processes each such file one by one.
In the file, identifies blocks of lines via the BLOCK_START/BLOCK_END regexp program constants.
Checks block for need of rewriting via the block_needs_rewrite() predicate.
Then rewrites that block via the rewrite_block() function and writes back the modified file.
"""


# --- task-specific block definition -----------------------------------------

BLOCK_START = re.compile(r"^\[SECTION::submission::")
BLOCK_END = re.compile(r"^\[ENDSECTION\]")
RELEVANT_LINE = re.compile(r"^\[INCLUDE::/_include/.*\.md\]")
INCLUDE_BLOCK_START_AND_END = False  # the empty-line check/rewrite acts on the inner lines only


def _is_empty(line):
    return line.strip() == ""


def _removable_indices(block):
    """Indices of empty lines that sit immediately before or after an
    [INCLUDE::/_include/*.md] line (adjacency judged on the original block, so
    empty lines around other text are never touched)."""
    def is_include(i):
        return 0 <= i < len(block) and RELEVANT_LINE.match(block[i])
    return [i for i, line in enumerate(block)
            if _is_empty(line) and (is_include(i - 1) or is_include(i + 1))]


def block_needs_rewrite(block):
    """True if the block has an empty line adjacent to an INCLUDE line."""
    return bool(_removable_indices(block))


def rewrite_block(block):
    """Drop the INCLUDE-adjacent empty lines.
    Returns (new_block, number_of_empty_lines_removed)."""
    drop = set(_removable_indices(block))
    kept = [line for i, line in enumerate(block) if i not in drop]
    return kept, len(drop)


# --- generic engine ----------------------------------------------------------

class RewriteError(Exception):
    """A file is malformed and cannot be processed; abort the whole run."""


def find_block(lines):
    """Locate the single block in `lines`.

    Returns (start, end) as line indices such that lines[start:end] is the block
    the check/rewrite functions operate on:
      * INCLUDE_BOUNDS is True  -> start/end span the delimiter lines inclusively
      * INCLUDE_BOUNDS is False -> the span covers only the lines in between
    Returns None if the file has no such block.
    Raises RewriteError on multiple start lines or a missing end line.
    """
    starts = [i for i, line in enumerate(lines) if BLOCK_START.match(line)]
    if len(starts) > 1:
        raise RewriteError("multiple [SECTION::submission::...] lines "
                           "(at lines %s)" % ", ".join(str(s + 1) for s in starts))
    if not starts:
        return None
    start = starts[0]
    ends = [i for i in range(start + 1, len(lines)) if BLOCK_END.match(lines[i])]
    if not ends:
        raise RewriteError("[SECTION::submission::...] at line %d has no "
                           "following [ENDSECTION]" % (start + 1))
    end = ends[0]
    if INCLUDE_BLOCK_START_AND_END:
        return start, end + 1
    return start + 1, end


def rewrite_file(path):
    """Rewrite `path` in place if needed. Returns the report metric, or None.

    Raises RewriteError if the file is malformed.
    """
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    span = find_block(lines)
    if span is None:
        return None
    start, end = span
    block = lines[start:end]
    if not block_needs_rewrite(block):
        return None
    new_block, metric = rewrite_block(block)
    lines[start:end] = new_block
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return metric


def walk(tree, pattern):
    """Yield every file below `tree` whose basename matches `pattern`, sorted."""
    for dirpath, dirnames, filenames in os.walk(tree):
        dirnames.sort()
        for name in sorted(filenames):
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(dirpath, name)


# --- command line ------------------------------------------------------------

def usage_error(message):
    sys.stderr.write("error: %s\n\n%s" % (message, USAGE))
    sys.exit(2)


def parse_args(argv):
    if not (2 <= len(argv) <= 3):
        usage_error("expected 2 or 3 arguments, got %d" % len(argv))
    tree, pattern = argv[0], argv[1]
    if not os.path.isdir(tree):
        usage_error("<tree> is not a directory: %s" % tree)
    if "*" not in pattern and "?" not in pattern:
        usage_error("<pattern> must be a filename glob containing '*' or '?': %s"
                    % pattern)
    if len(argv) == 3:
        try:
            max_files = int(argv[2])
        except ValueError:
            usage_error("<max> must be an integer: %s" % argv[2])
    else:
        max_files = DEFAULT_MAX
    return tree, pattern, max_files


def main(argv):
    tree, pattern, max_files = parse_args(argv)
    rewritten = 0
    for path in walk(tree, pattern):
        if rewritten >= max_files:
            break
        try:
            metric = rewrite_file(path)
        except RewriteError as exc:
            sys.stderr.write("error in %s: %s\n" % (path, exc))
            sys.exit(1)
        if metric is not None:
            print("%s: removed %d empty line%s"
                  % (path, metric, "" if metric == 1 else "s"))
            rewritten += 1


if __name__ == "__main__":
    main(sys.argv[1:])
