#!/usr/bin/env python3
import sys

def hash(s):
    current = 0
    for c in s:
        current = ((current+ord(c)) * 17) % 256
    return current

def process(filename):
    for line in open(filename):
        line = line.strip()
        total = sum([hash(instruction) for instruction in line.split(',')])
        print(total)

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-15.txt')
