from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        with open("data.txt", mode="r") as high_score_data:
            self.high_score = int(high_score_data.read())
            high_score_data.close()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", mode="r") as high_score_data:
            self.write(f"Score: {self.score} High Score: {high_score_data.read()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as high_score_data:
                high_score_data.write(f"{self.score}")

        self.score = 0
        self.update_scoreboard()

    def refresh(self):
        self.score += 1
        self.update_scoreboard()
