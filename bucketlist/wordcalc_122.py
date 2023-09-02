#!/usr/bin/env python3

import sys

w2n = {}
n2w = {}
for line in sys.stdin:
    tokens = line.strip().split()

    if tokens[0] == 'def':
        w2n[tokens[1]] = int(tokens[2])
        if tokens[2] not in n2w:
            n2w[tokens[2]] = tokens[1]
        elif tokens[2] in n2w:
            n2w[tokens[2]].remove()

    elif tokens[0] == 'calc':
        total = w2n[tokens[1]]

        try:
            i = 0
            while i < len(tokens):
                if tokens[i] == '+':
                    total = total + w2n[tokens[i + 1]]

                elif tokens[i] == '-':
                    total = total - w2n[tokens[i + 1]]
                i += 1

            print(' '.join(tokens[1:]) + " " + n2w[str(total)])
#            print(' '.join(tokens[1:]) + n2w[total])

        except KeyError:
            print(' '.join(tokens[1:]) + ' unknown')

    elif tokens[0] == 'clear':
        n2w = {}
        w2n = {}
