file = open("puzzle_input.txt", "r")

lines = file.readlines()
 
total = 0

for line in lines:
    current_digits = []
    for char in line:
        if char.isdigit():
            current_digits.append(int(char))
    if len(current_digits) > 0:
        total += 10 * current_digits[0]
        total += current_digits[-1]

print(total)
file.close()