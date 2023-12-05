#!/usr/bin/env python3
import sys

def process(filename):
    output = []
    for line in open(filename):
        line = line.strip()
        if line.startswith('seeds:'):
            output.append(('Seed', [int(s) for s in line.split(':')[-1].split()]))
        elif len(line) == 0:
            pass
        elif line[0].isdigit():
            destination, origin, length = [int(s) for s in line.split()]
            print(output, destination, origin, length)
            start_point = output[-2][1]
            current = output[-1][1]
            for i in range(len(start_point)):
                if start_point[i] in range(origin,origin+length):
                    print(f'Mapping {i} - {start_point[i]} in {range(origin,origin+length)} to {destination}+{start_point[i]-origin}')
                    current[i] = destination + (start_point[i]-origin)
        else: # new mapping start
            map_name = line.split('-')[-1].split()[0]
            output.append((', '+map_name, list(output[-1][1])))
    return output

def dump2(output, index):
    name = output[0][0]
    mapping = output[0][1]
    print(f'{name} {mapping[index]}', end='')
    if len(output) == 1:
        print()
    else:
        dump2(output[1:], index)

def dump(output):
    mapping = output[0][1]
    for i in range(len(mapping)):
        dump2(output, i)

if len(sys.argv) > 1:
    output = process(sys.argv[1])
else:
    output = process('input/day-4.txt')
dump(output)
print(min(output[-1][1]))
