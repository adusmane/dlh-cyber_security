#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-sha256 "$1" ; john --show --format=raw-sha256 "$1" | awk 'NR>1 {print $2}' > 6-password.txt
