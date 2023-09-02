#!/usr/bin/env python3

import sys

def chop(s):
    return s[1:len(s) - 1]

for line in sys.stdin:
    # print(line.strip())
    s = line.strip()
    # if not empty string then print it
    chopped = chop(s)
    if len(chopped) > 0:
        print(chopped)
