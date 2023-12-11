#!/usr/bin/env python3
import sys

def expand(universe):
    y = 0
    while y < len(universe):
        if not '#' in universe[y]:
            universe = universe[:y] + ['.'*len(universe[y])] + universe[y:]
            y+=1
        y+=1
    x = 0
    while x < len(universe[0]):
        if not '#' in [s[x] for s in universe]:
            universe = [s[:x] + '.' + s[x:] for s in universe]
            x+=1
        x+=1
    return universe

def print_universe(universe):
    for s in universe:
        print(s)

def sum_distances(galaxies):
    if galaxies == []:
        return 0
    first = galaxies[0]
    return sum([abs(first[0]-galaxy[0])+abs(first[1]-galaxy[1]) for galaxy in galaxies[1:]]) + sum_distances(galaxies[1:])

def process(filename):
    universe = []
    for line in open(filename):
        line = line.strip()
        universe.append(line)
    print('Unexpanded:')
    print_universe(universe)
    expanded_universe = expand(universe)
    galaxies = [(y,x) for y in range(len(universe)) for x in range(len(universe[0])) if universe[y][x] == '#']
    galaxies.sort()
    print(f'Galaxies: {galaxies}')
    distances = sum_distances(galaxies)
    print(distances)
    print('Expanded:')
    print_universe(expanded_universe)
    galaxies = [(y,x) for y in range(len(expanded_universe)) for x in range(len(expanded_universe[0])) if expanded_universe[y][x] == '#']
    galaxies.sort()
    print(f'Galaxies: {galaxies}')
    expanded_distances=sum_distances(galaxies)
    print(expanded_distances)
    expanded = expanded_distances - distances
    normal = distances - expanded
    for factor in [0, 1, 10, 100, 1000000]:
        print(f'Factor {factor}: {normal + expanded*factor}')

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-11.txt')
