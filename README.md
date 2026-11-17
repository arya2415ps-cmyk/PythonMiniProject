# Rock Paper Scissors — Python Mini Project

## Project details
- **Project:** Rock Paper Scissors (Project #59)
- **Language:** Python 3
- **Type:** Console-based game
- **Reference:** *The Big Book of Small Python Projects* by Al Sweigart

## Description
This program lets one player play Rock Paper Scissors against the computer. The player enters `R`, `P`, or `S`. The computer chooses one of the three moves randomly. The program compares both choices, displays the result, and updates the win, loss, or tie counters. The game continues until the player enters `Q`.

## Rules
- Rock beats Scissors.
- Paper beats Rock.
- Scissors beat Paper.
- Matching choices result in a tie.

## Concepts used
- Variables and assignment
- `while` loops
- `if`, `elif`, and `else` conditional statements
- User input and output
- String method `.upper()`
- `random` module and `random.randint()`
- `time` module and `time.sleep()`
- `sys.exit()` to quit the game

## Requirements
- Python 3.8 or later
- No third-party packages are needed.

## How to run

### Windows
1. Install Python 3 if it is not already installed.
2. Open Command Prompt or PowerShell in this folder.
3. Run:

   ```bash
   python rock_paper_scissors.py
   ```

   If `python` is not recognized, try:

   ```bash
   py rock_paper_scissors.py
   ```

### VS Code
1. Open this folder in VS Code.
2. Open `rock_paper_scissors.py`.
3. Open the integrated terminal.
4. Run `python rock_paper_scissors.py`.

## How to play
- Enter `R` for Rock.
- Enter `P` for Paper.
- Enter `S` for Scissors.
- Enter `Q` to quit.
- The current score is shown before each round.

The program accepts lowercase or uppercase input. Invalid entries are rejected and the program asks again.

## Program flow
1. Import the required built-in modules.
2. Initialize wins, losses, and ties to zero.
3. Ask the player for a valid move.
4. Convert the move to its full name.
5. Display a short countdown.
6. Generate the computer's move randomly.
7. Compare the two moves and decide the result.
8. Update the appropriate score.
9. Repeat until the player quits.

## Sample interaction

```text
Rock, Paper, Scissors, by Al Sweigart
- Rock beats scissors.
- Paper beats rock.
- Scissors beat paper.

0 Wins, 0 Losses, 0 Ties
Enter your move: (R)ock (P)aper (S)cissors or (Q)uit
> R
ROCK versus...
1...
2...
3...
SCISSORS
You win!
```

*The computer's choice is random, so actual output will vary.*

## Files
- `rock_paper_scissors.py` — complete source code
- `README.md` — project description and run instructions

## Possible improvements
- Add Lizard and Spock moves.
- Add a point-based target score or best-of series.
- Save scores to a file.
- Create a graphical user interface.

## Credits
The project is based on Project #59, “Rock Paper Scissors,” from *The Big Book of Small Python Projects* by Al Sweigart. This repository contains a runnable implementation for learning and practice.
