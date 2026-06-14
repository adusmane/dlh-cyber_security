#!/bin/bash
grep -E 'public|com2sec.*public|rocommunity.*public' /etc/snmp/snmpd.conf 2>/dev/null | grep -v '^#'
