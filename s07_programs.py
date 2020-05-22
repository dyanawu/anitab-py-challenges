#!/usr/bin/python3

def c2f(deg):
    return int((deg * 9/5) + 32)

temp_c = int(input("Please enter a temperature in Celsius: "))
print(c2f(temp_c))
