#!/usr/bin/python3

list_ = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(f"Sample list of lists:\n{list_}")
print(f"Even numbers: {[i for sublist in list_ for i in sublist if i % 2 == 0]}")
print(f"Even numbers, unflattened: {[[i for i in sublist if i % 2 == 0] for sublist in list_]}")
