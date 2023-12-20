from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

            
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)
        
    
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)        
    
    
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)        
    
    
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)        
    
    
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
            
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
        
    def extend(self):
        self.add_segment(self.segments[-1].position())