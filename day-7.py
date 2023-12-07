#!/usr/bin/env python3
import sys
from collections import Counter


ALLCARDS='23456789TJQKA'
ALLCARDS_J='J23456789TQKA'

def order(hand, joker):
    integer = 1
    for card in hand:
        if joker:
            integer = integer * 20 + ALLCARDS_J.find(card)
        else:
            integer = integer * 20 + ALLCARDS.find(card)
    return integer

def strength(hand, joker):
    counts = Counter()
    for card in hand:
        counts.update({card: 1})
    if joker:
        jokers = counts['J']
        del counts['J']
    else:
        jokers = 0
    ordered = counts.most_common()
    if jokers == 5 or (ordered[0][-1]+jokers == 5):
        return 7 # five of a kind
    if ordered[0][-1]+jokers == 4:
        return 6 # four of a kind
    if len(ordered) > 1 and (ordered[0][-1]+jokers == 3) and (ordered[1][-1] == 2):
        return 5 # full house
    if ordered[0][-1]+jokers == 3:
        return 4 # three of a kind
    if len(ordered) > 1 and (ordered[0][-1]+jokers == 2) and (ordered[1][-1] == 2):
        return 3 # two pair
    if ordered[0][-1]+jokers == 2:
        return 2 # one pair
    return 1 # high card
        
def process(filename, jokers):
    hands = []
    for line in open(filename):
        line = line.strip()
        hand,bid = line.split()
        bid = int(bid)
        print(f'Input {hand}: {strength(hand, jokers)}, {order(hand, jokers)}, {bid}')
        hands.append((strength(hand, jokers), order(hand, jokers), hand, bid))
    hands.sort()
    #print(hands)
    win = 0
    for i in range(len(hands)):
        win += hands[i][-1]*(i+1)
    print(win)

if len(sys.argv) > 1:
    process(sys.argv[1], True)
else:
    process('input/day-7.txt', True)
