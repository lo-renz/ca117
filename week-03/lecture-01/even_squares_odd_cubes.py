#!/usr/bin/env python3

def even_squares_odd_cubes(numbers):
    evens = []
    for even in numbers:
        if even % 2 == 0:
            evens.append(even ** 2)

    odds = []
    for odd in numbers:
        if odd % 2 == 1:
            odds.append(odd ** 3)

    return 
