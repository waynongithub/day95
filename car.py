import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        # self.move()

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        # time.sleep(0.01)

    def detect_collision(self,player_position):
        # if abs(turtle.ycor - car.ycor) < 20 AND abs(turtle.xcor  - car.xcor ) < 30
        if abs(player_position[1] - self.ycor()) < 20 and abs(player_position[0] - self.xcor()) < 30:
            return True
        return False


