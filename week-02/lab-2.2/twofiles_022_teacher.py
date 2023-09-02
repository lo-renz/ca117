#!/usr/bin/env python3

a_list = [1, 3, 5]
b_list = [2, 4, 6]

#print(list(zip(a_list, b_list)))
# print(zip(a_list, b_list))

#for (a, b) in zip(a_list, b_list):
#    print(a)
#    print(b)


with open(sys,argv[1], "r") as f:
    a_list = [line.strip() for line in f]

with open(sys.argv[2], "r") as f:
    b_list = [line.strip() fr line in f]


for (a, b) in zip(a_list, b_list):
    print(a)
    print(b)

# To use range
range(1, N + 1) # This will give you the numbers between 1 and "N" + 1
