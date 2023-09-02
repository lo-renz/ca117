#!/usr/bin/env python3

s = "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod."

# print(":".isalnum())

def palindrome(s):
    
    s = s.strip().lower()

    keep = []
    for c in s:
        if c.isalnum():
            keep.append(c)

    return keep == keep[::-1]:
    #    print(keep)


palindrome("cA,:t")
palindrome("abba")
