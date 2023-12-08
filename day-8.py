#!/usr/bin/env python3
import sys

def convert(location, loc2pos, pos2loc):
    if not location in loc2pos:
        position=len(pos2loc)
        loc2pos[location]=position
        pos2loc.append(location)
    return loc2pos[location]

def next_position(position, move, steps):
    for step in steps:
        if step == 'L':
            position = move[position][0]
        else:
            position = move[position][1]
    return position

def process(filename):
    loc2pos = {}
    pos2loc = []
    move = {}
    next_pos = []
    line_no=0
    for line in open(filename):
        line = line.strip()
        line_no += 1
        if line == '':
            pass
        elif '=' in line:
            line = line.replace(' ','').replace('(','').replace(')','')
            start, destinations = line.split('=')
            start = convert(start, loc2pos, pos2loc)
            left, right = destinations.split(',')
            left = convert(left, loc2pos, pos2loc)
            right = convert(right, loc2pos, pos2loc)
            move[start] = (left, right)
            print(f'{line_no:3d} {start:3d}-{pos2loc[start]}->[{left:3d}-{pos2loc[left]},{right:3d}-{pos2loc[right]}] {len(move):3d}->{move[start]}')
        else:
            steps = line
            print(steps)
    next_pos = [next_position(i, move, steps) for i in range(len(move))]
    print(next_pos)
    start = loc2pos['AAA']
    finish = loc2pos['ZZZ']
    num_moves = 0
    moved = ''
    while start != finish:
        begin = pos2loc[start]
        #print(f'{start}-{begin}: {move[start]} {steps[num_moves % len(steps)]}')
        step = steps[num_moves % len(steps)]
        moved += step
        if step == 'L':
            start = move[start][0]
        else:
            start = move[start][1]
        num_moves += 1
        #print(f'Move {num_moves}: {start} {step} {begin}->{pos2loc[start]}')
    print(num_moves)


if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-8.txt')
