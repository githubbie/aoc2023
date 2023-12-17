#!/usr/bin/env python3
import sys

def hash(s):
    current = 0
    for c in s:
        current = ((current+ord(c)) * 17) % 256
    return current

def do(instruction, boxes):
    label, length = instruction[:-1], instruction[-1]
    if length == '-':
        # remove
        box = hash(label)
        if label in boxes[box]:
            del boxes[box][label]
    else:
        label = label[:-1]
        box = hash(label)
        boxes[box][label] = int(length)

def print_boxes(boxes):
    for i, box in enumerate(boxes):
        if box:
            print(f'Box {i}:', end='')
            for label in box:
                print(f' [{label} {box[label]}]', end='')
            print()

def power(boxes):
    def p(box):
        return sum([(i+1)*length for i, length in enumerate(box.values())])
    return sum([(i+1)*p(box) for i,box in enumerate(boxes)])

def process(filename):
    for line in open(filename):
        line = line.strip()
        total = sum([hash(instruction) for instruction in line.split(',')])
        print(total)
        boxes = []
        for i in range(256):
            boxes.append({})
        print('Initialize')
        print_boxes(boxes)
        for instruction in line.split(','):
            print('Instruction:', instruction)
            do(instruction, boxes)
            print_boxes(boxes)
        print(power(boxes))

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-15.txt')
