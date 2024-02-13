from turtle import Turtle
from turtle import register_shape

class Line(Turtle):
    def __init__(self):
        super().__init__()
        # register_shape('images/rocket.gif')
        # self.shape('images/rocket.gif')
        self.shape('classic')
        self.width = 1
        self.shapesize(1, self.width)
        self.hideturtle()
        self.color('white')
        self.penup()
        self.baseline = -200
        self.goto(-400, self.baseline - 32)
        # self.left_edge = 0
        # self.right_edge = 0
        # self.step = 30
        # self.recalculate_edges()
        self.pendown()
        self.goto(400, self.baseline - 32)
        # self.showturtle()

    def move_left(self):
        if self.xcor() - self.step > -380 :
            newx = self.xcor() - self.step
        else:
            newx = -380
        self.goto(newx, self.baseline)
        # self.recalculate_edges()

    def move_right(self):
        if self.xcor() + self.step < 380:
            newx = self.xcor() + self.step
        else:
            newx = 380
        self.goto(newx, self.baseline)
        # self.recalculate_edges()

    def recalculate_edges(self):
        x, y = self.pos()
        self.left_edge = x - (20 * self.width)
        self.right_edge = x + (20 * self.width)
        # print(f"player: pos={x}, edges are {self.left_edge}, {self.right_edge}, y={y}")

