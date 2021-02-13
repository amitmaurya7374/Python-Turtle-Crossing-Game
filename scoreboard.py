FONT = ("Courier", 19, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    """This class handle a score of a player"""

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(arg=f"Level {self.level}", font=FONT, )

    def update_level(self):
        """This function increase a level of player """
        self.level += 1
        self.clear()
        self.write(arg=f"Level {self.level}", font=FONT)

    def game_over(self):
        """Print a game over text on screen"""
        self.goto(0, 0)
        self.hideturtle()
        self.penup()
        self.write(arg="Game Over", font=FONT, align="Center")
