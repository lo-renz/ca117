#!/usr/bin/env python3

def sum_up_to(n):
    if n == 0:
        return 0
    return n + sum_up_to(n - 1)


print(sum_up_to(10))
