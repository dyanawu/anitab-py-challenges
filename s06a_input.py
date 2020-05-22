def validate_input(n):
    try:
        n = int(n)
    except ValueError:
        return False

    if 0 <= n <= 10000:
        return True


def get_digits(n):
    n = int(n)
    digits = []
    while n != 0:
        (n, r) = divmod(n, 10)
        digits.insert(0, r)
    return digits


def main():
    entered = ""
    while not validate_input(entered):
        entered = input("Enter a number between 0 and 10000 inclusive: ")
        if validate_input(entered):
            digits = get_digits(entered)
            for x in digits:
                print(x)
            break
        print(f"{entered} is not valid input.")


if __name__ == "__main__":
    main()
