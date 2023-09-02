#!/usr/bin/env python3

# a--------b palindrome if a -- b and the missle bit is a palindrome
#  c------d  palindorme if c -- d and middle bit is a palindrome
#   e----f   palindrome if e -- f and midde bit is a palindrome
#     gh     palindrome if g -- h and middle bit is a palindrome


def rpal(s):
    if s == '':
        return True
    return s[0] == s[-1] and rpal(s[1:-1])


print(rpal('123454321'))
