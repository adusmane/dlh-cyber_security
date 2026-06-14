#!/bin/bash
subfinder -d $1 -silent | xargs -I {} sh -c 'echo "$(echo {} | sed "s/^.*$1/$1/"),$(dig +short {} | head -1)"' | grep -v ",$" | tee $1.txt
