#!/usr/bin/env python

import numpy as np

first = np.random.seed(123)
wet, h, t = [], 0, 0
e = 0
while e < 100:
    second = np.random.randint(0, 2)
    wet.append(second)
    e += 1

def change(k):
    if k == 1:
        return "Head"
    return "Tail"
jane = map(change, wet)
print(h, t)
print(f"There are {h} heads and {t} tails")
