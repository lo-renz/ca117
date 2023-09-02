#!/usr/bin/env python3

import sys

words = []
for line in sys.stdin:
    line = line.split()
    for word in line:
        if word.isalpha():
            word = word.lower()
            words.append(word)

altogether = "".join(words)

vowels = [v for v in altogether if v in "aeiou"]

freq = {}
for vowel in vowels:
    if vowel not in freq:
        freq[vowel] = 1
    elif vowel in freq:
        freq[vowel] = freq[vowel] + 1

for k, v in sorted(freq.items()):
    print(f'{k} : {v}')
