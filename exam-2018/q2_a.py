#!/usr/bin/env python3

def foo(l):
 q = []
 try:
    for i in l:
        q.append(i+1)
 except:
    q.append('x')
 else:
    print('y')
 finally:
    print('z')
    print(q)

print('foo()')
foo([3, 'a', 'b', 4])
