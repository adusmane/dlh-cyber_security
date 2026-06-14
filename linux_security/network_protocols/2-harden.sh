#!/bin/bash
find / -xdev -type d -perm -o+w 2>/dev/null | while read dir; do chmod 755 "$dir" && printf "%s\n" "$dir"; done
