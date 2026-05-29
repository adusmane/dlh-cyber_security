#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 "$1" --stdout > wordlist.txt && hashcat -m 0 -a 0 "$1" wordlist.txt -o 4-password.txt
