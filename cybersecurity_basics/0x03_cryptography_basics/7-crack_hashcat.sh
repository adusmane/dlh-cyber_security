#!/bin/bash
hashcat -m 0 -a 0 "$1" /usr/share/wordlists/rockyou.txt --force -o 7-password.txt --outfile-format=2 --potfile-disable

