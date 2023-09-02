#!/usr/bin/env python3

import sys

def main():
# This code puts the inputs into a list.
    with open(sys.argv[1], "r") as f:
        group = []
        line = f.readline().strip()
        while line != "":
            group.append(line)
            line = f.readline().strip()

#print(lines)

# This code looks for the best mark.
    best_mark = 0
    for student_mark in group:
        if int(student_mark[:2]) > best_mark:
            best_mark = int(student_mark[:2])

# print(best_mark)

    best_students = []
    for student in group:
        if int(student[:2]) == best_mark:
            best_students.append(student[3:])

    print(f"Best student(s): {', '.join(best_students)}")
    print(f"Best mark: {best_mark}")


if __name__ == "__main__":
    main()
