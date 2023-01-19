from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.seth(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.backward(MOVE_DISTANCE)

    def go_right(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)
        self.left(90)

    def go_left(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)
        self.right(90)

    def at_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def go_start(self):
        self.goto(STARTING_POSITION)
