#!/usr/bin/env python3

def allvowels(s):
    # return whether all vowels are in s
    return 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s


low = ['zebra', 'aeiouzzz', 'saeiou', 'cats', 'dog']

aws = [w for w in low if allvowels(w.lower())]

print(aws)

print(min(aws, key=len))

#slow = sorted(low)
#print(slow)
#print(min(low))
#print(max(low))

# find the word which is the smallest in the length sense of a word.
# the key's job is to return the attribute we are interested in.
#print(min(low, key=len))
