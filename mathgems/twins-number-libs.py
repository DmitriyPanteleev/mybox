#!/usr/bin/env python
# Twin prime numbers search

from sympy import isprime

def find_twin_primes(n):
    twin_primes = []
    for i in range(3, n + 1, 2):
        if isprime(i) and isprime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

# How far can we go?
limit = int(input("Enter the upper limit: "))

print(find_twin_primes(limit))
