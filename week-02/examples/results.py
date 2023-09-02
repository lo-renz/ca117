#!/usr/bin/env python3

import sys

def main():
    with open("results.txt", "r") as f:

        for line in f:
            tokens = line.split()

            name = " ".join(tokens[:-1])
            mark = tokens[-1]

            if int(mark) >= 40:
                result = "passed"
            else:
                result = "failed"

            print(f'{name} {result} with a mark of {mark}')

if __name__ == "__main__":
    main()
