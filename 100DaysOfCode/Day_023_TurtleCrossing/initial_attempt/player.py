from turtle import Turtle

SHAPE = "turtle"
NORTH = 90
INITIAL_STARTING_POSITION = (0, -270)
MOVEMENT_SPEED = 20

class Player(Turtle):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.shape(SHAPE)
        self.setheading(NORTH)
        self.penup()
        self.goto(INITIAL_STARTING_POSITION)
        
    def go_up(self):
        self.forward(MOVEMENT_SPEED)
        
        
        