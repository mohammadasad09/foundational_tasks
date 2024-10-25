from turtle import Turtle
from high_score_manager import HighScoreManager


score_manager = HighScoreManager('Snake Game/high_score.txt')
maximum_score = score_manager.get_max_score()


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.high_score = score_manager.get_max_score()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.counter} High Score: {self.high_score}", move= False, align = "center", font=('Courier', 24, 'normal'))
    
    def increase_score(self):    
        self.counter += 1
        self.update_scoreboard()
