#!/usr/bin/env python3

import sys
from math import sqrt

class Stack(object):

    def __init__(self):
        self.list = []

    def push(self, e):
        self.list.append(e)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def is_empty(self)
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)

binops = {'+': float.__add__, '-': float.__sub__, '*': float.__mul__, '/': float.__truediv__}

uniops = {'n': float.__neg__, 'r': sqrt}

def calculator(line):

    stack = Stack()
    tokens = line.strip().split()

    for token in tokens:
        for n in token:
            if n.isdigit():
                list.push(float(n))



tests = ['5', '8.5 2 /', '2 3 +', '2 3 r +', '1 2 3 * +', '5 2 n *', '1 2 3 + -', '2 1 2 3 + - *', '2 1 2 3 + - * n', '2 1 2 3 + - * n r', '6 +', '9 r']

def main():

    for test in tests:
        try:
            a = calculator(test.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')


if __name__ == "__main__":
    main()
