#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    #print(line)
    i = 0
    while i < len(line):
        if line[i] in "aeiou":
            line = line[:i] + line[i + 2:]
        i += 1

    print(line)
