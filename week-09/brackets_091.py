#!/usr/bin/env python3

import sys

class Stack(object):

    def __init__(self):
        self.l = []

    # s.push(e): add e to the stack
    def push(self, e):
        self.l.append(e)

    # s.pop(): remove and return element at top of stack
    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0
    # or you can do return not(self.l)

    def __len__(self):
        return len(self.l)

# helper dictionary: keys close values.
d = { ')':'(', '}':'{', ']':'['}

# lefties ({[
# righties )}]

def matcher(line):
    s = Stack()

    # for each character in line.
        # we are interested in tracking opening brackets.
        # id the current character a ledty?
        # if yes push it on the stack.

        # is the current character a righty?
        # if so, verify ot closes the lefty at the top of the stack.

    for c in line:
        if c in d.values():
            s.push(c)

        if c in d.keys(): # does c close s.pop()
            # map c to what it closes.
            if d[c] != s.pop(c):
                return False

    return s.is_empty()
