#!/usr/bin/env python
# Count the number of primes in range [1, n].

import time
from tokenize import Double
import taichi as ti
ti.init()

@ti.func
def fib(n):
    f1 = 0
    f2 = 1
    f = 1
    for i in range(n):
        f = f1 + f2
        f2 = f1
        f1 = f
    print(f)
    return f

@ti.kernel
def fibbonacci(n: int) -> ti.i64:
    p = fib(n)
    return p

number = int(input("Enter number: "))

tic = time.perf_counter()
print(fibbonacci(number))
toc = time.perf_counter()

print(f"Execution time {toc - tic:0.4f} seconds")
