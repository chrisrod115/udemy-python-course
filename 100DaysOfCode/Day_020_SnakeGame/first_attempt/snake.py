from turtle import Turtle
class Snake():
    def __init__(self) -> None:
        self.length = 0
        self.body_coordinates = []
        self.head = []
        self.initial_body_coordinates = [(0,0), (0, -20), (0, -40)]
        self.initialize_snake()
        
        
    def add_block(self, location):
        block = Turtle(shape="square")
        block.color("white")
        block.penup()
        block.goto(location)
        
    
    def initialize_snake(self):
        for i in range(2):
            self.add_block(self.initial_body_coordinates[i])
            
        
