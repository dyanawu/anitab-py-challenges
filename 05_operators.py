#!/usr/bin/python3
from functools import reduce

marks = []
while len(marks) < 5:
    marks.append(int(input()))
average = reduce(lambda x, y: x + y, marks)/5

if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
else:
    print("F")
