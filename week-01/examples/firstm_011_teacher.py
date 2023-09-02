#!/usr/bin/env python3

line = "Mickey Mouse was a kind of mouse. A mouse with a sense of humor"

#print(line)
#tokens = line.strip().split()
#print(tokens)
#i = 0
#while i < len(tokens):
#    if tokens[i].startswith("m"):
#        tokens[i] = tokens[i].capitalize()
#        break
#    # print(tokens[i])
#    i += 1
#print(tokens)
#
#print(" ".join(tokens))

import sys

def firstm(s):
    tokens = line.strip().split()
    i = 0
    while i < len(tokens):
        if tokens[i].startswith("m"):
            tokens[i] = tokens[i].capitalize()
            break
        i += 1
    return " ".join(tokens)

print(firstm(line))
