import random
from turtle import Turtle,Screen


def main():
    screen = Screen()
    colors = ["red", "blue", "green", "yellow","black","orange"]
    turt = []

    # Setup the screen to 500 x 400
    screen.setup(width=500,height=400)

    # declare x, y position
    y_pos = 180
    x_pos = -250

    # Pop a screen to ask user to guess the winner
    chosen = screen.textinput(title="Make your guess!", prompt="Which turtle will win the race? Enter a color : ")

    # Boolean Variable to check if turtle reach ending point
    end_point = False

    for i in range(6):
        turt.append(Turtle("turtle"))
        turt[i].turtlesize(2)
        turt[i].penup()
        turt[i].goto(x_pos,y_pos)
        turt[i].color(colors[i])
        y_pos -=70

    while not end_point:
        selected_turtle = random.randint(0,5)
        turt[selected_turtle].forward(10)

        if int(turt[selected_turtle].xcor()) == 250:
            print(f"{turt[selected_turtle].pencolor()} wins!!")
            end_point = True
        
            if colors[selected_turtle] == chosen:
                print("You guess correctly!!")
            else:
                print("Too bad... wrong turtle!!")
        

    screen.exitonclick()

if __name__ =="__main__":
    main()