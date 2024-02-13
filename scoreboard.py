from turtle import Turtle

# FONT = ("Courier", 24, "normal")
YOUR_SCORE = "successful crossings : "
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        # self.setposition(0, 270)
        self.goto(0,270)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()
    #
    # def write_score(self):
    #     self.write("successful crossings:" + successfultr(self.score), align="center", font=("Courier", 24, "normal"))
    #     self.write( str(self.score), align="center", font=("Courier", 24, "normal"))

    def write_score(self):
        self.clear()
        self.write(YOUR_SCORE + str(self.score), False, align='center', font=('Courier', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER", False, align='center', font=('Courier', 45, 'normal'))