from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Disable turtle animation 
screen.tracer(0)


index = 0

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

gameover = False

while not gameover:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend_snake()
        food.refresh()

    # Detect collision with wall
    if (
        snake.snake_head.xcor() > 280 
        or snake.snake_head.xcor() < -280 
        or snake.snake_head.ycor() > 280 
        or snake.snake_head.ycor() < -280
        ):
        gameover = True
        scoreboard.game_over()
    
    # Detect collision with body or tail
    # Slice the head out from the for loop
    for seg in snake.snake_seg[1:]:
        if snake.snake_head.distance(seg) < 15:
            gameover = True
            scoreboard.game_over()

    # Detection collision with tail
    


    







screen.exitonclick()