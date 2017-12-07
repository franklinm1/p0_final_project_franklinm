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
    def __init__(self):
        self.type = []    # the type or in my games case "occupation"
        self.weapon = []  # type of weapon that the villain can use
        self.size = []   # the size the villain can be

    def create(self):
        ty = ["Physician", "Nurse", "Orderly", "Medical Examiner", "Therapist"]
        wp = ["telekinesis", "a surgical saw", "long chains", "mind control", "a giant scalpel"]
        sz = ["small", "big", "tall", "towering", "large"]

        boss = random.choice(ty)
        if boss == "Physician":
            wp = ["a surgical saw", "a giant scalpel"]
            sz = ["big", "tall", "towering"]
            print("The BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")
        elif boss == "Medical Examiner":
            wp = ["stryker saws"]
            sz = ["lofty", "towering", "giant"]
            print("The BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")
        elif boss == "Nurse":
            wp = ["telekinesis", "long chains"]
            sz = ["small"]
            print("The BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")
        elif boss == "Orderly":
            wp = ["telekinesis", "long chains"]
            sz = ["small"]
            print("The BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")
        elif boss == "Therapist":
            wp = ["telekinesis", "mind control"]
            sz = ["large"]
            print("The BOSS is a", random.choice(sz), boss, "and welds", random.choice(wp), "as their weapon")

def instructions(user):
    print("Hello There,", user, "and welcome to my game!")
    time.sleep(2)
    print("The Abandoned Hospital.")
    time.sleep(2)
    print()
    print("The rules and objectives are simple: Beat the BOSS and you win!")
    time.sleep(4)
    print()
    print("Your goal is to get through the hospital without dying.")
    time.sleep(3)
    print()
    print("A random BOSS will be generated at the beginning of the game.")
    time.sleep(3)
    print("You can do one of two things.")
    print()                                         # these are the two options you have on each floor
    print("You can either REST or FIGHT")
    print()
    time.sleep(2)
    print("If you REST there will be a chance that the BOSS will damage you")
    time.sleep(2)
    print()
    print("If you roll a 7 or more the BOSS misses their attack")
    print("If you roll a 6 or less you are damaged by the BOSS")
    time.sleep(5)
    print()
    print("The other option is to FIGHT")
    print()
    print("On this one the stakes are a little higher")
    print()
    time.sleep(4)
    print("If you roll a 6-9 or more you land a successful attack on the BOSS")
    print("If you roll a 2-4 or less you are damaged by the BOSS")
    time.sleep(5)
    print()
    print("There are also special rolls you can get that will lead to different attacks, with different damage types")
    time.sleep(3)
    print()
    print("The special numbers are 1, 5, and 10")
    time.sleep(3)
    print()
    print("The goal of the game is to beat the BOSS")
    print("If you do, Congrats, you beat my game.")
    time.sleep(4)
    print()
    print("HOWEVER, if you lose... you die... yeah that's about it.")
    print()
    print("Simple right... GREAT, LET'S PLAY")
    print()
    time.sleep(3)

def turns():
    global player_health
    global villain_health
    player_health = 100
    print("You start off with 100 health")
    villain_health = 200
    print("The BOSS starts off with 200 health")
    time.sleep(2)
    print()
    print("You have TWO choices in order to proceed")   # then you are giving the three choices, you choose ONE
    while player_health > 0 and villain_health > 0:
        player_choice = input("Do you wish to [Rest/Fight]: ")
        print()
        if player_choice == "Rest":
            print("You choose to REST.")
            print()
            time.sleep(2)
            gain_lose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            roll = random.choice(gain_lose)
            if roll <= 5:      # 1-5                # If you roll a 1-6 you lose health
                print("You rolled a", roll)
                player_health = player_health - 10
                time.sleep(1)
                print("You are at", player_health, "health")
                print("You were hit with a AVERAGE attack and lost 10 HP, what will you do next?")
                print()
            else:
                print("You dodged the attack, losing no health")
                print()
        if player_choice == "Fight":
            print("You choose to FIGHT.")
            print()
            time.sleep(2)
            gain_lose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            roll = random.choice(gain_lose)
            if roll in range(2, 5):  # 2-4
                print("You rolled a", roll)          # if you roll a 2-4 the PLAYER takes 25 damage
                player_health = player_health - 25
                time.sleep(2)
                print("You are at", player_health, "health")
                print("You were hit with a AVERAGE attack and lost 25 HP, what will you do next?")
                print()
            elif roll == 1:
                print("You rolled a", roll)          # if you roll a 1 the PLAYER takes 50 damage
                player_health = player_health - 45
                time.sleep(2)
                print("You are at", player_health, "health")
                print("You were hit with a CRITICAL attack and lost 45 HP!, what will you do next?")
                print()
            elif roll in range(6, 10):
                print("You rolled a", roll)           # if you roll a 6-9 the BOSS takes 55 damage
                villain_health = villain_health - 55
                print()
                time.sleep(2)
                print("You hit the BOSS with a AVERAGE hit")
                print()
                print("The BOSS is at", villain_health)
                print("The BOSS lost 55 HP, what will you do next?")
                print()
            elif roll == 5:   # 5
                print("You rolled a", roll)           # if you roll a 5 the BOSS takes 35 damage
                villain_health = villain_health - 35
                print()
                time.sleep(2)
                print("You hit the BOSS with a AVERAGE attack")
                print()
                print("The BOSS is at", villain_health)
                print("The BOSS lost 35 HP, what will you do next?")
                print()
            elif roll == 10:  # 10
                print("You rolled a", roll)            # if you roll a 10 the BOSS takes 100 damage
                villain_health = villain_health - 100
                print()
                time.sleep(2)
                print("You hit the BOSS with a CRITICAL attack")
                print()
                print("The BOSS is at", villain_health)
                print("The BOSS lost 100 HP!, what will you do next?")
                print()
    print("GAME OVER. Let's go see the results")
    print()

def final_outcome():
    global player_health
    global villain_health
    time.sleep(3)
    print("You made it to the end.... and it seems that...")
    print()
    time.sleep(2)
    if villain_health <= 0:
        time.sleep(1)
        print("YOU WIN!!")
        print()
        print("You survived with", player_health, "health left.")
        print()
        time.sleep(1)
        print("THANKS FOR PLAYING!")
    if player_health <= 0:
        time.sleep(1)
        print("You unfortunately didn't make it...")
        print()
        time.sleep(1)
        print("Well... THANKS FOR PLAYING!")

def main():
    user = input("Please enter your name player: ")
    print()
    instructions(user)

    boss = Boss()   # this creates the object in the class Boss
    boss.create()

    turns()
    final_outcome()

main()