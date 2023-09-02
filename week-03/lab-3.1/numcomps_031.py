#!/usr/bin/env pyton3

import sys

def multiples_of_3(numbers):
    return [n for n in numbers if n % 3 == 0]


def square_multiples_of_3(numbers):
    return [n**2 for n in numbers if n % 3 == 0]


def double_multiples_of_4(numbers):
    return [n*2 for n in numbers if n % 4 == 0]


def multiples_of_3_or_4(numbers):
    return [n for n in numbers if n % 3 == 0 or n % 4 == 0]


def multiples_of_3_and_4(numbers):
    return [n for n in numbers if n % 3 == 0 and n % 4 == 0]

def main():
    for n in sys.stdin:
        a = []
        for i in range(1, int(n) + 1):
            a.append(i)
        print(f'Multiples of 3: {multiples_of_3(a)}')
        print(f'Multiples of 3 squared: {square_multiples_of_3(a)}')
        print(f'Multiples of 4 doubled: {double_multiples_of_4(a)}')
        print(f'Multiples of 3 or 4: {multiples_of_3_or_4(a)}')
        print(f'Multiples of 3 and 4: {multiples_of_3_and_4(a)}')


if __name__ == "__main__":
    main()
