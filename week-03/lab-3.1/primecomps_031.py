#!/usr/bin/env python3

import sys

def primes(numbers):
    return [n for n in numbers if n > 1 and (n % 1 == n)]

def main():
    for line in sys.stdin:
        n = int(line)
        numbers = []
        for i in range(1, n + 1):
            numbers.append(i)
        print(primes(numbers))

if __name__ == "__main__":
    main()
