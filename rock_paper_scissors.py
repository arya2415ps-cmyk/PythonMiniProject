"""
ROCK, PAPER, SCISSORS
Mini Project based on Project #59 from
The Big Book of Small Python Projects by Al Sweigart.

Run: python rock_paper_scissors.py
"""

import random
import time
import sys


print("Rock, Paper, Scissors, by Al Sweigart")
print("- Rock beats scissors.")
print("- Paper beats rock.")
print("- Scissors beat paper.")

# These variables keep track of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # Main game loop

    while True:  # Keep asking until the player enters a valid move.
        print()
        print("{} Wins, {} Losses, {} Ties".format(wins, losses, ties))
        print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")

        playerMove = input("> ").upper()

        if playerMove == "Q":
            print("Thanks for playing!")
            sys.exit()

        if playerMove == "R" or playerMove == "P" or playerMove == "S":
            break
        else:
            print("Type one of R, P, S, or Q.")

    # Display the player's choice.
    if playerMove == "R":
        print("ROCK versus...")
        playerMove = "ROCK"
    elif playerMove == "P":
        print("PAPER versus...")
        playerMove = "PAPER"
    elif playerMove == "S":
        print("SCISSORS versus...")
        playerMove = "SCISSORS"

    # Count to three with dramatic pauses.
    time.sleep(0.5)
    print("1...")
    time.sleep(0.25)
    print("2...")
    time.sleep(0.25)
    print("3...")
    time.sleep(0.25)

    # Display what the computer chose.
    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = "ROCK"
    elif randomNumber == 2:
        computerMove = "PAPER"
    elif randomNumber == 3:
        computerMove = "SCISSORS"

    print(computerMove)
    time.sleep(0.5)

    # Display and record the win/loss/tie.
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1

    elif playerMove == "ROCK" and computerMove == "SCISSORS":
        print("You win!")
        wins = wins + 1

    elif playerMove == "PAPER" and computerMove == "ROCK":
        print("You win!")
        wins = wins + 1

    elif playerMove == "SCISSORS" and computerMove == "PAPER":
        print("You win!")
        wins = wins + 1

    elif playerMove == "ROCK" and computerMove == "PAPER":
        print("You lose!")
        losses = losses + 1

    elif playerMove == "PAPER" and computerMove == "SCISSORS":
        print("You lose!")
        losses = losses + 1

    elif playerMove == "SCISSORS" and computerMove == "ROCK":
        print("You lose!")
        losses = losses + 1
