#!/usr/bin/env python3

import sys

nums2words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten'
    }

words2translation = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
        word, translation = line.strip().split()
        words2translation[word] = translation

for line in sys.stdin:
    numbers = line.strip().split()
    slist = []

    for number in numbers:
        slist.append(words2translation[nums2words[number]])

    print(' '.join(slist))
