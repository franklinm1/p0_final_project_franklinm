#####################################################################
# Author: Megan Franklin
# Username: franklinm:
#
# Assignment: Project 0: Final Project
#
# Goals: This assignment is built upon using old code from past assignments and making them better by updating them
#        with better code designs from what we've learned the whole semester.
# Old Code Being Used: A5: The Game of Nim, and T1: Create your own Adventure
#
# Help From:
######################################################################
import time
import random
import turtle

user = input("Please enter your name: ")
def instructions():
    print("Hello There,", user, "and welcome to my game!")   # the "!" isn't where I want it to be
    time.sleep(3)
    print("Welcome to my adventure game: The Haunted House.")
    print("The rules and objectives are simple:")
    time.sleep(3)
    print()
    print("Your goal is to get through my haunted house which is five levels tall with 20 points or more.")
    print("Since I'm nice, you get 10 points off the bat")
    time.sleep(6)
    print()
    print("The points system is simple: on each floor you will encounter a villain.")   # everything below explains the point system
    print("You can do one of three things.")
    time.sleep(6)
    print()                                         # these are the three options you have on each floor
    print("You can either RUN, HIDE, or FIGHT")     # this is the only choice where you have no chance to gain points
    print("If you RUN you lose 2 points no matter what. But hey, you make it to the next level")
    time.sleep(5)
    print()
    print("If you HIDE you get to roll your fate")  # you have a 50/50 chance to gain points
    print("If you roll a 7 or more the villain doesn't see you and you receive 3 points")
    time.sleep(5)
    print("BUT if you roll a 6 or less the villain finds you, you lose 2 points, and you make it out by the skin of your teeth")
    time.sleep(5)
    print()
    print("The last option is to FIGHT")
    print("On this one the stakes are a little higher")
    time.sleep(4)
    print("If you roll a 8 or more you defeat the villain and gain 5 points")
    print("If you roll a 7 or less you are hurt by the villain but somehow manage to make it to the next level")
    time.sleep(6)
    print()
    print("By the time you make it to the final level, you should have 20 points or more")
    print("If you do, Congrats, you beat my game.")
    time.sleep(5)
    print("HOWEVER, if you lose... you are now one of my new villains.")
    print()
    print("Simple right... GREAT, LET'S PLAY")
    time.sleep(4)


def main():
    instructions()


main()
