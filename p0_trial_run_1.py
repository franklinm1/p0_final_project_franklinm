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

def instructions(user):
    print("Hello There,", user, "and welcome to my game!")
    print("The Abandoned Hospital.")
    print("The rules and objectives are simple: Get to the final level with points to win!")
    time.sleep(4)
    print()
    print("Your goal is to get through the hospital with 30 points or more.")
    print("Since I'm nice, you get 20 points off the bat")
    time.sleep(6)
    print()
    print("The points system is simple: on each floor you will encounter a villain.")   # everything below explains the point system
    print("You can do one of three things.")
    time.sleep(6)
    print()                                         # these are the three options you have on each floor
    print("You can either RUN, HIDE, or FIGHT")     # this is the only choice where you have no chance to gain points
    print("If you RUN you lose 1 point no matter what. But hey, you make it to the next level")
    time.sleep(5)
    print()
    print("If you HIDE you get to roll your fate")  # you have a 50/50 chance to gain points
    print("If you roll a 6 or more the villain doesn't see you and you receive 3 points")
    time.sleep(5)
    print("BUT if you roll a 5 or less the villain finds you, you lose 1 points, and you make it out by the skin of your teeth")
    time.sleep(5)
    print()
    print("The last option is to FIGHT")
    print("On this one the stakes are a little higher")
    time.sleep(4)
    print("If you roll a 8 or more you defeat the villain and gain 5 points")
    print("If you roll a 7 or less you are damaged by the villain and lose 2 points but still move to the next level.")
    time.sleep(6)
    print()
    print("By the time you make it to the final level, you should have 30 points or more")
    print("If you do, Congrats, you beat my game.")
    time.sleep(5)
    print("HOWEVER, if you lose... you are now one of my new villains.")
    print()
    print("Simple right... GREAT, LET'S PLAY")
    time.sleep(4)

def levels():               # first you are told how many points you have
    num_points = 20
    time.sleep(2)
    print("You have THREE choices in order to proceed")   # then you are giving the three choices, you choose ONE
    for i in range(5):
        player_choice = input("Do you wish to {Run/Hide/Fight]: ")
        if player_choice == "Run":
            num_points = num_points - 2  # you lose 2 points no matter what
            print("You choose to RUN.")
            time.sleep(1)
            print("You lost 2 points and are now at", num_points, ". You may now continue dearest player.")
        if player_choice == "Hide":
            print("You choose to HIDE.")
            time.sleep(2)
            gain_lose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if random.choice(gain_lose) <= 5:
                num_points = num_points - 2
                time.sleep(2)
                print("You lost 2 points and are now at", num_points, ". Shall we continue, dearest player.")
            elif random.choice(gain_lose) >= 6:
                num_points = num_points + 3
                print("You gained 3 points and are now at", num_points, ". This is getting fun! Let's keep going.")
        if player_choice == "Fight":
            print("You choose to FIGHT.")
            time.sleep(2)
            gain_lose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if random.choice(gain_lose) <= 7:
                num_points = num_points - 3
                time.sleep(2)
                print("You lost 3 points and are now at", num_points, ". Don't worry, everyone has one of those days. Lets keep going.")
            elif random.choice(gain_lose) >= 8:
                num_points = num_points + 5
                print("You gained 5 points and are now at", num_points, ". You did it!! More fun awaits.")

def final_outcome():
    num_points = 20   # i need to make this global
    time.sleep(3)
    print("You made it to the end. Now let's see what fate has in-store for you.")
    time.sleep(2)
    if num_points >= 20:
        print("YOU WIN!!")
    else:
        print("... Sorry, it looks like you didn't win. Well, thanks for playing HAHA.")
def main():
    user = input("Please enter your name: ")
    instructions(user)
    levels()
    final_outcome()


main()
