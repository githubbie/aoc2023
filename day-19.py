#!/usr/bin/env python3
import sys
import re
import math

instr_re = re.compile('(?P<variable>[a-z]*)(?P<op>[<>])(?P<value>[0-9]*):(?P<label>[a-zA-Z]*)')

def part_value(part, label, program):
    for instruction in program[label]:
        label = instruction['label']
        if 'variable' in instruction:
            lvalue = int(part[instruction['variable']])
            rvalue = int(instruction['value'])
            evaluation = (instruction['op'] == '<' and lvalue < rvalue) or \
                         (instruction['op'] == '>' and lvalue > rvalue)
        else:
            evaluation = True
        if evaluation:
            if label == 'A':
                return sum([int(v) for v in part.values()])
            elif label == 'R':
                return 0
            else:
                print(f' -> {label}', end='')
                return part_value(part, label, program)

def num_parts(parts):
    return math.prod(v[1]-v[0] for v in parts.values())

def num_accepted(parts, label, program):
    initial_label = label
    total = 0
    for instruction in program[label]:
        label = instruction['label']
        if 'variable' in instruction:
            variable = instruction['variable']
            rvalue = int(instruction['value'])
            true_parts = parts.copy()
            false_parts = parts.copy()
            a,b = parts[variable]   # a <= variable < b
            if instruction['op'] == '<':
                true_parts[variable] = (a, min(b, rvalue))
                false_parts[variable] = (max(a, rvalue), b)
            else:
                true_parts[variable] = (max(a, rvalue+1), b)
                false_parts[variable] = (a, min(b, rvalue+1))
            if true_parts[variable][0] >= true_parts[variable][1]:
                true_parts = {}
            if false_parts[variable][0] >= false_parts[variable][1]:
                false_parts = {}
        else:
            true_parts = parts.copy()
            false_parts = {}
        if true_parts != {}:
            if label == 'A':
                total += num_parts(true_parts)
            elif label == 'R':
                pass
            else:
                total += num_accepted(true_parts, label, program)
        if false_parts == {}:
            break
        else:
            parts = false_parts
    return total

def process(filename):
    program = {}
    parts = []
    in_program = True
    for line in open(filename):
        line = line.strip().replace('{',' ').replace('}',' ').replace(',',' ')
        if line == '':
            in_program = False
        elif in_program:
            label, *instructions = line.split()
            program[label]=[]
            for instruction in instructions:
                match = instr_re.match(instruction)
                if match:
                    program[label].append(match.groupdict())
                else:
                    program[label].append({'label': instruction})
        else:
            part = {}
            for assignment in line.split():
                variable, value = assignment.split('=')
                part[variable]=value
            parts.append(part)
    print(program)
    print(parts)
    total = 0
    for part in parts:
        print(f'{part}: in', end='')
        value = part_value(part, 'in', program)
        print(f' {value}')
        total += value
    print(total)
    possible_parts = {'x': (1,4001), 'm': (1,4001), 'a': (1,4001), 's': (1,4001)}
    print(num_accepted(possible_parts, 'in', program))

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-19.txt')
