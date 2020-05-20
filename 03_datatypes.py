#!/usr/bin/python3

def print_time():
    import time
    print(f"The date and time is now {time.ctime()}.")

def circle_maths():
    PI = 3.14159
    radius = int(input("Enter a radius: "))
    print(f"The area of a circle with radius {radius} units is {PI * radius * radius} units squared.")
    print(f"The circumferenceof a circle with radius {radius} units is {2 * PI * radius} units squared.")

def make_list():
    sequence = list(input("Enter a comma-separated series of numbers:\n").split(", "))
    print(f"A list: {sequence}")
    print(f"A tuple: {tuple(sequence)}")

def test_range():
    test_number = int(input("Enter a number to test range: "))
    if 900 <= test_number <= 1100 or 1900 <= test_number <= 2100:
        print(True)
    else:
        print(False)

def test_in_group():
    in_value = int(input("Enter a number to check value in group: "))
    group = [int(x) for x in input("Enter a list of numbers like before: ").split(", ")]
    if in_value in group:
        print(True)
    else:
        print(False)

def from_17():
    given_number = int(input("Enter a number: "))
    if given_number > 17:
        print((given_number - 17) * 2)
    else:
        print(abs(given_number - 17))

command = ""

while command != "q":
    command = input("""\n=======================================
Please select a function by letter:
a. display the current date and time
b. do some circle maths
c. generate a list and a tuple
d. test a number to be within 100 of 1000 or 2000
e. check if a value is in a group of values
f. do some maths with 17
q. Quit
""")

    dispatch = {
        "a": print_time,
        "b": circle_maths,
        "c": make_list,
        "d": test_range,
        "e": test_in_group,
        "f": from_17,
        "q": exit
    }

    dispatch[command]()
