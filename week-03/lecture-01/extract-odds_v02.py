#!/usr/bin/env python3

def extract_odds(numbers):
    return [n for n in numbers if n % 2 == 1]


print(extract_odds([1, 2, 3, 4, 5, 6, 7, 8]))
