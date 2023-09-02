#!/usr/bin/env python3

import sys

for lines in sys.stdin:
    s = lines.strip()
    es = (s[-2:] == "ch" or s[-2:] == "sh" or s[-1] == "o")
    es1 = (s[-1] == "x" or s[-1] == "s" or s[-1] == "z")
    ies = (s[-2] in "bcdfghjklnmpqrstvywxz" and s[-1] == "y")
    ves = (s[-1] == "f")
    vesfe = (s[-2:] == "fe")
    if (es):
        print(s + "es")
    elif (es1):
        print(s + "es")
    elif (ies):
        print(s[:-1] + "ies")
    elif (ves):
        print(s[:-1] + "ves")
    elif (vesfe):
        print(s[:-2] + "ves")
    else:
        print(s + "s")

