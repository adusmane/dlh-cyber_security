#!/bin/bash
whois "$1" | awk '/^Registrant Name:/,/^Tech Email:/' | awk -F': ' '/^(Registrant|Admin|Tech)/ {gsub(/ +$/, "", $2); field=$1; value=($2==""?"":$2); if(field~/Street/) value=value" "; if(field~/Ext/) field=field":"; gsub(/^[^:]*:/, "", field); gsub(/^[ \t]+|[ \t]+$/, "", field); print field","value}' | sed '/^$/d' > "$1.csv"
