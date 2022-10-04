#!/usr/bin/env python
# Trivial fibonnachi number.

import time

def fib(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f = f1 + f2
        f2 = f1
        f1 = f
    return f

number = int(input("Enter number: "))

tic = time.perf_counter()
print(fib(number))
toc = time.perf_counter()

print(f"Execution time {toc - tic:0.4f} seconds")
