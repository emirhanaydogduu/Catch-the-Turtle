import random
import turtle
import time

background = turtle.Screen()
background.bgcolor("light blue")
background.title("Catch the Turtle")


def increase_score(x, y):
    global score
    score += 1
    turtle.write(f'Score: {score}', align="center", font=("Calibri", 24, "bold"))


def start_game():
    global time_counter
    while time_counter > 0:
        turtle.clear()
        turtle.write(f'Time: {time_counter}', font=("Calibri", 24, "bold"))
        time.sleep(0.5)
        time_counter -= 1

    turtle.clear()
    turtle.write('Game Over!', font=("Calibri", 24, "bold"))


score = 0
turtle.speed(4)
turtle.penup()
turtle.shape("turtle")
turtle.color("green")
turtle.shapesize(stretch_wid=1.5, stretch_len=1.5)
turtle.penup()
turtle.onclick(increase_score)

distance = 0
for i in range(1292948248):
    if (-300 < turtle.xcor() < 300) and (-300 < turtle.ycor() < 300):
        turtle.right(random.randint(0, 360))
        distance = random.randint(100, 300)
        turtle.forward(distance)
    else:
        turtle.right(180)
        turtle.forward(distance)

start_game()
