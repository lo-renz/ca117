#!/usr/bin/env python3

lines = ["Humpty Dumpty sat on a wall\n", "Humpty Dumpty had a great fall\n"]
#lines = sys.stdin.readlines()

for line in lines:
    print(line)
maxlen = -1
for line in lines:
    print(len(line.strip()))
    if len(line) > maxlen:
        maxlen = len(line.strip())
print(maxlen)
for line in lines:
    #print(lines.strip())
    print(f'{line.strip():^{maxlen}s}')
