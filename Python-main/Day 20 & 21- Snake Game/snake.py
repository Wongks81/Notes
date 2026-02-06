from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Disable turtle animation 
screen.tracer(0)

snake = []
x_pos = 0
y_pos = 0
index = 0

for i in range(3):
    snake.append(Turtle("square"))
    snake[i].penup()
    snake[i].color("white")
    snake[i].goto(x_pos,y_pos)
    x_pos -= 20


gameover = False

while index < 20:
    screen.update()
    time.sleep(0.5)

    for s in range(len(snake) - 1 ,0,-1):
        # This for loop is to move the snake according to the pos of the front snake piece
        # Meaning snake[2] will move to the position of snake[1] ...etc..

        # Getting the x and y coordinates of the previous snake piece and pass it to the current snake piece
        x_pos = snake[s-1].xcor()
        y_pos = snake[s-1].ycor()
        snake[s].goto(x_pos,y_pos)
        
        
        
    snake[0].forward(20)
    index += 1
    











screen.exitonclick()