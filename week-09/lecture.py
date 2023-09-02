#!/usr/bin/env python3

# Define out class here
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

# use a stack to print out the elements of a list in reverse order.
mylist = [1, 2, 3, 4, 6]
s = Stack()
for n in mylist:
    s.push(n)

print(len(s))
print(s.top())

while not(s.is_empty()): # for as long as the stack is not empty.
    print(s.pop())
