import random
import time
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []

    def set_car_in_start_position(self,car):
        car.setposition(random.choice(range(290, 1200)), random.choice(range(-260, 280)))

    def create_cars(self):
        for n in range(50):
            car = Car()
            print(f"making car {n}")
            self.set_car_in_start_position(car)
            self.cars.append(car)

