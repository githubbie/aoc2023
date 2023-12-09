#!/usr/bin/env python3
import sys

def process(filename):
    for line in open(filename):
        line = line.strip()

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-4.txt')
