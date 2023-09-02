#!/usr/bin/env python3

class Stack(object):

     def __init__(self):
         self.s = []

     def push(self, e):
         self.s.append(e)

     def pop(self):
         if self.s != []:
             return self.s.pop()

     def top(self):
         return self.s[-1]

     def is_empty(self):
         return len(self.s) == 0

     def __len__(self):
         return len(self.s)

s = Stack()

string = '2 3 +'

for ch in string:
    if ch.isdigit():
        stack.push(float(ch))

print(stack)
