from turtle import Turtle,Screen
from random import random

def main():
    timmy_turtle = Turtle()

    #draw_multishapes(timmy_turtle)
    for sides in range(3,11):
        lecturer_solution(timmy_turtle,sides)
    screen = Screen()
    screen.exitonclick()


def lecturer_solution(turtle, num_sides):
    angle = 360 / num_sides
    turtle.pencolor(random(),random(),random())
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

def draw_multishapes(turtle):
    draw_triangle(turtle)
    turtle.pencolor("blue")
    draw_square(turtle)
    turtle.pencolor("green")
    draw_pentagon(turtle)
    turtle.pencolor("brown")
    draw_hexagon(turtle)
    turtle.pencolor("black")
    draw_octagon(turtle)
    turtle.pencolor("cyan")
    draw_nonagon(turtle)
    turtle.pencolor("orange")
    draw_decagon(turtle)

def draw_decagon(turtle):
    for _ in range(10):
        turtle.rt(36)
        turtle.forward(100)

def draw_nonagon(turtle):
    for _ in range(9):
        turtle.rt(40)
        turtle.forward(100)

def draw_octagon(turtle):
    for _ in range(8):
        turtle.rt(45)
        turtle.forward(100)

def draw_hexagon(turtle):
    for _ in range(6):
        turtle.rt(60)
        turtle.forward(100)

def draw_pentagon(turtle):
    turtle.forward(100)
    for _ in range(5):
        # 72 degress 
        # 108 is the actual angle between 2 points
        # so outer angle is 180 - 108 = 72 degress
        turtle.rt(72)
        turtle.forward(100)

def draw_triangle(turtle):
    turtle.forward(100)
    turtle.left(-120)
    turtle.forward(100)
    turtle.left(-120)
    turtle.forward(100)
    turtle.left(-120)

def draw_dash(turtle):
    for _ in range(50):
        turtle.forward(5)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

def draw_square(turtle):
    turtle.forward(100)
    turtle.rt(90)
    turtle.forward(100)
    turtle.rt(90)
    turtle.forward(100)
    turtle.rt(90)
    turtle.forward(100)
    turtle.rt(90)



if __name__ == "__main__":
    main()