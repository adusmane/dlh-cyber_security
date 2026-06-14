#!/bin/bash
find / -xdev -type d -perm -0002 2>/dev/null | while read dir; do chmod 755 "$dir" && printf "%s\n" "$dir"; done
