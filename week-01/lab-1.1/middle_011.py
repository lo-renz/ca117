#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        s = line.strip()
        middle = s[len(s) // 2]
        if len(s) % 2 != 0:
            print(middle)
        else:
            print("No middle character!")


if __name__ == "__main__":
    main()
