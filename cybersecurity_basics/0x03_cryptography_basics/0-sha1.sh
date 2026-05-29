#!/bin/bash
echo -n "$1" | sha1sum | grep -o '^[a-f0-9]*' > 0_hash.txt
