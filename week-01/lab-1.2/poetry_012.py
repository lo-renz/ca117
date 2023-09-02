#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

curr = 0

for line in lines:
    prev = len(line) - 1 
    if curr < prev:
        curr = prev

for line in lines:
    line = line.strip()
    print(f'{line:^{curr}}')
