#!/usr/bin/python3
# Write a program to generate the reverse of a given number N.
# Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them.
# For e.g., reverse of 10400 will be 401 instead of 00401.

# Sample Input : 1234
# Sample Output : 4321

def reverse_number(n: str) -> int:
    return int(n[::-1])

print(reverse_number(input("Enter a number to reverse: ")))
