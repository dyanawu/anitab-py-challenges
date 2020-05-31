#!/usr/bin/python3
# Given a number N, figure out if it is a member of fibonacci series or not.
# Return true if the number is a member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
# F(n) = F9n-1) + F(n-2)
# Where, F(0) = 0 and F(1) = 1

def is_fibonacci(n: int) -> bool:
    if n == 0:
        return True

    previous = 0
    current = 1
    while current < n:
        previous, current = current, current + previous

    return current == n

print(is_fibonacci(int(input("Enter a number: "))))
