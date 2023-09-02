#!/usr/bin/env python3

import sys

a = []
for numbers in sys.stdin.readline().strip().split():
    if numbers.isdigit():
        a.append(int(numbers))

a = sorted(a)
A = a[0]
B = a[1]
C = a[2]

order = sys.stdin.readline().strip()
output = []

if order[0] == "A":
    output.append(str(A))
elif order[0] == "B":
    output.append(str(B))
elif order[0] == "C":
    output.append(str(C))

if order[1] == "A":
    output.append(str(A))
elif order[1] == "B":
    output.append(str(B))
elif order[1] == "C":
    output.append(str(C))

if order[2] == "A":
    output.append(str(A))
elif order[2] == "B":
    output.append(str(B))
elif order[2] == "C":
    output.append(str(C))

print(" ".join(output))

