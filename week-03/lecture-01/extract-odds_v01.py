#!/usr/bin/env python3

def extract_odds(numbers):
    odds = []
    for n in numbers:
        if n % 2 == 1:
            odds.append(n)
        #are you an odd number?
    return odds

print(extract_odds([1, 2, 3, 4, 5, 6, 7, 8]))
