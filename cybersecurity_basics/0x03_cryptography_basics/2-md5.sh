#!/bin/bash
echo -n "$1" | md5sum | grep -o '^[a-f0-9]*' > 2_hash.txt
