#!/usr/bin/env python3

def main01(a, b):


    try:
        N = a // b
        for x in range(N):
            print(x)

    except ZeroDivisionError:
        print("Something went wrong")
        return False


    return True


# main01(6, 2)
main01(6, 0)

