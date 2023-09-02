#!/usr/bin/env python3

import sys

file1 = []
f1 = open(sys.argv[1], "r")
for n in f1:
    file1.append(int(n))
f1.close()

file2 = [0]
f2 = open(sys.argv[2], "r")
for m in f2:
    file2.append(int(m))
f2.close()

i = 0
while i < len(file1):
    print(file1[i])
    print(file2[i + 1])
    i += 1
