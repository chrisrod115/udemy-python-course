from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

WALL = (-280, 280)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



snake = Snake()
scoreboard = Scoreboard()
food = Food()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    x_pos = snake.snake_head.xcor()
    y_pos = snake.snake_head.ycor()
    if x_pos < WALL[0] or x_pos > WALL[1] or y_pos < WALL[0] or y_pos > WALL[1]:
        scoreboard.reset()   
        snake.reset()
        
        
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()