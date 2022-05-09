from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-290,270)
        self.hideturtle()
        self.display_level()



    def game_over(self):
        board = Turtle()
        board.goto(-50,0)
        board.write("Game Over!!!", font=FONT)
        board.hideturtle()


    def display_level(self):
        self.write(f"Level: {self.level}", font=FONT)
        

    def increase_level(self):
        self.clear()
        self.level += 1
        