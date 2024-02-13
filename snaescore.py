from turtle import Turtle

YOUR_SCORE = "your score = "
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setposition(0, 270)
        self.hideturtle()
        self.color('yellow')
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(YOUR_SCORE + str(self.score), False, align='center', font=('Courier', 15, 'normal'))

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        # t = Turtle()
        self.penup()
        self.setposition(0,0)
        # t.hideturtle()
        self.color('pink')
        self.write("GAME OVER", False, align='center', font=('Courier', 20, 'normal'))

