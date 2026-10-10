#!/usr/bin/env bash
sudo nmap -sF -f -T2 -p 80-85 "$1"

