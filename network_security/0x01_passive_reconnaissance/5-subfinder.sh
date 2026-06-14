#!/bin/bash
subfinder -d $1 -silent | while read domain; do echo "$domain,$(dig +short $domain | head -1)"; done | grep -v ",$" | tee $1.txt
