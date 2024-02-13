from turtle import Turtle
from random import randint


class Bullet(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.color('yellow')
        self.shape('circle')
        # self.turtlesize=1
        self.shapesize(0.5, 0.5)
        self.penup()
        self.goto(x_cor, -200)
        self.speed('slowest')
        self.showturtle()
        # self.x_move = 5
        self.y_move = 20
        # self.xbounced = 0
        # self.ybounced = 0

    def reset_position(self):
        self.goto(0, 0)

    # def bounce_x(self):
    #     self.x_move *= -1

    # def bounce_y(self):
    #     print(f"bounced Y")
    #     self.y_move *= -1

    def move(self):
        # if self.xcor() > 380 or self.xcor() < -380:
        #     self.bounce_x()
        # if self.ycor() > 280 or self.ycor() < -280:
        #     self.bounce_y()
        newx = self.xcor()
        newy = self.ycor() + self.y_move
        self.goto(newx, newy)
        # print(f"move {newx}, {newy}")
        # return True
        if self.ycor() < -400:
            self.reset()



