######################################################################
# Author: Megan Franklin
# Username: franklinm
#
# Assignment: Project 0: Final Project
#
# Goals: This assignment is built upon using old code from past assignments and making them better by updating them
#        with better code designs from what we've learned the whole semester.
# Old Code Being Used: A5: The Game of Nim, and T1: Create your own Adventure
#
# Help From: Scott Heggen
######################################################################
import time
import random

class Boss:
    def __init__(self, ty, wp, sz):
        self.type = ty    # the type or in my games case "occupation"
        self.weapon = wp   # type of weapon that the villain can use
        self.size = sz    # the size the villain can be

    def create(self, ty, wp, sz):
        self.type = ["Physician", "Nurse", "Orderly", "Medical Examiner", "Therapist"]
        self.weapon = ["telekinesis", "a surgical saw", "chains", "mind control", "a scalpel"]
        self.size = ["small", "big", "tall", "towering", "large"]

        self.weapon.deepcopy = wp
        self.size.deepcopy = sz

        boss = random.choice(ty)
        if boss == "Physician":
            wp = ["a surgical saw", "a scalpel"]
            sz = ["big", "tall", "towering"]
        elif boss == "Medical Examiner":
            wp = ["stryker saws"]
            sz = ["lofty", "towering", "giant"]
        elif boss == "Nurse":
            wp = ["telekinesis", "chains"]
            sz = ["small"]
        elif boss == "Orderly":
            wp = ["telekinesis", "chains"]
            sz = ["small"]
        elif boss == "Therapist":
            wp = ["telekinesis", "mind control"]
            sz = ["large"]

        boss = Boss(ty, wp, sz)
        boss.create(random.choice(ty), random.choice(wp), random.choice(sz))
        print("This BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")

def instructions(user):
    print("Hello There,", user, "and welcome to my game!")
    print("The Abandoned Hospital.")
    print("The rules and objectives are simple: Beat the BOSS and you win!")
    time.sleep(4)
    print()
    print("Your goal is to get through the hospital without dying.")
    time.sleep(3)
    print()
    print("The BOSS will be generated at the beginning of the game.")
    print("You can do one of two things.")
    time.sleep(5)
    print()                                         # these are the two options you have on each floor
    print("You can either REST or FIGHT")
    print()
    time.sleep(2)
    print("If you REST there will be a chance that the BOSS will damage you")
    time.sleep(2)
    print()
    print("If you roll a 5 or more you land a successful attack on the BOSS")
    print("If you roll a 6 or less you are damaged by the BOSS")
    time.sleep(5)
    print()
    print("The other option is to FIGHT")
    print("On this one the stakes are a little higher")
    print()
    time.sleep(4)
    print("If you roll a 6 or more you land a successful attack on the BOSS")
    print("If you roll a 5 or less you are damaged by the BOSS")
    time.sleep(5)
    print()
    print("The goal of the game is to beat the BOSS")
    print("If you do, Congrats, you beat my game.")
    time.sleep(4)
    print("HOWEVER, if you lose... you die... yeah that's about it.")
    print()
    print("Simple right... GREAT, LET'S PLAY")
    print()
    time.sleep(3)

def turns():
    global player_health
    global villain_health
    player_health = 100
    villain_health = 200
    time.sleep(2)

    #boss = Boss(ty, wp, sz)
    #boss.create(random.choice(ty), random.choice(wp), random.choice(sz))
    #print("This BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")

    print("You have TWO choices in order to proceed")   # then you are giving the three choices, you choose ONE
    while player_health > 0 and villain_health > 0:   # this may not work
        player_choice = input("Do you wish to [Rest/Fight]: ")
        if player_choice == "Rest":
            print("You choose to REST.")
            time.sleep(2)
            gain_lose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            roll = random.choice(gain_lose)
            if roll <= 6:
                print("You rolled a", roll)
                player_health = player_health - 15
                time.sleep(1)
                print("You are at", player_health)
                print("You were hit with a attack and lost 15 HP, what will you do next?")
        if player_choice == "Fight":
            print("You choose to FIGHT.")
            time.sleep(2)
            gain_lose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            roll = random.choice(gain_lose)
            if roll <= 5:
                print("You rolled a", roll)
                player_health = player_health - 20
                time.sleep(1)
                print(player_health)
                print("You were hit with a attack and lost 20 HP, what will you do next?")
            elif roll >= 6:
                print("You rolled a", roll)
                villain_health = villain_health - 35
                print("The BOSS is at", villain_health)
                print("You managed to hit the BOSS with a attack they lost 35 HP, what will you do next?")
    print("GAME OVER. Let's go see the results")

def final_outcome():
    global player_health
    global villain_health
    time.sleep(3)
    print("You made it to the end.... and it seems that...")
    time.sleep(2)
    print(player_health)
    if villain_health == 0:
        print("YOU WIN!!")
    if player_health == 0:
        print("Sorry.... you lose!")

def main():
    user = input("Please enter your name player: ")
    instructions(user)

    #boss = Boss(ty, wp, sz)
    #boss.create(random.choice(ty), random.choice(wp), random.choice(sz))
    #print("This BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")

    turns()
    final_outcome()
main()
