#!/usr/bin/python3
def validate_input(s: str) -> bool:
    try:
        int(s)
    except ValueError:
        return False
    return True


def get_digits(s: str) -> list:
    return [int(i) for i in s]


def contains_only_valid(digits: list) -> bool:
    valid_digits = {3, 5, 7}
    digits = set(digits)
    if digits - valid_digits == set():
        return True
    return False


def main():
    entered = ""
    while not validate_input(entered):
        entered = input("Enter a whole number: ")
        if validate_input(entered):
            digits = get_digits(entered)
            print(contains_only_valid(digits) and len(digits) % 2 == 0)
            break
        print(f"{entered} is not a whole number.")


if __name__ == '__main__':
    main()
