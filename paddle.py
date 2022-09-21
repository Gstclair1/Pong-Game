from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):

    def __init__(self, start):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setpos(start)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


