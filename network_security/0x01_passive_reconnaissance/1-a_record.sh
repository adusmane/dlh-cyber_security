#!/bin/bash
nslookup -type=A "$1" 2>/dev/null | grep -A1 "Name:" | grep -v "Name:" | grep -v "^--$" | sed '/^$/d'
