from turtle import Screen, Turtle
from random import randint,random


def main():
    turtle = Turtle()
    screen = Screen()
    screen.colormode(255)

    turtle.speed("fastest")

    for angle in range(0,360,5):
        turtle.pencolor(get_random_color())
        turtle.setheading(angle)
        turtle.circle(100)

    screen.exitonclick()

def get_random_color():
    return (randint(0,255),randint(0,255),randint(0,255))

if __name__ == "__main__":
    main()