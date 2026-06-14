#!/bin/bash
find / -type d -perm -o+w 2>/dev/null | while read dir; do echo "$dir"; chmod 755 "$dir"; done
