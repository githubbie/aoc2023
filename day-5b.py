#!/usr/bin/env python3
import sys

def process_mapping(positions, output, destination, source, length):
    to_delete = []
    to_add = []
    source = (source, source+length-1)
    for position in positions:
        print(f'Processing {position} versus {source}:')
        if source[1] < position[0]:
            print('A')
            # position: ________________+------+____
            # source:   _____+------+_______________
            pass    
        elif position[0] >= source[0] and position[0] <= source[1] <= position[1]:
            print('B')
            # position: ________________+------+____
            # source:   _____+--------------+_______
            # IN: (p0,s1), OUT (s1+1,p1)
            output.append((destination+(position[0]-source[0]), destination+(source[1]-source[0])))
            if source[1] < position[1]:
                to_add.append((source[1]+1, position[1]))
            to_delete.append(position)
        elif source[0] <= position[0] <= source[1] and source[0] <= position[1] <= source[1]:
            print('C')
            # position: ________________+------+____
            # source:   _____+-------------------+__
            # IN: (p0,p1)
            output.append((destination+(position[0]-source[0]), destination+(position[1]-source[0])))
            to_delete.append(position)
        elif position[0] <= source[0] <= position[1] and position[0] <= source[1] <= position[1]:
            print('D')
            # position: ______+------+______________
            # source:   _________+-+________________
            # IN: (s0,s1), OUT: (p0,s0-1), (s1+1, p1)
            if position[0] <= source[0]-1:
                to_add.append((position[0], source[0]-1))
            if source[1]+1 <= position[1]:
                to_add.append((source[1]+1, position[1]))
            output.append((destination+(source[0]-source[0]), destination+(source[1]-source[0])))
            to_delete.append(position)
        elif position[0] <= source[0] <= position[1] and position[1] <= source[1]:
            print('E')
            # position: ______+------+_____________
            # source:   _________+---------+_______
            # IN: (s0,p1), OUT: (p0,s0-1)
            if position[0] <= source[0]-1:
                to_add.append((position[0], source[0]-1))
            output.append((destination+(source[0]-source[0]), destination+(position[1]-source[0])))
            to_delete.append(position)
        else:
            print('F')
            # position: ____+------+_____________
            # source:   ______________+-------+__
            pass
        print(f'to_add: {to_add}')
        print(f'to_del: {to_delete}')
        print(f'output: {output}')
    for position in to_delete:
        positions.remove(position)
    for position in to_add:
        positions.append(position)

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
            output = [(output[2*i], output[2*i]+output[2*i+1]-1) for i in range(int(len(output)/2))]
            print('seeds:')
        elif line == '':
            positions = finish_mapping(positions, output)
            output = []
            print(positions)
        elif line.endswith('map:'):
            print(line)
        else:
            destination, source, length = [int(s) for s in line.split()]
            print(f'Mapping {(source, source+length-1)} to {(destination, destination+length-1)}:')
            process_mapping(positions, output, destination, source, length)
            print(f'  remaining positions: {positions}')
            print(f'  output             : {output}')
    positions = finish_mapping(positions, output)
    output = []
    print(sorted(positions))
    print(min(positions)[0])

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-5.txt')
