#!/usr/bin/env python3

# infinite recursion
#def printn(n):
#    print(n)
#    printn(n + 1)
#    return


#printn(1)

def printn(n):
    if (n == 6):
        return
    print(n)
    printn(n)
    return


print(1)
