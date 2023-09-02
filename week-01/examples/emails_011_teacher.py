#!/usr/bin/env python3

#email = "valerie.maguire2@mail.dcu.ie"
#[left, _] = email.split("@")
#print(left)
# print(right)
#print(left.strip("0123456789"))
#
#left = left.strip("0123456789")
#
#[fname, sname] = left.split(".")
#print(fname)
#print(sname)
#print(" ".join([fname.capitalize(), sname.capitalize()]))

#import sys
#
#for email in sys.stdin:
#    [left, _] = email.split("@")
#    left = left.strip("1234567890")
#    [fname, sname] = left.split(".")
#    print(" ".join([fname.capitalize(), sname.capitalize()]))

def email(s):
    #...
    [left, _] = s.split("@")
    left = left.strip("1234567890")
    [fname, sname] = left.split(".")
    return " ".join(fname.capitalize(), sname.capitalize())

print(email("valerie.maguire2@mail.dcu.ie"))
