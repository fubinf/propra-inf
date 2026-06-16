#!/bin/sh
# git-setup.sh — run ONCE per clone, after:
#   git clone …
#   git submodule update --init
#
# Git refuses to auto-apply config from tracked files (a cloned repo could
# otherwise run arbitrary commands via aliases/pager/hooks). So team-wide git
# settings have to be applied explicitly by each person — that is what this
# script is for. It is tracked, so the *content* is shared and versioned;
# re-run it whenever it changes.
set -e

cd "$(dirname "$0")/.."

# --- Superproject policy ---
# Rebasing superproject commits is safe (nothing external references them).
git config pull.rebase true
# A single `git push` also publishes new submodule commits first, in order.
git config push.recurseSubmodules on-demand
# Pull/checkout recurse into submodules so the working tree follows the recorded
# gitlinks instead of drifting.
git config submodule.recurse true

# --- Submodule (altdir) policy ---
# Integrate teammates' work by MERGE, never rebase: a rebase rewrites your
# submodule commits' SHAs, which invalidates the gitlinks the superproject has
# already recorded. Merge preserves those SHAs, so recorded gitlinks stay valid.
git -C altdir config pull.rebase false

echo "Team git settings applied (superproject + altdir)."
