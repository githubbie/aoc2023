#!/usr/bin/env python3
import re

def read_schematic(filename):
    regex = re.compile('(?P<number>\d+)|(?P<part>[^.0-9])')
    line_number = 0
    numbers = [] # (line, (start,end), value)*
    parts = {}   # [line][position]
    lines = []   # (string)*
    for line in open(filename):
        start_pos = 0
        line = line.strip()
        lines.append(line)
        parts[line_number] = {}
        print(f'Line {line_number}: {line}')
        while start_pos < len(line):
            match = regex.search(line, start_pos)
            if match:
                span = (match.start(), match.end()-1)
                if match.group('number'):
                    number = int(match.group('number'))
                    numbers.append((line_number, span, number))
                    print(f'Number: {number} on ({span}, {line_number})')
                else:
                    part = match.group('part')
                    parts[line_number][span[0]] = { part: [] }
                    print(f'Part: {part} on ({span}, {line_number})')
                start_pos = match.end()
            else:
                start_pos = len(line)
        line_number += 1
    return numbers, parts, lines

def count_number(line_number, span, parts, number, lines):
    for line in range(line_number-1,line_number+2):
        if line in parts:
            for pos in range(span[0]-1,span[1]+2):
                if pos in parts[line]:
                    part = list(parts[line][pos].keys())[0]
                    print(f'Found part {part} @ ({pos}, {line_number}) for {number} ({span}, {line_number})')
                    print(f'Line {line_number}: {lines[line_number]}')
                    if line_number != line:
                        print(f'Line {line}: {lines[line]}')
                    parts[line][pos][part].append(number)
                    return True
    return False

numbers, parts, lines = read_schematic('input/day-3.txt')
total = 0
for line_number, span, number in numbers:
    if count_number(line_number, span, parts, number, lines):
        total += number
print(total)
total = 0
for line in parts:
    for pos in parts[line]:
        for part in parts[line][pos]:
            if part == '*' and len(parts[line][pos][part]) == 2:
                gear_ratio = parts[line][pos][part][0] * parts[line][pos][part][1]
                print(f'Found gear {part} @ ({pos}, {line}) with ratio {parts[line][pos][part][0]}*{parts[line][pos][part][1]}={gear_ratio}:')
                if line > 0:
                    print(f'Line {line-1}: {lines[line-1]}')
                print(f'Line {line}: {lines[line]}')
                if line < len(lines)-1:
                    print(f'Line {line+1}: {lines[line+1]}')
                total += gear_ratio
print(total)


