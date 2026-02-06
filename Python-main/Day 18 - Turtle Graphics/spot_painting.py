from turtle import Turtle,Screen
from random import randint

def main():
    turtle = Turtle()
    screen = Screen()
    screen.colormode(255)

    # Get the screensize and store it in the tupple
    (width,height) = screen.screensize()
    print(f"{width}{height}")

    # lift the pen so that it will not draw when moving to starting position
    turtle.penup()

    # hide the arrow
    turtle.hideturtle()

    # as 0,0 is in the middle, to get to the lower left we have to multiply by negative 1

    for h in range(int(height /2) * -1 , int(height/2), 50):
        for w in range(int(width/2) * -1, int(width/2), 50):
            turtle.setpos(w,h)
            turtle.dot(30,random_color())

    screen.exitonclick()

def random_color():
    return (randint(0,255),randint(0,255),randint(0,255))

if __name__ == "__main__":
    main()