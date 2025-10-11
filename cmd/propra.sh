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

SEDRILA=~/venv/sedrila/bin/python\ /ws/fubinf/sedrila/py/sedrila.py  # which command to use
# user must set PROPRA_BASEDIR: common prefix of both propra deploy dirs (which end in PROPRA_TARGETDIR)

s_setSS() {
  export SEDRILA_TITLE="Programmierpraktikum SoSe 2025, Bachelor Informatik, FU Berlin"
  export SEDRILA_NAME="ProPra-2025-04"
  export SEDRILA_PARTICIPANTS_FILE="participants-2025-04.tsv"
  PROPRA_BUILDDIR="out/2025-04"
  PROPRA_TARGETDIR="K-ProPra-2025-04"
}

s_setWS() {
  export SEDRILA_TITLE="Programmierpraktikum WiSe 2025/2026, Bachelor Informatik, FU Berlin"
  export SEDRILA_NAME="ProPra-2025-10"
  export SEDRILA_PARTICIPANTS_FILE="participants-2025-10.tsv"
  PROPRA_BUILDDIR="out/2025-10"
  PROPRA_TARGETDIR="K-ProPra-2025-10"
}

s_set_draft() {
  s_setWS
  PROPRA_BUILDDIR="out/draft"
  unset PROPRA_TARGETDIR
}

s_author_do() {  # possible args are additional sedrila flags, esp. --stats
  (set -x;  $SEDRILA author "$@" $PROPRA_BUILDDIR)
}

s_author1() {  # build all tasks. 
  s_set_draft
  s_author_do --include_stage draft "$@"
}

s_authorSS() {  # build released tasks for summer semester
  s_setSS
  s_author_do --include_stage beta "$@"
}

s_authorWS() {  # build released tasks for winter semester
  s_setWS
  s_author_do --include_stage beta "$@"
}

s_author2() {  # build released tasks for both semesters
  s_authorSS "$@"
  s_authorWS --stats "$@"
}

s_publish_do() {
  rsync -cir --delete --exclude='instructor/.sedrila_cache.*' $PROPRA_BUILDDIR/* PROPRA_BASEDIR/$PROPRA_TARGETDIR
}

s_publishSS() {  # 
  s_setSS
  s_publish_do  
}

s_publishWS() {
  s_setWS
  s_publish_do  
}

s_serve() {
  s_set_draft
  (cd $PROPRA_BUILDDIR; $SEDRILA server --quiet 8099 .)
}
