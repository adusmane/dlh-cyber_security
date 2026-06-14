#!/bin/bash
nslookup -type=MX "$1" 2>/dev/null | grep -A10 "Non-authoritative answer:" | grep "mail exchanger"
