#!/usr/bin/env python

def func(arg,iter):
    if iter < 0 :
        return 1
    return func(arg,iter - 1) + arg

l = func(2,256)

print(l)
