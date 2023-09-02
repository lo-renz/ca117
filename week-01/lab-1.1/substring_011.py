#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        s = line.split()
        word1 = s[0].lower()
        word2 = s[1].lower()
        if word1 in word2:
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    main()
