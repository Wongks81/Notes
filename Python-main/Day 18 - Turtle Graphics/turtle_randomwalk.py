from turtle import Screen, Turtle
from random import randint,random,choice

def main():
    turt = Turtle()
    turt.pensize(10)
    turt.speed("fast")
    #random_walk(turt)
    #lecturer_solution(turt)

    screen = Screen()

    random_walk_color(turt, screen)

    screen.exitonclick()

def random_walk_color(turtle, screen):
    direction = [0,90,180,270]
    for _ in range(200):
        # using 0-255 as range for rgb, need to change the colormode to 255
        screen.colormode(255)
        turtle.pencolor(randint(0,255),randint(0,255),randint(0,255))
        turtle.setheading(choice(direction))
        turtle.forward(30)

def random_walk(turtle):

    for _ in range(50):
        direction = randint(1,4)
        turtle.pencolor((random(),random(),random()))

        if direction == 1:
            continue
        elif direction == 2:
            turtle.left(90)
        elif direction == 3:
            turtle.right(90)
        elif direction == 4:
            turtle.back(90)

        turtle.forward(30)

def lecturer_solution(turtle):
    direction = [0,90,180,270]
    for _ in range(200):
        # using float point from 0-1 as rgb (hue(?)), default colormode is 1.0 (?)
        turtle.pencolor(random(),random(),random())
        turtle.setheading(choice(direction))
        turtle.forward(30)

if __name__ == "__main__":
    main()