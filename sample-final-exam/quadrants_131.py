#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()

    if int(line[0]) > 0 and int(line[1]) > 0:
        print(1)

    elif int(line[0]) > 0 and int(line[1]) < 0:
        print(2)

    elif int(line[0]) < 0 and int(line[1]) < 0:
        print(3)

    elif int(line[0]) < 0 and int(line[1]) > 0:
        print(4)
