#!/usr/bin/env python3

def parse_line(s):
    result = []
    game, draws = line.split(':')
    game = int(game.split(' ')[1])
    draws = draws.split(';')
    for draw in draws:
        result.append({})
        cubes = draw.split(',')
        for cube in cubes:
            number, color = cube.split()
            number = int(number)
            result[-1][color] = number
    return game, result

def valid_game(game, max_colors):
    for draw in game:
        for color in max_colors:
            if draw.get(color,0) > max_colors[color]:
                return False
    return True

def game_power(game, colors = ['red', 'green', 'blue']):
    max_colors = { color: 0 for color in colors }
    for draw in game:
        for color in max_colors:
            max_colors[color] = max(max_colors[color], draw.get(color,0))
    power = 1
    for color in colors:
        power *= max_colors[color]
    return power

correct = 0
power = 0
for line in open('input/day-2.txt'):
    game, result = parse_line(line.strip())
    if valid_game(result, {'red': 12, 'green': 13, 'blue': 14}):
        correct += game
    else:
        print(f'Incorrect: {line.strip()}')
    power += game_power(result)
print(correct)
print(power)
