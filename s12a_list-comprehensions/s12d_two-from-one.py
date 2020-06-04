#!/usr/bin/python3

print("Returning even and odd from one list comprehension:")
print([[i + j
       for i in range(0, 21, 2)]
       for j in range (0, 2)])
