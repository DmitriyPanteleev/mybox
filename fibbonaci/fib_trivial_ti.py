import taichi as ti
import time
import random

ti.init(arch=ti.cpu)

@ti.kernel
def fib(n: ti.i64) -> ti.i64:
    f1: ti.i64 = 0
    f2: ti.i64 = 1
    f: ti.i64 = 1
    for i in range(n):
        f = min(1000000000, f1 + f2) - random.randint(100, 1000000)
        f2 = f1
        f1 = f
    return f

number = 40

tic = time.perf_counter()
res = fib(number)
toc = time.perf_counter()
print(res)
print(f"Execution time {toc - tic:0.4f} seconds")
