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
