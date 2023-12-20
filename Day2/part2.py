import re

file = open("puzzle_input.txt", "r")

lines = file.readlines()

# Stores the sum for the answer
answer = 0


# i stores the index of the current game
i = 1
# Stores whether the current config is possible
flag = 0

for line in lines:
    r_min = 0
    b_min = 0
    g_min = 0
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
                if 10* int(ball[0]) + int(ball[1]) > r_min:
                    r_min = 10* int(ball[0]) + int(ball[1]) 
            if ball [2] == "r":
                if int(ball[0]) > r_min:
                    r_min = int(ball[0])
            if ball[3] == "b": 
                if 10* int(ball[0]) + int(ball[1]) > b_min:
                    b_min = 10* int(ball[0]) + int(ball[1]) 
            if ball [2] == "b":
                if int(ball[0]) > b_min:
                    b_min = int(ball[0])
            if ball[3] == "g": 
                if 10* int(ball[0]) + int(ball[1]) > g_min:
                    g_min = 10* int(ball[0]) + int(ball[1]) 
            if ball [2] == "g":
                if int(ball[0]) > g_min:
                    g_min = int(ball[0])
    answer += g_min * r_min * b_min

print(answer)
file.close()