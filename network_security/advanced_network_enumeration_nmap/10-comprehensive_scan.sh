#!/bin/bash
sudo nmap --script http-vuln-cve2017-5638,ssl-enum-ciphers,ftp-anon -oN comprehensive_scan_results.txt $1
