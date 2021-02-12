"""Player is a turtle that want to cross a road ."""
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Inherit from turtle class
class Player(Turtle):
    """This class handle all functionality of player"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)

    def move_player(self):
        """This function help turtle to move_forward"""
        self.forward(10)
