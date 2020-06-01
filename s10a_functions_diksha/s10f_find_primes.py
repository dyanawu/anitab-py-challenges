#!/usr/bin/python3
# Given an integer N, print all the prime numbers that lie in the range 2 to N (both inclusive).
# Print the prime numbers in different lines.

def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True

def small_primes(n):
    from math import sqrt, ceil
    limit = ceil(sqrt(n)) + 2
    return [x for x in range (2, limit) if is_prime(x)]

def greek_sift(number):
    bucket = list(range(1, number +1))
    sieve = small_primes(number)
    for prime in sieve:
        bucket = [x for x in bucket if (x % prime or x == prime) and x > 1]
    print("\n".join([str(x) for x in bucket]))

greek_sift(int(input("Enter a number: ")))
