#!/usr/bin/env python3

import sys

def main():

    try:
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
            best_student = ""
            highest_mark = 0
            for line in lines:
                if int(line[:2]) > highest_mark:
                    highest_mark = int(line[:2])
                    best_student = line

            print(f"Best student:{best_student[2:]}".strip())
            print(f"Best mark: {highest_mark}")

    except FileNotFoundError:
        print(f"The file {sys.argv[1]} could not be opened.")

if __name__ == "__main__":
    main()
