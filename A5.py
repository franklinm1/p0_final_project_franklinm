##############################
# Author: Megan Franklin
# Username: franklinm

# Assignment: A5: The Game of Nim
# Objectives: Practice breaking a larger problem down into smaller "mental chunks" using functions
#             Gain practice using loops and modulus (%)

# TA's that helped me: Will Romano and Aaron Christson
##############################
import time

import random

def game_instructions():
    """This will explain what the game is and the objective the player needs to accomplish."""
    print("Hello player! Would you like to play a game with me?")
    time.sleep(1)
    print("Great! This is The Nim Number Game")
    print("The game is simple. In this game you play against a computer. Me! ")
    time.sleep(1)
    print("I have a certain amount of monkeys in a barrel and it's your objective to be the last one to pull monkeys out of the barrel.")
    time.sleep(1)
    print("The player without a monkey to pull out is the loser.")
    time.sleep(1)
    print("Let's get started!")


def number_of_monkeys():
    """This will collect the input from the player of the total number of monkeys that will be used"""
    monkeys_in_barrel = int(input("How many monkeys do you wish to have total? "))
    while monkeys_in_barrel < 15:
        monkeys_in_barrel = int(input("Try again "))
    return monkeys_in_barrel


def player_turn(monkeys_in_barrel):
    """This will collect the players first move (the first set of monkeys to grab)."""
    time.sleep(1)
    print("There are " + str(monkeys_in_barrel) + " monkeys left.")
    time.sleep(1)
    print("Its your turn to go. You get to pull out either 1, 2, 3, or 4 monkeys per turn")
    turn_player = int(input("How many do you wish to pull out?: "))
    while 0 < turn_player < 5:
        return turn_player                         # this will return the players number of monkeys they want to pull out


def computer_turn(monkeys_in_barrel):
    """This is have the computer input a number of monkeys to be pulled from the barrel."""
    print("Now it's the computers turn")
    computer_choice = monkeys_in_barrel % 5        # this uses modulus to get the best possible number of monkeys the computer should pull out
    if computer_choice == 0:                       # if the remainder from modulus is 0 the computer will choice a random number from 1 to 4
        computer_choice = random.randint(1, 4)
    print(computer_choice)
    monkeys_in_barrel -= computer_choice
    return monkeys_in_barrel                       # this wil return/print the current number of monkeys


def main():
    game_instructions()
    monkeys_in_barrel = number_of_monkeys()        # this monkeys_in_barrel is different from the def number_of_monkeys variable.
    player_choice = player_turn(monkeys_in_barrel)   # this gives a value to number of monkeys the human player pulls out
    total_left = monkeys_in_barrel-player_choice   # this gives value to the remaining number of monkeys each time the players pulls a set number out
    computer_choice = computer_turn(total_left)    # this gives value to the number of monkeys the computer pulls out
    monkeys_in_barrel = computer_choice
    while monkeys_in_barrel > 0:
        turn_player = player_turn(computer_choice)
        print(turn_player)                         # this prints the number of the players first turn
        monkeys_in_barrel -= turn_player           # this will subtract the players amount of monkeys pulled out each human player turn
        print(monkeys_in_barrel)
        if monkeys_in_barrel <= 0:                 # if it's the players turn and the total number of monkeys left is 0 they win
            print("You win!")
            break
        computer_choice = computer_turn(monkeys_in_barrel)
        print(computer_choice)
        monkeys_in_barrel = computer_choice
        if monkeys_in_barrel <= 0:                 # if it's the computers turn and the total number of monkeys is 0 the computer wins
            print("The computer wins!")
            break
main()
