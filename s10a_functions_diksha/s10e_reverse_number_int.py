#!/usr/bin/python3
# Write a program to generate the reverse of a given number N.
# Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them.
# For e.g., reverse of 10400 will be 401 instead of 00401.

# Sample Input : 1234
# Sample Output : 4321

def reverse_int(n: int) -> int:
    digits = []
    while n != 0:
        q, r = divmod(n, 10)
        digits.append(r)
        n = q

    power = len(digits)
    number = 0
    for i in range(power):
        number += digits[i] * (10 ** (power - i - 1))

    return number

print(reverse_int(int(input("Enter a number to reverse: "))))
