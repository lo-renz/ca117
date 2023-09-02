#!/usr/bin/env python3

import sys

nums2words = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten'
    }

for numbers in sys.stdin:
    numbers = numbers.strip().split()
    slist = []
    for number in numbers:
        slist.append(nums2words[int(number)])
    print(' '.join(slist))
