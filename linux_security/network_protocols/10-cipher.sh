#!/bin/bash
nmap --script ssl-enum-ciphers -p 443 $1 | grep -E "^(Starting Nmap|Nmap scan|Host is up|PORT|443/tcp|Nmap done|Host script results|ssl-enum-ciphers:|[[:space:]]+|_  least strength:)"
