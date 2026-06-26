#!/bin/bash
sudo nmap -n -sn -PS22,80,443 $1
