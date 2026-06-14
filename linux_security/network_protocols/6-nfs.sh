#!/bin/bash
showmount -e $1 2>/dev/null | grep -E '\(everyone\)|\(.*\)' | sed 's/^[[:space:]]*//'
