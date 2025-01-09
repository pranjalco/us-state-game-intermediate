# Project 18: U.S. States Game

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 23 Dec 2024
- **Last Modified**: 9 Jan 2025

## Description:
The U.S. States Game is an interactive game where players guess the names of all 50 U.S. states. If a correct state name is entered in the dialog box, it is written on the U.S. map. Incorrect guesses do nothing. The game uses "blank_states_img.gif" as the U.S. map, which is located within the project folder. The dialog box displays the number of states guessed and those remaining. 

If the user types "Exit" in the box, the game stops. If any states remain unguessed, they are saved to a CSV file named `missing_states_to_guess.csv` in the `RemainingStates` folder. Once all states are guessed, the game congratulates the player.

The project uses two classes:
1. **StateInfoCalculation()**: This class reads data from "50_states.csv" and creates a `final_data_list`, a list of lists in the format `[state, x, y]`, where `state` is the name and `x, y` are its coordinates on the map. This list is accessible in the program after creating an object of the class.

2. **WriteState()**: This class writes text on the screen as required. It is responsible for dynamically writing state names on the map and displaying messages.

## How to Use:
1. Run the `app.py` file to start the game.
2. Enter the names of U.S. states in the input dialog box.
3. Correct guesses are displayed on the map.
4. Type "Exit" in the dialog box to quit the game.
5. Upon exiting, unguessed states are saved to `RemainingStates/missing_states_to_guess.csv` for further review.

## Level
- **Level**: Intermediate
- **Skills**: Object-oriented programming (OOP), file handling, data manipulation with Pandas, graphical programming with Turtle
- **Domain**: Educational Games, Data Visualization

## Features
- Uses OOP with two classes: `StateInfoCalculation` and `WriteState`
- Reads and processes data from a CSV file
- Dynamically writes guessed state names on a graphical U.S. map
- Displays remaining states count in a dialog box
- Saves unguessed states to a CSV file for review
- Congratulates the user upon successful completion of the game
- Contains `experiments` folder for temp files or practice
- Contains `screenshots` folder for gameplay screenshots

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/us-state-game-intermediate.git
   ```
2. Navigate to the project directory:
   ```bash
   cd us-state-game-intermediate
   ```

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

---
**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*

