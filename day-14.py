#!/usr/bin/env python3
import sys

def transpose(map):
    return [''.join(s[j] for s in map) for j in range(len(map[0]))]

def print_map(map):
    for s in map:
        print(s)

def shift_row(s, reverse):
    return '#'.join([''.join(sorted(p, reverse=reverse)) for p in s.split('#')])

def shift_map(map, reverse):
    return [shift_row(r, reverse) for r in map]

def count_row(s):
    return len(s.split('O'))-1

def count_map(map):
    return sum([(len(map)-i)*count_row(r) for i,r in enumerate(map)])

def tilt(map, direction):
    map = map.copy()
    for c in direction.replace('C','NWSE'):
        if c == 'N':
            map = transpose(shift_map(transpose(map), True))
        elif c == 'S':
            map = transpose(shift_map(transpose(map), False))
        elif c == 'E':
            map = shift_map(map, False)
        elif c == 'W':
            map = shift_map(map, True)
    return map

def process(filename):
    for map_s in open(filename).read().split('\n\n'):
        map = map_s.split('\n')
        if map[-1] == '':
            del map[-1]
        print_map(map)
        print(count_map(tilt(map, 'N')))
        single_steps = tilt(map, 'C')
        double_steps = tilt(map, 'CC')
        n = 1
        while single_steps != double_steps:
            single_steps = tilt(single_steps, 'C')
            double_steps = tilt(double_steps, 'CC')
            n += 1
        cycle_map = tilt(single_steps, 'C')
        k = 1
        while cycle_map != single_steps:
            cycle_map = tilt(cycle_map, 'C')
            k += 1
        number_of_cycles = int((1_000_000_000 - n)/k)
        remainder = 1_000_000_000-n-k*number_of_cycles
        print(n, k, number_of_cycles, remainder)
        final_map = single_steps
        for _ in range(remainder):
            final_map = tilt(final_map, 'C')
        print_map(final_map)
        print(count_map(final_map))


if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-14.txt')
