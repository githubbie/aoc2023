#!/usr/bin/env python3
import re

int_map = { 'one'   : 1,
            'two'   : 2,
            'three' : 3,
            'four'  : 4,
            'five'  : 5,
            'six'   : 6,
            'seven' : 7,
            'eight' : 8,
            'nine'  : 9 }

int_map.update({str(i): i for i in range(10)})

def reverse(s):
    return s[::-1]

regex_digits = re.compile('\d')
regex = re.compile('('+'|'.join(int_map.keys())+')')
regex_reverse = re.compile('('+'|'.join([reverse(s) for s in int_map.keys()])+')')

sum1 = 0
sum2 = 0
for line in open('input/day-1.txt'):
    line = line.strip()
    digits = regex_digits.findall(line)
    first = regex.search(line).groups()[0]
    last = regex_reverse.search(reverse(line)).groups()[0]
    number1 = 10*int(digits[0]) + int(digits[-1])
    sum1 += number1
    number2 = 10*int_map[first] + int_map[reverse(last)]
    sum2 += number2
    print(line, first, last, number1, sum1, number2, sum2)
print(sum1)
print(sum2)
