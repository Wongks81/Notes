from audioop import add
from turtle import Turtle

# Can only declare constants here
MOVE_DISTANCE = 20
PLACEMENT_DISTANCE = 20
(UP,DOWN,LEFT,RIGHT) = (90,270,180,0)


class Snake:
    ''' Class to create a piece of Snake '''

    def __init__(self):
        self.snake_seg = []
        self.create_snake()
        self.snake_head = self.snake_seg[0]

    def create_snake(self):
        # init the first 3 squares for the snake
        for i in range(3):
            if i == 0:
                position = (0,0)
            else:
                position = self.snake_seg[-1].position()

            self.add_segment(position=position)
        

    def add_segment(self,position):
        ''' Add a segment to the current snake'''

        snake = Turtle("square")

        # init the object properties
        snake.penup()
        snake.color("white")

        snake.goto(position)
        self.snake_seg.append(snake)

    def extend_snake(self):
        self.add_segment(self.snake_seg[-1].position())

    def move(self):
        for s in range(len(self.snake_seg) - 1 ,0,-1):
            # This for loop is to move the snake according to the pos of the front snake piece
            # Meaning snake[2] will move to the position of snake[1] ...etc..

            # Getting the x and y coordinates of the previous snake piece and pass it to the current snake piece
            self.x_pos = self.snake_seg[s-1].xcor()
            self.y_pos = self.snake_seg[s-1].ycor()
            self.snake_seg[s].goto(self.x_pos,self.y_pos)

        self.snake_head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
    def left(self):
         if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
         if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)