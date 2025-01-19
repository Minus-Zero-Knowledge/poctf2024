#!/usr/bin/sh

hashcat --stdout -a 0 monstertrucks_monsterjam.txt -r spaces.rule -r casing.rule -r digits.rule > monstertrucks.txt
