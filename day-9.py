#!/usr/bin/env python3
import sys

def predict_forward(values):
    if values == [0]*len(values):
        print(f'predict_forward({values}) = 0')
        return 0
    else:
        delta = [values[i+1]-values[i] for i in range(len(values)-1)]
        prediction = predict_forward(delta)
        print(f'predict_forward({values}) = {values[-1]+prediction}')
        return values[-1]+prediction

def predict_backward(values):
    if values == [0]*len(values):
        print(f'predict_backward({values}) = 0')
        return 0
    else:
        delta = [values[i+1]-values[i] for i in range(len(values)-1)]
        prediction = predict_backward(delta)
        print(f'predict_backward({values}) = {values[0]-prediction}')
        return values[0]-prediction

def process(filename):
    total_forward = 0
    total_backward = 0
    for line in open(filename):
        line = line.strip()
        readings = [int(s) for s in line.split()]
        prediction = predict_forward(readings)
        total_forward += prediction
        prediction = predict_backward(readings)
        total_backward += prediction
    print(total_forward)
    print(total_backward)


if len(sys.argv) > 1:
    process(sys.argv[1])
else:
    process('input/day-9.txt')
