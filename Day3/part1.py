import re

file = open("puzzle_input.txt", "r")

grid = []
symbol_indices = []
number_indices = []
lines = file.readlines()

row_number = 0

for line in lines:
    line = line.replace("\n","")
    for char in line:
        print(char)
        print(char.isdigit())
        if not char.isdigit() and char != ".":
            symbol_indices.append([row_number, line.index(char)])
            row_number += 1
        elif char.isdigit():
            number_indices.append([row_number, line.index(char)])


print(symbol_indices)

file.close()