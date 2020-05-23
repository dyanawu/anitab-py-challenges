#!/usr/bin/python3
def contains_only_valid(digits: list) -> bool:
    valid_digits = {3, 5, 7}
    digits = set(digits)
    if digits - valid_digits == set():
        return True
    return False


entered = input("Enter a whole number: ")
if len(entered) %2 != 0:
    print(False)
else:
    digits = [int(i) for i in entered]
    print(contains_only_valid(digits))
