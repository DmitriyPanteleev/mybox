#!/usr/bin/env python
# Twin prime numbers search

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(n):
    twin_primes = []
    for i in range(3, n + 1, 2):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

# How far can we go?
limit = int(input("Enter the upper limit: "))

# Test the function
print(find_twin_primes(limit))
