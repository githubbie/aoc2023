#!/usr/bin/env python3
import sys

def count(line, position, damaged):
    print(f'count({line}, {position}, {damaged} = ')
    # count the number of solutions for finding the sequence of 
    # of damaged springs in damaged, in the string line, starting
    # at position
    # Assumptions:
    # - the first damaged spring can start immediately at position
    at_least_remaining = sum(damaged)+len(damaged)-1
    print('  ', len(line)-position, at_least_remaining)
    if len(line)-position < at_least_remaining:
        print('(a) 0')
        return 0
    if damaged == []:
        if line.find('#', position) == -1:
            print('(b) 1')
            return 1
        else:
            print('(c) 0')
            return 0
    next_qm = line.find('?', position)
    next_hs = line.find('#', position)
    if next_qm == -1:
        next_possible = next_hs
    elif next_hs == -1:
        next_possible = next_qm
    else:
        next_possible = min(next_qm, next_hs)
    if next_possible > -1:
        needed = damaged[0]
        print('    ', next_possible, needed, len(line))
        if (next_possible + needed == len(line)) or \
           ((next_possible + needed < len(line)) and (line[next_possible+needed] in '?.')):
            allowed = not '.' in line[next_possible:next_possible+needed]
        else:
            allowed = False
        if allowed and line[next_possible] == '?':
            result = count(line, next_possible+needed+1, damaged[1:]) + \
                     count(line, next_possible+1, damaged)
            print(f'(d) {result}')
            return result
        elif allowed and line[next_possible] == '#':
            result = count(line, next_possible+needed+1, damaged[1:])
            print(f'(e) {result}')
            return result
        elif not allowed and line[next_possible] == '?':
            result = count(line, next_possible+1, damaged)
            print(f'(f) {result}')
            return result

    print('(g) 0')
    return 0

def process(filename):
    total = 0
    for line in open(filename):
        line = line.strip()
        s, *damaged = line.replace(',',' ').split()
        damaged = [int(i) for i in damaged]
        total += count(s, 0, damaged)
    print(total)

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-12.txt')
