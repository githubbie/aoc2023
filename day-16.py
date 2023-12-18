#!/usr/bin/env python3
import sys

def process_beams(map, beams, energized, processed):
    new_beams = []
    for x,y,dx,dy in beams:
        if (x,y,dx,dy) in processed:
            # already handled this, ignore
            pass
        elif x+dx >= len(map[0]) or x+dx < 0 or y+dy >= len(map) or y+dy < 0:
            # leaving the map
            pass
        else:
            processed.add((x,y,dx,dy))
            energized[y+dy][x+dx] = True
            if (map[y+dy][x+dx] == '.') or \
               (map[y+dy][x+dx] == '|' and dx == 0) or  \
               (map[y+dy][x+dx] == '-' and dy == 0):
                new_beams.append((x+dx, y+dy, dx, dy))
            elif map[y+dy][x+dx] == '|' and dy == 0:
                new_beams.append((x+dx, y+dy, 0, 1))
                new_beams.append((x+dx, y+dy, 0, -1))
            elif map[y+dy][x+dx] == '-' and dx == 0:
                new_beams.append((x+dx, y+dy, 1, 0))
                new_beams.append((x+dx, y+dy, -1, 0))
            elif map[y+dy][x+dx] == '\\':
                new_beams.append((x+dx, y+dy, dy, dx))
            elif map[y+dy][x+dx] == '/':
                new_beams.append((x+dx, y+dy, -dy, -dx))
    return new_beams

def dump_energized(energized):
    for line in energized:
        print(''.join([{False: '.', True: '#'}[e] for e in line]))

def process_map(map, initial_position):
    beams = [initial_position]
    energized = [[False for _ in map[0]] for _ in map]
    processed = set()
    while beams != []:
        #print("Beams:", beams)
        #dump_energized(energized)
        beams = process_beams(map, beams, energized, processed)
    #print("Final:")
    #dump_energized(energized)
    return sum([sum(e) for e in energized])

def process_map1(map):
    print(process_map(map, (-1,0,1,0)))

def process_map2(map):
    max_total = -1
    for x in range(len(map[0])):
        max_total = max(max_total,
                        process_map(map, (x, -1, 0, 1)),
                        process_map(map, (x, len(map)+1, 0, -1)))
    for y in range(len(map)):
        max_total = max(max_total,
                        process_map(map, (-1, y, 1, 0)),
                        process_map(map, (len(map[0]), y, -1, 0)))
    print(max_total)

def process(filename):
    map = []
    for line in open(filename):
        map.append(line.strip())
    process_map1(map)
    process_map2(map)

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-16.txt')
