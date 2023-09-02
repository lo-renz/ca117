#!/usr/bin/env python3

numbers = [3, 4, 6, 5, 1, 8]

def even_squares(list):
    return [n ** 3 if n % 2 else n ** 2 for n in numbers]

print(even_squares(numbers))
