#!/usr/bin/env python3
import sys
import math

def get_steps1(position, moves, steps):
    num_moves = 0
    while position != 'ZZZ':
        move = steps[num_moves % len(steps)]
        num_moves+=1
        next_position = moves[position][move]
        #print(f'Move {num_moves}: {position} {move} {next_position}')
        position = next_position
    return num_moves

def get_steps2(position, moves, steps):
    num_moves = 0
    while not position.endswith('Z'):
        move = steps[num_moves % len(steps)]
        num_moves+=1
        next_position = moves[position][move]
        #print(f'Move {num_moves}: {position} {move} {next_position}')
        position = next_position
    return num_moves

def process(filename):
    moves = {}
    steps = ''
    for line in open(filename):
        line = line.strip().translate(str.maketrans('(),=','    '))
        pieces = line.split()
        print(f'pieces: {pieces}')
        if len(pieces) == 0:
            pass
        elif len(pieces) == 1:
            steps = pieces[0]
        else:
            start, left, right = pieces
            moves[start] = { 'L': left, 'R': right }
    print(f'steps: {steps}')
    print(f'moves: {moves}')

    # part I: single position
    print(get_steps1('AAA', moves, steps))

    # part II: ghost positions
    positions = [p for p in moves.keys() if p.endswith('A')]
    steps_per_pos = [get_steps2(p, moves, steps) for p in positions]
    print(positions)
    print(steps_per_pos)
    print(math.lcm(*steps_per_pos))

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-8.txt')
