from turtle import Turtle

class Ball(Turtle):
    # def __init__(self, paddle, block_list):
    def __init__(self):
        # super().__init__(shape='circle')
        # self.shape('circle')
        super().__init__()
        self.up()
        self.color('white')
        self.dx, self.dy = 5, 6
        # self.paddle = paddle
        # self.block_list = block_list

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

        # Border bounce
        if self.xcor() <= -380 or self.xcor() >= 380:
            self.dx *= -1
        if self.ycor() >= 280:
            self.dy *= -1
        if self.ycor() < -300:
            self.goto(0, 0)

        # # Paddle bounce
        # if (-240 <= self.ycor() <= -230) and (paddle.xcor() - 60 < self.xcor() < paddle.xcor() + 60) and self.dy < 0:
        #     self.dy *= -1
        #
        # # Block collision check
        # for i in block_list:
        #     if (i.ycor() - 20 <= self.ycor() <= i.ycor() + 20) and (
        #             i.xcor() - 60 < self.xcor() < i.xcor() + 60) and ball.dy > 0:
        #         i.goto(1000, 1000)
        #         ball.dy *= -1
        #         block_list.remove(i)