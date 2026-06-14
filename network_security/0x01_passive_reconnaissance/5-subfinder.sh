#!/bin/bash
subfinder -silent -d $1 -nW -oI | tee $1.txt
