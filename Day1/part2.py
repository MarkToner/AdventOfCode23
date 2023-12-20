digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = ["o1e", "t2o", "t3e", "f4r", "f5e","s6x", "s7n", "e8t", "n9e",]
file = open("puzzle_input.txt", "r")

lines = file.readlines()
 
total = 0

for line in lines:
    print(line)
    for digit in digits:
        if digit in line:
                line = line.replace(digit, numbers[digits.index(digit)])

    print(line)
    current_digits = []
    for char in line:
        if char.isdigit():
            current_digits.append(int(char))
    if len(current_digits) > 0:
        total += 10 * current_digits[0]
        t1 = 10 * current_digits[0]
        total += current_digits[-1]
        t1 += current_digits[-1]
        print(t1)
        
print(total)
file.close()