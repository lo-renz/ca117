#!/usr/bin/env python3

# let's try to come up with a recursive approach to
# computing the length of a string.

# Q1. What is the simplist possible string we could be passed? This is our base case.
# Q2.

# ''
# abcde
# 1 + bcde
#   1 + cde
#       1 + de
#           1 + e
#               1 + ''

def rlen(s):
    if s == '':
        return 0
    return 1 + rlen(s[1:])

s = 'GAGO'

print(s, rlen(s))
print(rlen(''))
