#!/usr/bin/python3
# Write a function to print first x terms of the series 3N + 2 which are not multiples of 4.
# The function takes a variable x.
# The output of the series should be separated by spaces.

def print_terms(x: int) -> None:
    out_arr = []
    n = 1
    while len(out_arr) < x:
        term = (n * 3 + 2)
        if term % 4 != 0:
            out_arr.append(str(term))
        n += 1

    print(" ".join(out_arr))

print_terms(int(input("Enter a number: ")))
