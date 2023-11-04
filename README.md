# New York Times Wordle Solver

A Python program to automate solving The New York Times Wordle game.

## How It Works
- Uses Selenium to open the Wordle game page.
- Interacts with the game to guess words.
- Analyzes feedback ("c" for correct, "p" for misplaced, "n" for incorrect) to narrow down possibilities.
- Continues guessing words until the correct one is found.

## Solver Algorithm (solver.py)
- Utilizes a 5-letter word dictionary to refine guesses based on feedback.
- Selects the next word to minimize incorrect attempts.

## Dependencies 
- Requires Selenium and PyAutoGUI for automation.
- MIGHT BE OUTDATED

