#!/usr/bin/env python3
import sys

def read_cards(filename):
    multiplier = [1]*220
    win = 0
    for line in open(filename):
        line = line.strip()
        card, numbers = line.split(':')
        card = int(card.split()[1])
        print(f'{line} [multiplier: {multiplier[card]}]')
        winning, drawn = numbers.split('|')
        winning = set([int(s) for s in winning.split()])
        drawn = set([int(s) for s in drawn.split()])
        count = len(winning & drawn)
        if count > 0:
            prize = 2**(count-1)
        else:
            prize = 0
        for i in range(1,count+1):
            multiplier[card+i]+=multiplier[card]
        win += prize*multiplier[card]
        #print(f'{winning}, {drawn}, {winning & drawn}')
        #print(f'Multipliers {multiplier}')
        print(f'Card {card}: {count} winners for {prize} with multiplier {multiplier[card]}: {winning & drawn}. Total now {win}')
    print(win)
    print(sum(multiplier[1:card+1]))

if len(sys.argv) > 1:
    read_cards(sys.argv[1])
else:
    read_cards('input/day-4.txt')
