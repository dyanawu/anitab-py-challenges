#!/usr/bin/python3

size = int(input("Enter a number: "))

for i in range(1, size + 1):
    if i % 2 == 0:
        print(("#" * i).rjust(size, " "))
        continue
    print((str(i) * i).rjust(size, " "))
