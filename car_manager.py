"""
 Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
"""
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """This class create multiple car """

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        """Create a  Single car """
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car) # added a  single car into a list

    def move_car(self):
        """Move towards left direction"""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)