#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "${BASH_SOURCE[0]%/*}" || exit; { set +x; } 2>/dev/null; } 2>&1

( set -x; make )
