#!/usr/bin/env python
# Collatz's hypothesis

def collatz(n):
    i=0
    max = 0
    print(f"Collatz's hypothesis with {n}")
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        if n > max:
            max = n
        i += 1
        print(f"iterration {i} : {n}")
    
    print(f"Total iterration: {i}")
    print(f"Max of sequence: {max}")


num = int(input("Enter the number: "))

collatz(num)
