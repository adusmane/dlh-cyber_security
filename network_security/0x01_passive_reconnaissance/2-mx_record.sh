#!/bin/bash
nslookup -type=MX "$1" 2>/dev/null | grep -E "^(Server:|Address:|holbertonschool.com.*mail exchanger)"
