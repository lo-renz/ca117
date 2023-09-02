#!/usr/bin/env python3

import sys

inputs = []
with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        inputs.append(line)

print(inputs)

for w in inputs:

    i = 0

    while i < len(inputs):

        line = sys.stdin.readline()

        while line != "":
            if inputs[i] in line:
                print(inputs[i])
            line = sys.stdin.readline()
        i += 1
