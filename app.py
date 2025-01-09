import turtle
import pandas

from state_info_calculation import StateInfoCalculation
from write_state import WriteState
from functions import *

"""
# Project 18: U.S. States Game

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 23 Dec 2024
- **Last Modified**: 9 Jan 2025

## Description:
The U.S. States Game is an interactive game where players guess the names of all 50 U.S. states. If a correct 
state name is entered in the dialog box, it is written on the U.S. map. Incorrect guesses do nothing. The game 
uses "blank_states_img.gif" as the U.S. map, which is located within the project folder. The dialog box displays 
the number of states guessed and those remaining. 

If the user types "Exit" in the box, the game stops. If any states remain un-guessed, they are saved to a CSV file 
named `missing_states_to_guess.csv` in the `RemainingStates` folder. Once all states are guessed, the game congratulates 
the player.

The project uses two classes:
1. **StateInfoCalculation()**: This class reads data from "50_states.csv" and creates a `final_data_list`, a list of 
lists in the format `[state, x, y]`, where `state` is the name and `x, y` are its coordinates on the map. This list 
is accessible in the program after creating an object of the class.

2. **WriteState()**: This class writes text on the screen as required. It is responsible for dynamically writing state 
names on the map and displaying messages.

## How to Use:
1. Run the `app.py` file to start the game.
2. Enter the names of U.S. states in the input dialog box.
3. Correct guesses are displayed on the map.
4. Type "Exit" in the dialog box to quit the game.
5. Upon exiting, un-guessed states are saved to `RemainingStates/missing_states_to_guess.csv` for further review.

## Level
- **Level**: Intermediate
- **Skills**: Object-oriented programming (OOP), file handling, data manipulation with Pandas, graphical programming 
              with Turtle
- **Domain**: Educational Games, Data Visualization

## Features
- Uses OOP with two classes: `StateInfoCalculation` and `WriteState`
- Reads and processes data from a CSV file
- Dynamically writes guessed state names on a graphical U.S. map
- Displays remaining states count in a dialog box
- Saves un-guessed states to a CSV file for review
- Congratulates the user upon successful completion of the game
- Contains `experiments` folder for temp files or practice
- Contains `screenshots` folder for gameplay screenshots

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to 
     execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.
"""

screen = turtle.Screen()
screen.title("U.S. States Game by Pranjal Sarnaik")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_info_calculation = StateInfoCalculation()
write_state = WriteState()

guessed_states = []
total = 50
n = 0

name_l()
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{n}/{total} Guess the State", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    # Here by using write_name turtle object we will write name of state on map.
    write_name = turtle.Turtle()
    write_name.penup()
    write_name.shape("circle")
    write_name.shapesize(0.1, 0.1)

    for element in state_info_calculation.final_data_list:
        if answer_state not in guessed_states:
            if answer_state == element[0]:
                write_name.goto(element[1], element[2])
                write_name.write(element[0], align="center", font=("Arial", 10, "bold"))
                guessed_states.append(element[0])
                n += 1

                # Here we will stop game when all states guessed.
                if n == 50:
                    write_state.game_completed()
                    game_is_on = False

# Finding which states are remaining to be guessed and saving to .csv file
remaining_states = []
for state in state_info_calculation.final_data_list:
    if state[0] not in guessed_states:
        remaining_states.append(state[0])

# print(remaining_states)

remaining_states_data = pandas.DataFrame(remaining_states)
remaining_states_data.to_csv("./RemainingStates/missing_states_to_guess.csv")
