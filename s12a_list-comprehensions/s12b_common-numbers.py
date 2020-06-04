#!/usr/bin/python3

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_b = [2, 3, 5, 7, 11, 13, 17]

def find_common(arr1: list, arr2: list) -> list:
    return [i for i in arr1 if i in arr2]

print("List A:", list_a)
print("List B:", list_b)
print("find_common:", find_common(list_a, list_b))
