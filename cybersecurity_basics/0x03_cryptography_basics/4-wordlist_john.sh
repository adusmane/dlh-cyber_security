#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 "$1" --stdout | grep -Ff - hash.txt > 4-password.txt
