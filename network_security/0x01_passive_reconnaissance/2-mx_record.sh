#!/bin/bash
nslookup -type=MX "$1" 2>/dev/null | grep -E "^(Server:|Address:|$1.*mail exchanger)"
