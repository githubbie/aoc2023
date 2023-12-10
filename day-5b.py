#!/usr/bin/env python3
import sys

def process_mapping(positions, output, destination, source, length):
    to_delete = []
    for position in positions:
        if source <= position < source+length:
            output.append(destination + (position-source))
            to_delete.append(position)
    for position in to_delete:
        positions.remove(position)

def finish_mapping(positions, output):
    output.extend(positions)
    return output

def process(filename):
    positions = []
    output = []
    for line in open(filename):
        line = line.strip()
        if (positions == []) and (output == []):
            output = [int(s) for s in line.split(':')[1].split()]
        elif line == '':
            positions = finish_mapping(positions, output)
            output = []
        elif line.endswith('map:'):
            print(line)
        else:
            destination, source, length = [int(s) for s in line.split()]
            process_mapping(positions, output, destination, source, length)
    positions = finish_mapping(positions, output)
    output = []
    print(min(positions))

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-5.txt')
