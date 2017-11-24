#####################################################################
# Author: Megan Franklin
# Username: franklinm:
#
# Assignment: Project 0: Final Project
#
# Goals: This assignment is built upon using old code from past assignments and making them better by updating them
#        with better code designs from what we've learned the whole semester.
# Old Code Being Used: A5: The Game of Nim, and T1: Create your own Adventure
# This is where I will build my Villain Class
#
# Help From:
######################################################################
from random import randrange


class Villain:
    def __init__(self, pt, wp, sz, cl):
        # self.name = ""  # I may not need this
        self.position = []
        self.weapon = []
        self.size = []

    # I need to create a function that has all of the lists below and will get called when a new villain needs to be created
br = ["Physician", "Nurse", "Orderly", "Mortician", "Therapist"]
wp = ["telekinesis", "an axe", "strength", "a sword", "a scythe", "chains"]
sz = ["small", "big", "tall", "giant", "towering", "large", "tiny"]


villain_1 = randrange(0, len(br), randrange(0, len(wp)))
villain_2 = randrange(0, len(wp), randrange(0, len(br)))
print("Villain 1 is a", br[villain_1], "and welds", wp[villain_1], "as their weapon")
print("Villain 2 welds", wp[villain_2], "as their weapon and is a", br[villain_2])
