from turtle import Screen, Turtle, down

tim = Turtle()
screen= Screen()

# tells the screen to start listening to events
screen.listen()

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)
    
def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def clear_screen():
    # reset() might be better(?)
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# When user press 'space' on the keyboard, it will execute move_forward function.
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="c",fun=clear_screen)


screen.exitonclick()