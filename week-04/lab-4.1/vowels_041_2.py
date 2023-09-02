#!/usr/bin/env python3

import sys

def tagger(item):
    return item[1]

# reads all of the input and makes a list with all the vowels that appear.
line = sys.stdin.read().lower()
vowels = [v for v in line if v in "aeiou"]

# puts the vowels into a dictionary and records it's frequency in the input.
freq = {}
for vowel in vowels:
    if vowel not in freq:
        freq[vowel] = 1
    elif vowel in freq:
        freq[vowel] = freq[vowel] + 1

#sort_values = sorted(freq.items(), key=lambda x:x[1], reverse=True)
width = len(str(max(freq.values())))
#for i in sort_values:
#    print(f'{i[0]} : {i[1]:>{width}}')

for k, v in sorted(freq.items(), key=tagger, reverse=True):
    print(f'{k} : {v:>{width}}')
