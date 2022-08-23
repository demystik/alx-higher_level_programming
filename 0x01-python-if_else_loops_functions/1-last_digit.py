#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number
if i < 0:
    i = -1 * i
    i = i % 10
    i = -1 * i
else:
    i = i % 10
if i == 0:
    print(f"Last digit of {number} is {i} and is 0")
elif i > 5:
    print(f"Last digit of {number} is {i} and is greater than 5")
elif i < 6 and i != 0:
    print(f"Last digit of {number} is {i} and is less than 6 and not 0")
