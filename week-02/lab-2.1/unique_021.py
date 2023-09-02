#!/usr/bin/env python3

import sys
import string

input = sys.stdin.read().lower().strip().split()
#print(input)

tokens = []
for w in input:
    s = w.strip(string.punctuation)
    tokens.append(s)

#print(tokens)
#print(len(input))
#print(len(tokens))

unique = []
for uw in tokens:
    if uw not in unique and (uw.isalpha() or uw.isdigit()):
        unique.append(uw)
        print(uw)

print(len(unique))

#words = []
#for word in tokens:
#    if word.isalnum():
#        words.append(word)

#print(words)

#words = []
#for word in input:
#    if word.isalnum():
#        words.append(word)

#unique = []
#uw stands for unique word
#for uw in words:
#    if uw not in unique:
#        unique.append(uw)
#        print(uw)

#print(len(unique))
