import turtle


class WriteState(turtle.Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        # self.goto(1000, 1000)
        # self.hideturtle()
        self.shape("circle")
        self.shapesize(0.1, 0.1)
        self.name()

    def write_answer_on_map(self, x, y, state):
        self.goto(x, y)
        self.write(state, align="center", font=("Arial", 10, "bold"))

    def game_completed(self):
        self.goto(0, 0)
        self.write("Game Completed!", align="center", font=("Arial", 16, "bold"))
        self.goto(0, -30)
        self.write("All State names guessed, Congratulations!", align="center",font=("Arial", 16, "bold"))

    def name(self):
        self.hideturtle()
        self.goto(240, -270)
        self.write("Created by Pranjal Sarnaik", align="center", font=("Arial", 10, "bold"))
