#!/usr/bin/env python3

import sys

letters = []
strlen = 0

for line in sys.stdin:
    line = line.strip()
    wordlen = len(line)
    strlen += 1

    i = 0
    while i < wordlen:
        letters.append(line[i])
        i += 1

words = []

j = 0
while j < wordlen:
    word = ''.join(letters[j::strlen + (wordlen - strlen)])
    words.append(word)
    j += 1

slist = sorted(words, key=str.lower)

try:
    for i in range(len(slist)):
        for x in slist:
            print(x[i], end='')
        print()
except IndexError:
    pass

#print(slist)

#print(letters)
#print(words)
#print(wordlen)
#print(strlen)
