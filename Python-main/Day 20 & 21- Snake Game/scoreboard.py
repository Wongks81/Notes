from turtle import Turtle

ALIGN = "center"
FONT = ('Arial',24,'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,250)
        self.pencolor("white")
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score}",align=ALIGN,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER",align=ALIGN,font=FONT)

