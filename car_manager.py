from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE
        # self.x = -300
        #
        # for y in range(-250, 300):
        #     self.make_car(y)
        #     y += MOVE_INCREMENT

        # i = random.randint(1, 2)
        #
        # for shape in range(i):
        #     x = random.randint(-300, 300)
        #
        #     car = Turtle()
        #     car.penup()
        #     car.color(random.choice(COLORS))
        #     car.shape('square')
        #     car.shapesize(stretch_wid=5, stretch_len=2)
        #     car.goto(x, y)

    def make_car(self):
        random_chance = random.randint(1, 5)

        if random_chance == 1:
            car= Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
