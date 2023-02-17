from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.update_level()
        
        
    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    
    def level_up(self):
        self.level += 1
        self.update_level()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)