lines = open("input.txt").readlines()

position = 50
password = 0
import time

for line in lines:
    direction = (-1 if line[0] == "L" else 1)
    difference = int(line[1:])
    for _ in range(difference):
        position += direction
        position = position % 100
        if position == 0:
            password += 1

print(password)