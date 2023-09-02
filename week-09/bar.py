#!/usr/bin/env python3

def bar(n):
    if n == 0:
        return 0
    return bar(n - 1)

print(bar(10))
