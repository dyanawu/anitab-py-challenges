#!/usr/bin/python

num_list = [int(x) for x in input().split()]
print(num_list)

odd_one = 0
for n in num_list:
    odd_one ^= n

print(odd_one)
