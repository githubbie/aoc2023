#!/usr/bin/env python3
import sys

def transpose(map):
    return [''.join(s[j] for s in map) for j in range(len(map[0]))]

def print_map(map):
    for s in map:
        print(s)

def shift_left_row(s):
    return '#'.join([''.join(sorted(p, reverse=True)) for p in s.split('#')])

def shift_left_map(map):
    return [shift_left_row(r) for r in map]

def count_row(s):
    return len(s.split('O'))-1

def count_map(map):
    return sum([(len(map)-i)*count_row(r) for i,r in enumerate(map)])

def process(filename):
    for map_s in open(filename).read().split('\n\n'):
        map = map_s.split('\n')
        if map[-1] == '':
            del map[-1]
        print_map(map)
        print()
        print_map(transpose(map))
        print()
        print_map(shift_left_map(transpose(map)))
        print()
        print_map(transpose(shift_left_map(transpose(map))))
        print()
        print(count_map(transpose(shift_left_map(transpose(map)))))

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-14.txt')
