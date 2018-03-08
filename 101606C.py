values = {
    "red" : 1,
    "yellow" : 2,
    "green" : 3,
    "brown" : 4,
    "blue" : 5,
    "pink" : 6,
    "black" : 7
}

N = int(input())
score = 0
red_balls = 0
max_ball = 0
for i in range(N):
    sc = values[input()]
    if sc > max_ball:
        max_ball = sc
    score += sc
    if sc == 1:
        red_balls += 1

if score == N:
    score = 1
if max_ball > 1:
    score += red_balls * max_ball
print(score)
