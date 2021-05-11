from turtle import Screen, Turtle
import random

def fractal(level, turtle, length, direction=90):
    for _ in range(3):
        turtle.forward(length)

        if level > 1:
            fractal(level- 1, turtle, length / 2, -direction)

        turtle.right(direction)

    turtle.forward(length)
    turtle.left(direction)

screen = Screen()

turtle = Turtle()
turtle.speed('fastest')  # because I have no patience

fractal(5, turtle, 75)

turtle.hideturtle()
screen.exitonclick()