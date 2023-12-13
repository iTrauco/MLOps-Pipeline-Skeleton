#!/usr/bin/env bash

cat $1 | tr -d '\"' | tr -d '{{' |  tr -d '}}' | awk '{{ if($0 !~ /^[[:space:]]*$/) print $0 }}' | sed 's/^ *//g'  > $2
