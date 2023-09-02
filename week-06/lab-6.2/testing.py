#!/usr/bin/env python3

def testing(x):
    if x % 2 == 0:
        return True
    else:
        return False


x = 10
for i in range(1, x + 1):
    print(f'{i:>2} = {testing(i)}')
