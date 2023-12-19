"""

# Main things to complete (overview):

1. We need to move the snake 
2. Make sure to add food to the field 
3. Create a boundary the size of the screen

# Subtasks (these are smaller tasks to complete): 

1. If the head hits the body it should end game
2. If you eat a piece of food it should add length to the snake
3. Add key-presses to set the direction of the snake
4. Check to see if you are near the snake food and decide when it adds it to the tail
5. Make the food dissapear 

# How to complete this while using OOP: 

1. create a snake class 
2. create a food class
3. combine both in main
"""


from turtle import Turtle, Screen
from food import Food
from snake import Snake

HEIGHT, WIDTH = 500, 400

def initialize_all():
    turtle = Turtle()
    screen = Screen()
    food = Food()
    snake = Snake()
    keys()
    screen_params(HEIGHT,WIDTH)
    pass


def screen_params(height, width):
    screen.setup(height,width)


def keys():
    screen.listen()
    screen.onkeypress(forward, "Right")
    screen.onkeypress(up, "Up")
    screen.onkeypress(back, "Left")
    screen.onkeypress(down, "Down")
    

def play_snake():
    initialize_all()
    make()
    playing = True
    while playing:
        if (hits_wall() or eats_self()) == True:
            playing = False
        elif eats_food() == True:
            add_body()
            continue
            


def main():
    play_snake()


if __name__ == "__main__":
    main()
    

screen.exitonclick()