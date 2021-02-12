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
        self.goto(STARTING_POSITION)

    def move_player(self):
        """This function help turtle to move_forward"""
        self.forward(MOVE_DISTANCE)

    def reset_player_position(self):
        """This will reset a position when player reach a finish line"""
        self.goto(STARTING_POSITION)
