#!/usr/bin/env python3
import sys

def replace_start(maze, size, start):
    north = 0 < start[1]         and maze[start[1]-1][start[0]] in '|7F'
    south = start[1] < size[1]-1 and maze[start[1]+1][start[0]] in '|LJ'
    east  = start[0] < size[0]-1 and maze[start[1]][start[0]+1] in '-7J'
    west  = 0 < start[0]         and maze[start[1]][start[0]-1] in '-LF'

    if   north and south:
        symbol = '|'
    elif north and west:
        symbol = 'J'
    elif north and east:
        symbol = 'L'
    elif east and south:
        symbol = 'F'
    elif east and west:
        symbol = '-'
    elif south and west:
        symbol = '7'
    else:
        print(f'Failed: {size} {start} {north} {east} {south} {west}')
    print(f'Start symbol: {size} {start} {north} {east} {south} {west}: {symbol}')
    maze[start[1]] = maze[start[1]].replace('S', symbol)

# (dx,dy) per symbol
STEP = { '|': [( 0,-1), ( 0,+1)],
         '-': [(-1, 0), (+1, 0)],
         'L': [( 0,-1), (+1, 0)],
         'J': [( 0,-1), (-1, 0)],
         '7': [( 0,+1), (-1, 0)],
         'F': [( 0,+1), (+1, 0)]
       }

def take_step(maze, now, previous):
    steps = STEP[maze[now[1]][now[0]]]
    option1 = (now[0]+steps[0][0],now[1]+steps[0][1])
    option2 = (now[0]+steps[1][0],now[1]+steps[1][1])
    if option1 != previous:
        print(f'From {now} via {maze[now[1]][now[0]]} to {option1} (before {previous})')
        return option1, now
    else:
        print(f'From {now} via {maze[now[1]][now[0]]} to {option2} (before {previous})')
        return option2, now

def furthest_point(maze, start):
    now, previous = take_step(maze, start, (-2,-2))
    steps = 1
    while now != start:
        print(f'After {steps} steps, now in {now} (coming from {previous})', end=' ')
        now, previous = take_step(maze, now, previous)
        steps += 1
    return int(steps/2)

def process(filename):
    maze = []
    line_no = 0
    start = (-1,-1)
    for line in open(filename):
        line = line.strip()
        maze.append(line)
        start_x = line.find('S')
        if start_x > -1:
            start = (start_x, line_no)
        line_no+=1
    maze_size = (len(maze[0]),len(maze))
    replace_start(maze, maze_size, start)
    print(furthest_point(maze, start))

if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-10.txt')
