#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt "$1" --format=Raw-MD5 --show | cut -d: -f2 > 4-password.txt
