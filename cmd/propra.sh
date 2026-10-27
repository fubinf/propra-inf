# Shell infrastructure for building, deploying, and using propra-inf.
# Based on sedrila.
# In a fork, make your own file, source this one, and redefine what you need to be different

# At any time, we have two ProPras running in parallel, 
# one called summer semester (SS), starting in April
# one called winter semester (WS), starting in October
# each of them runs for 12 months.
# We want to be able to keep their content in sync to allow for additions/modifications after start.
# We use a single sedrila.yaml for building both of them, parameterized by environment variables
# and separate participants files.

SEDRILA=dsedrila  # which command to use, e.g. define a suitable shell function
# user must set PROPRA_BASEDIR: common prefix of both propra deploy dirs (which end in PROPRA_TARGETDIR)

s_setSS() {
  printf 'Are you sure? ProPra-2027-04? Press Ctrl-C if not.  '
  read answer
  export SEDRILA_TITLE="Programmierpraktikum SoSe 2027, Bachelor Informatik, FU Berlin"
  export SEDRILA_NAME="ProPra-2027-04"
  export SEDRILA_PARTICIPANTS_FILE=""
  export SEDRILA_STARTDATE="2027-04-21"
  export SEDRILA_ENDDATE="2028-03-31"
  PROPRA_BUILDDIR="out/2027-04"
  PROPRA_TARGETDIR="K-ProPra-2027-04"
}

s_setWS() {
  export SEDRILA_TITLE="Programmierpraktikum WiSe 2026/2027, Bachelor Informatik, FU Berlin"
  export SEDRILA_NAME="ProPra-2026-10"
  export SEDRILA_PARTICIPANTS_FILE="participants/propra-2026-10.tsv"
  export SEDRILA_STARTDATE="2026-10-20"
  export SEDRILA_ENDDATE="2027-09-30"
  PROPRA_BUILDDIR="out/2026-10"
  PROPRA_TARGETDIR="K-ProPra-2026-10"
}

s_set_draft() {
  s_setWS
  PROPRA_BUILDDIR="out/draft"
  unset PROPRA_TARGETDIR
}

s_author_do() {  # possible args are additional sedrila flags, esp. --stats
  (set -x;  $SEDRILA author build "$@" $PROPRA_BUILDDIR)
}

s_author() {  # build all tasks. Add --print-status manually to get progressplot data
  s_set_draft
  s_author_do --include-stage draft "$@"
}

s_authorSS() {  # build released tasks for summer semester
  s_setSS
  s_author_do --include-stage beta "$@"
}

s_authorWS() {  # build released tasks for winter semester
  s_setWS
  s_author_do --include-stage beta "$@"
}

s_author2() {  # build released tasks for all currently maintained ProPras
  # s_authorSS "$@"  # receives no updates any more
  s_authorWS "$@"
}

s_publish_do() {
  (set -x; 
   rsync -cir --delete --exclude='instructor/.sedrila_cache.*' $PROPRA_BUILDDIR/ $PROPRA_BASEDIR/$PROPRA_TARGETDIR)
}

s_publishSS() {  
  s_setSS
  s_publish_do  
}

s_publishWS() {
  s_setWS
  s_publish_do  
}

s_publish2() {
  # s_publishSS  # receives no updates any more
  s_publishWS
}

s_serve() {
  s_set_draft
  (cd $PROPRA_BUILDDIR; $SEDRILA server --quiet --port 8099 .)
}

propra_pullpush() (
  # do git pull, then git push, and handle the complicated case of merge-altdir + rebased-propra:
  set -eu
  fail() { echo "propra_sync: $*" >&2; exit 1; }
  say()  { echo "###   $*" >&2; }
  run()  { echo "+ $*" >&2; "$@"; }     # echo a state-changing/network command, then run it
  top=$(git rev-parse --show-superproject-working-tree)
  [ -n "$top" ] || top=$(git rev-parse --show-toplevel)
  cd "$top"            # subshell: cannot leak to the caller
  [ -e altdir/.git ] || fail "no altdir submodule in $top"
  say "main repo: $top"

  say "altdir: attach to main, merge remote main"
  run git -C altdir fetch origin
  cur=$(git -C altdir symbolic-ref -q --short HEAD || echo DETACHED)
  say "altdir is on: $cur"
  case $cur in
    main) ;;
    DETACHED)  # adopt the detached HEAD only if it contains local main
      run git -C altdir merge-base --is-ancestor main HEAD || fail "altdir: local main has commits not in HEAD"
      run git -C altdir checkout -q -B main HEAD ;;
    *) fail "altdir is on branch '$cur', expected main" ;;
  esac
  run git -C altdir merge --no-edit --autostash origin/main \
    || fail "altdir merge failed; resolve in altdir, then rerun"

  say "main repo: rebase onto remote main"
  [ "$(git symbolic-ref -q --short HEAD)" = main ] || fail "main repo not on branch main"
  run git pull --rebase --autostash origin main || {
    while [ -d "$(git rev-parse --git-path rebase-merge)" ] \
       || [ -d "$(git rev-parse --git-path rebase-apply)" ]; do
      # the only tolerated conflict is the altdir pointer: take altdir's merged HEAD
      [ "$(git diff --name-only --diff-filter=U)" = altdir ] || fail "unexpected rebase conflict"
      say "rebase conflict only in altdir pointer: use altdir's merged HEAD"
      run git add altdir
      if git diff --cached --quiet; then run git rebase --skip
      else GIT_EDITOR=true run git rebase --continue; fi || true
    done
  }

  if [ "$(git rev-parse HEAD:altdir)" != "$(git -C altdir rev-parse HEAD)" ]; then
    say "altdir pointer is stale: record merged altdir state"
    run git add altdir
    run git commit -q -m "update submodule altdir"
  else
    say "altdir pointer is up to date"
  fi

  say "push: altdir first, then main repo"
  run git -C altdir push origin main
  run git push origin main
)
