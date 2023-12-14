#!/usr/bin/env python3
import sys

def find_reflections(vector):
    print(f'find_reflections({vector}):', end='')
    result = []
    for i in range(1, len(vector)):
        if i <= len(vector)/2:
            #print(vector[:i], list(reversed(vector[i:2*i])))
            comparison = zip(vector[:i],reversed(vector[i:2*i]))
        else:
            #print(vector[2*i-len(vector):i], list(reversed(vector[i:])))
            comparison = zip(vector[2*i-len(vector):i],reversed(vector[i:]))
        equal = [a==b for a,b in comparison]
        #print(i, list(comparison), equal, all(equal))
        if all(equal):
            result.append(i)
    print(result)
    return set(result)

def handle_map(horizontal, vertical):
    print(horizontal)
    print(find_reflections(horizontal))
    print(vertical)
    print(find_reflections(vertical))
    return sum(find_reflections(horizontal))+100*sum(find_reflections(vertical))

def handle_map_part2(horizontal, vertical):
    original_horizontal = find_reflections(horizontal)
    original_vertical = find_reflections(vertical)
    total = 0
    for h in range(len(vertical)):
        for v in range(len(horizontal)):
            print(h, v, horizontal[v], vertical[h])
            horizontal[v] = horizontal[v] ^ (1 << (len(vertical)-h-1))
            vertical[h] = vertical[h] ^ (1 << (len(horizontal)-v-1))
            print(h, v, horizontal[v], vertical[h])
            new_horizontal = find_reflections(horizontal) - original_horizontal
            new_vertical = find_reflections(vertical) - original_vertical
            if new_horizontal or new_vertical:
                print(f'result: {sum(new_horizontal)+100*sum(new_vertical)}')
                return sum(new_horizontal)+100*sum(new_vertical)
            horizontal[v] = horizontal[v] ^ (1 << (len(vertical)-h-1))
            vertical[h] = vertical[h] ^ (1 << (len(horizontal)-v-1))
            print(h, v, horizontal[v], vertical[h])

def process(filename):
    horizontal, vertical = [], []
    total1, total2 = 0, 0
    for line in open(filename):
        line = line.strip()
        if line != '':
            line = line.replace('.','0').replace('#','1')
            vertical.append(int(line,2))
            if horizontal == []:
                horizontal = ['']*len(line)
            horizontal = [s+line[i] for i,s in enumerate(horizontal)]
        else:
            horizontal = [int(s,2) for s in horizontal]
            total1 += handle_map(horizontal, vertical)
            total2 += handle_map_part2(horizontal, vertical)
            horizontal, vertical = [], []
    # last map
    horizontal = [int(s,2) for s in horizontal]
    total1 += handle_map(horizontal, vertical)
    total2 += handle_map_part2(horizontal, vertical)
    print(total1)
    print(total2)

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-13.txt')
