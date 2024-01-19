#!/usr/bin/env python
"""
The fishermen fished all day long, and in the evening, after putting their catch on the shore, they went to bed.
However, one of them could not sleep and decided to leave, taking his part of the catch. After counting the catch,
the fisherman divided all the fish into three parts. At the same time, one fish turned out to be extra. The fisherman
threw it into the water, took his share and went home. In the middle of the night the second fisherman woke up and,
not noticing the absence of the first comrade, divided the remaining fish into three parts, one extra fish was also
thrown into the water, took his share and swam home. The third fisherman did the same thing in the morning, not noticing
that he was alone. The problem asked what was the smallest number of fish the fishermen could have.
"""

def check_valid_fish_number(fish_number):
    
    if fish_number % 3 == 1 :
        x = fish_number - (fish_number // 3) - 1
        xf = fish_number // 3
        if x % 3 == 1:
            y = x - (x // 3) - 1
            yf = x // 3
            if y % 3 == 1:
                zf = y // 3
                print(f"Fisherman 1: {xf}, Fisherman 2: {yf}, Fisherman 3: {zf}")
                return True
    
    return False

for fish_number in range(1, 1000):
    if check_valid_fish_number(fish_number):
        print(f"Minimal fish number {fish_number}")
        break
