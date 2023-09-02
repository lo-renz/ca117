#!/usr/bin/env python3

import sys

def allvowels(w):
    return 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w

def main():

    l = [line.strip() for line in sys.stdin]

    words_allvowels = [w for w in l if allvowels(w.lower())]
    print(f'Shortest word containing all vowels: '
          f'{min(words_allvowels, key=len)}')

    words_iary = [w for w in l if w.lower().endswith('iary')]
    print(f'Words ending in iary: {len(words_iary)}')

    most_ees = max([w.lower().count('e') for w in l])

    words_most_ees = [w for w in l if w.lower().count('e') == most_ees]
    print(f'Words with most e\'s: {words_most_ees}')

if __name__ == "__main__":
    main()
