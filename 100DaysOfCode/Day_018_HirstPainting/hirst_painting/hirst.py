import random as rand
import colorgram as cg
from turtle import Turtle, Screen

STARTING_POSITION = (-350, -300)
ENDING_POSITION = (350, 300)


def extract_colors(image_path, num_colors):
    return cg.extract(image_path, num_colors)


def organize_colors(image_colors):
    return [(item.rgb.r, item.rgb.g, item.rgb.b) for item in image_colors]


def random_color(color_palette):
    return rand.choice(color_palette)


def create_turtle_dot(t, x_cor, y_cor, color):
    t.penup()
    t.goto(x_cor, y_cor)
    t.dot(20, color)


def main():
    screen = Screen()
    screen.colormode(255)
    t = Turtle()
    t.speed(0)
    t.hideturtle()

    image_path = '/Users/christopherrodriguez/Documents/GitHub/udemy-python-course/100DaysOfCode/Day_018_TurtleGraphics/hirst_painting/hirst.jpg'
    num_colors = 30

    raw_colors = extract_colors(image_path, num_colors)
    color_palette = organize_colors(raw_colors)

    for x_cor in range(STARTING_POSITION[0], ENDING_POSITION[0], 50):
        for y_cor in range(STARTING_POSITION[1], ENDING_POSITION[1], 50):
            rand_color = random_color(color_palette)
            create_turtle_dot(t, x_cor, y_cor, rand_color)

    screen.exitonclick()


if __name__ == "__main__":
    main()
