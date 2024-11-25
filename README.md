# Number Guessing Game

A simple Python number guessing game with adjustable difficulty (easy, medium, hard), score tracking, and a persistent high score. Players guess a number between 1 and 100 with a limited number of attempts, receive higher/lower hints, and try to beat their high score.

Project URL : https://roadmap.sh/projects/number-guessing-game

## How to Play

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   ```

2. **Run the game:**
   ```bash
   python NumberGuessing.py
   ```

3. **Choose difficulty:** Select Easy (10 chances), Medium (5 chances), or Hard (3 chances).

4. **Guess the number:** Enter your guess when prompted.

5. **Receive feedback:** The game will tell you if your guess is too high or too low.

6. **Win or lose:** Guess the correct number within the allowed attempts to win!  Your score will increase with each win.  If you run out of attempts, the game will show the time elapsed.

7. **Play again?:**  Choose to play another round or quit.  The high score is saved when you quit.

## Features

* **Three difficulty levels:** Easy, Medium, and Hard.
* **Clear instructions:** The game guides the player through the process.
* **Feedback after each guess:** Helps the player narrow down the correct number.
* **Random number generation:** Ensures a different challenge each time.
* **Score tracking:** Keeps track of the player's correct guesses across multiple rounds.
* **Time tracking:**  Shows how long it took to guess the number (for lost rounds).
* **Persistent high score:** Saves the highest score achieved between game sessions (using `hs.json`).

## Code Overview

The code is written in Python and uses the `random`, `json`, and `time` modules. The `NumberGuessing` class handles game logic:

* **`__init__`:** Initializes the game, prints welcome messages, sets the default difficulty, and initializes score.
* **`__switch_mode`:** Sets the chosen difficulty and adjusts the number of allowed attempts.
* **`play`:** Starts the game loop, gets player input, provides feedback, checks for win/loss conditions, manages score, and handles replay functionality.  It also saves the high score to `hs.json` on exit.

## File Structure
```
number_guessing_game.py   # Main Python script for the game
hs.json                 # Stores the high score (created automatically if it doesn't exist)
README.md                # This file
```



## Example Gameplay

```
Welcome to the Number Guessing Game!
...
Enter your guess: 50
Incorrect! The number is greater than 50.

Enter your guess: 75
Congratulations! You guessed the correct number in 2 attempts.
Total Score: 1
Guessed in : 5.23 sec

Do you want to play more? (Y/N) : y
...

```
