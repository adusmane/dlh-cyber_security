#!/bin/bash
sha1sum <<< "$1" | cut -d' ' -f1 > 0_hash.txt
