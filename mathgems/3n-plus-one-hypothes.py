# This program is a simple implementation of the 3n+1 hypothesis

num = int(input("Enter the number of sequence members: "))
i = 1

while num > 0:
  k = 3 * i + 1
  if k % 2 == 0:
    print(f"{k} is bifurcation number for {i}")
    num -= 1
  else:
    print(f"{k} is pure 3n+1 number for {i}")
  i += 1
