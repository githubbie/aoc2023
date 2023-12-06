#!/usr/bin/env python3
import sys

def race(time):
    distances = [t*(time-t) for t in range(time)] + [0]
    print(f'Distances for {time}: {distances}')
    return distances

def process(filename):
    for line in open(filename):
        line = line.strip()
        if line.startswith('Time'):
            times = [int(s) for s in line.split(':')[-1].split()]
        else:
            max_distances = [int(s) for s in line.split(':')[-1].split()]
    total=1
    for race_number in range(len(times)):
        distances = race(times[race_number])
        winning = sum([1 if distances[i] > max_distances[race_number] else 0 for i in range(len(distances))])
        print(f'Race {race_number}: {winning}')
        total *= winning
    print(total)

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-6.txt')
