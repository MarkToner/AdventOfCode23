digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
file = open("puzzle_input.txt", "r")

lines = file.readlines()
 
total = 0

for line in lines:
    print(line)
    string = ''
    for letter in line:
        string += letter
        for digit in digits:
            if digit in string:
                string = string.replace(digit, str(digits.index(digit)+1))

    line = string
    print(line)
    current_digits = []
    for char in line:
        if char.isdigit():
            current_digits.append(int(char))
    if len(current_digits) > 0:
        total += 10 * current_digits[0]
        total += current_digits[-1]
        
print(total)
file.close()