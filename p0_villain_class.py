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
import random


class Villain:
    def __init__(self, ty, wp, sz):
        self.type = ty    # the type or in my games case "occupation"
        self.weapon = wp   # type of weapon that the villain can use
        self.size = sz    # the size the villain can be

    def create(self, ty, wp, sz):
        self.type = ["Physician", "Nurse", "Orderly", "Medical Examiner", "Therapist"]
        self.weapon = ["telekinesis", "a surgical saw", "chains", "mind control", "a scalpel"]
        self.size = ["small", "big", "tall", "towering", "large"]

        vil_1 = random.choice(ty)
        if vil_1 == "Physician":
            wp = ["a surgical saw", "a scalpel"]
            sz = ["big", "tall", "towering"]
        elif vil_1 == "Medical Examiner":
            wp = ["stryker saws"]
            sz = ["lofty", "towering", "giant"]
        elif vil_1 == "Nurse":
            wp = ["telekinesis", "chains"]
            sz = ["small"]
        elif vil_1 == "Orderly":
            wp = ["telekinesis", "chains"]
            sz = ["small"]
        elif vil_1 == "Therapist":
            wp = ["telekinesis", "mind control"]
            sz = ["large"]

vil_1 = Villain(ty, wp, sz)
vil_1.create(random.choice(ty), random.choice(wp), random.choice(sz))
print("Villain 1 is a", random.choice(sz), vil_1, "and welds", random.choice(wp), "as their weapon")


