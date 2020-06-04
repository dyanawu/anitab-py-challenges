#!/usr/bin/python3
import time
import decimal

def for_loop():
    output = []
    for i in range (1, 11):
        output.append(i)
    return output

def list_comprehension():
    return [i for i in range (1, 11)]


decimal.getcontext().prec = 10

print("Running for loop")
start_for = time.time()
print(for_loop())
end_for = time.time()
print(f"Completed in: {decimal.getcontext().create_decimal(end_for - start_for)}s")

print("Running list comprehension")
start_list = time.time()
print(list_comprehension())
end_list = time.time()
print(f"Completed in: {decimal.getcontext().create_decimal(end_list - start_list)}s")
