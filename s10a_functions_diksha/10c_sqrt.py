#!/usr/bin/python3
# Given a number N, find its square root. You need to find and print only the integral part of the square root of N.
# For eg. if the number given is 18, answer is 4.
from math import sqrt

def int_sq(n: int) -> int:
    return int(sqrt(n))

print(int_sq(int(input("Enter a number: "))))
