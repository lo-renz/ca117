#!/usr/bin/env python3

s = "alphanumeric@123_"

t = "".join(ch for ch in s if ch.isalnum())
print(t)
