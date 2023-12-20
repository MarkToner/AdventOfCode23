import re

file = open("puzzle_input.txt", "r")

lines = file.readlines()

# Stores the sum for the answer
possible = 0

r_Max = 12
b_Max = 14
g_Max = 13

# i stores the index of the current game
i = 1
# Stores whether the current config is possible
flag = 0

for line in lines:
    # Remove the Game X: 
    line = re.sub(r'^.*?: ', '', line)
    # Create an array for the rounds
    rounds = line.split(';')
    for round in rounds:
        # Create an array so we can deal with each colour separately
        balls = round.split(',')
        for ball in balls:
            if ball[0] == " ":
                ball = ball[1:]
            space = ball.index(" ")
            if ball[3] == "r" and ball[2] == " ":
                if 10* int(ball[0]) + int(ball[1]) > r_Max:
                    flag = 1
                    break
            if ball [2] == "r":
                if int(ball[0]) > r_Max:
                    flag = 1
                    break
            if ball[3] == "b": 
                if 10* int(ball[0]) + int(ball[1]) > b_Max:
                    flag = 1
                    break
            if ball [2] == "b":
                if int(ball[0]) > b_Max:
                    flag = 1
                    break
            if ball[3] == "g": 
                if 10* int(ball[0]) + int(ball[1]) > g_Max:
                    flag = 1
                    break
            if ball [2] == "g":
                if int(ball[0]) > g_Max:
                    flag = 1
                    break
    if flag == 0:
        possible += i
    i += 1
    flag = 0

print(possible)
file.close()