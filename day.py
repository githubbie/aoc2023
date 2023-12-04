#!/usr/bin/env python3
import sys

def xxx(filename):
    for line in open(filename):
        line = line.strip()

if len(sys.argv) > 1:
    xxx(sys.argv[1])
else:
    xxx('input/day-4.txt')
