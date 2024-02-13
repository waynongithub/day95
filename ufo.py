from turtle import Turtle, register_shape
from random import randint, choice
import time

class UFO(Turtle):
    def __init__(self, position):
        super().__init__()
        colors = ['red', 'blue', 'yellow', 'purple', 'green', 'orange']
        register_shape('images/ufo3.gif')
        register_shape('images/ufo7-60.gif')
        register_shape('images/explode.gif')
        self.color(choice(colors))
        self.hideturtle()
        # self.shape('square')
        self.shape('images/ufo7-60.gif')
        self.speed('fastest')
        self.width = 2
        self.height = 1
        self.step = 1
        self.shapesize(self.height, self.width)
        self.penup()
        self.xcor, self.ycor = position
        self.goto(self.xcor, self.ycor)
        self.bottom_edge = self.ycor - self.height/2
        self.top_edge = self.ycor + self.height
        self.right_edge = self.xcor + (self.width/2 * self.width)
        self.left_edge = self.xcor - (self.width/2 * self.width)
        # print(f"xcor={self.xcor}, ycor={self.ycor}")
        self.direction = "right"
        self.showturtle()

    def move(self, switch, drop):
        if switch:
            if self.direction == "right":
                self.direction = "left"
            else:
                self.direction = "right"
            self.ycor = self.ycor - 1

        if drop:
            self.ycor = self.ycor - 10

        if self.direction == "right":
            self.xcor = self.xcor + self.step
        else:
            self.xcor = self.xcor - self.step

        self.goto(self.xcor, self.ycor)

    def got_hit(self):
        # self.shape('images/ufo7-60.gif')
        # time.sleep(0.2)
        self.xcor = 0
        self.ycor = 500
        self.goto(self.xcor, self.ycor)