#!/usr/bin/env python3

import sys
from math import pi

for line in sys.stdin:
    n = int(line)
    print(f'{pi:.{n}f}')
