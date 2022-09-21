from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.r_score}    PONG     {self.l_score}", move=False, align=ALIGNMENT, font=FONT)

    def r_scored(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_scored(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
