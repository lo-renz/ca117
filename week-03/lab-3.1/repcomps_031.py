#!/usr/bin/env python3

import sys

def replace(numbers):
    return ["X" if n % 3 == 0 else n for n in numbers]


def main():
    for line in sys.stdin:
        numbers = []
        n = int(line)
        for i in range(1, n + 1):
            numbers.append(i)
        print(replace(numbers))


if __name__ == "__main__":
    main()
