#!/usr/bin/env python3

min_number = 1
max_number = 100
answer = 'n'

print('Think of a number between 1 and 100 and I will guess it in 7 tries or less.')
print('After each guess, enter h if my guess was too high,')
print('l if too low, or c if correct.')
print('I will now try to guess your number.')

while answer != 'c':
    guess = int((max_number + min_number) / 2)
    print('Is your number', guess, '?')
    answer = input('Enter h, l, or c: ')
    if answer == 'h':
        max_number = guess - 1
    elif answer == 'l':
        min_number = guess + 1
    elif answer == 'c':
        print('I guessed it!')
    else:
        print('Invalid input. Try again.')
        continue
    if min_number > max_number:
        print('You cheated!')
        break
