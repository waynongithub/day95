from turtle import Turtle


class Score(Turtle):
    def __init__(self, level, ufos_destroyed):
        super().__init__()
        self.hideturtle()
        self.total_ufos_destroyed_count = 0
        self.ufo_destroyed_in_current_level = 0
        self.lives_left = 5
        self.level = 1
        self.penup()
        self.color('orange')
        self.goto(-200, 260)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"LEVEL: {self.level}    SCORE: {self.total_ufos_destroyed_count}    LIVES LEFT: {self.lives_left}",
                   font=('Courier', 15, 'normal'))

    # def total_ufos_destroyed(self):
    #     # print(f"score: in ufo_destroyed, count={self.destroyed_ufos_count}")
    #     self.total_ufos_destroyed_count += 1
    #     self.update_score_board()
    #
    # def ufos_destroyed_in_current_level(self):
    #     # print(f"score: in ufo_destroyed, count={self.destroyed_ufos_count}")
    #     self.ufo_destroyed_in_current_level += 1
    #     self.update_score_board()

    def ufo_destroyed(self):
        self.total_ufos_destroyed_count += 1
        self.ufo_destroyed_in_current_level += 1
        self.update_score_board()

    def player_dead(self):
        self.lives_left -= 1
        self.update_score_board()

    def next_level(self):
        self.level += 1
        self.update_score_board()
        self.ufo_destroyed_in_current_level = 0

    def new_bullet(self):
        self.lives_left -= 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, -100)
        self.color('yellow')
        self.write(f"GAME OVER", align='center', font=('Courier', 45, 'bold'))