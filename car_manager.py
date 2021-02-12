"""
 Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
"""
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """This class create multiple car """

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=3)
        self.setheading(180)
        self.goto(x=280, y=50)
        self.color(random.choice(COLORS))

    # TODO: create multiple cars on random position
    def move_car(self):
        """Move towards left direction"""
        self.forward(MOVE_INCREMENT)
