#!/usr/bin/env python3

s = "Summer_has_arrived!"
try:
    print('A: {:s}'.format(s[::3]))
    print('B: {:s}'.format(s[-100:100]))
    i = len(s) // 5
    s[i].upper()
    print('C: {:s}'.format(s[i]))
except:
    print('Something went wrong!')
