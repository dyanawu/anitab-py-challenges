#!/usr/bin/python3

# given n, generate first n fibonacci numbers from 0
# then map + lambda, return squared list

# 6  [0, 1, 1, 4, 9, 25]
# 10 [0, 1, 1, 4, 9, 25, 64, 169, 441, 1156]
# 13 [0, 1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025, 7921, 20736]
# 4  [0, 1, 1, 4]
# 9  [0, 1, 1, 4, 9, 25, 64, 169, 441]

def gen_fibonacci(n: int) -> list:
    series = [0]

    previous = 0
    current = 1
    while len(series) < n:
        series.append(current)
        previous, current = current, current + previous

    return series

main_series = gen_fibonacci(int(input("Enter number of terms: ")))
print(list(map(lambda x: x ** 2, main_series)))
