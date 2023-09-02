#!/usr/bin/env python3

def isprime(n):
    
    if n <= 1:
        return False

    for i in range(2, n // 2 + 1): 
        # make sure n // s is included
        # is i a factor of n
        # if i divides evenly into a
        if n % i == 0:
            return False

    return True


for line in sys.stdin:
    m  = int(line.strip()) + 1

    primes = [n for n in range(m) if isprime(n)]

