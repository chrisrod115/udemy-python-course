### Pong Game ###

"""
Requirements: 
1. User Paddle Left
2. Independent Right Paddle
3. Moving pong ball
4. Divider Net
5. Bounce Zone top and bottom
6. Scoreboard
"""
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)    

l_paddle = Paddle((-280, 0))
r_paddle = Paddle((270, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()


screen.exitonclick()