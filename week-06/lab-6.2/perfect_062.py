#!/usr/bin/env python3

import sys

def sum_factors(n):
    sum_of_factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_factors.append(i)
    return sum_of_factors


for line in sys.stdin:
    n = int(line)
    if sum(sum_factors(n)) == n:
        print(True)
    else:
        print(False)
