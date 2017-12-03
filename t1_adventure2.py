######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T1: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start of not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]")

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)


if dead == True:
    quit()

#########################################################################################################

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.

# TODO Don't forget to check if your user is dead at the end of your chapter!

print()
print("Welcome,", username, ", to the Underground")
time.sleep(delay)
print("You seem to have fallen into with no easy way to get out.")
print("Before you lies two paths.")
time.sleep(delay)
print("One path takes you through a journey of Mercy, leading you to your ticket out of the Underground.")
print("The other, is a game of Genocide where you have to kill your way home... or die trying")
print("Choose wisely")
print()
time.sleep(delay * 2)
print("Before you is a hallway with a dim light at the end.")
time.sleep(delay / 2)
print("Staying here is certainly not wise. You must find your way out.")
print()
time.sleep(delay)
direction = input("Which direction would you like to go? [North/East/West]")

#########################################################################################################

if direction == "East":
   print("You see a seemingly harmless flower.")
   time.sleep(delay / 2)
   print("Hi There. I'm Flowely. Flowely the Flower")
   print("To make it out of here alive you have to fight me and win")
   time.sleep(delay)
   print("Let's see whatcha got kid")
elif direction == "West":
   print("You make it to the end and see a... monster?!")
   time.sleep(delay)
   print("The monster attacks you and you can only run and hide.")
   print("You run down the hallway and run into a wall. It's over now.")
   time.sleep(delay)


   speed = int(input("How many steps would you like to take?"))
   if speed < 5:
       print("Flowly hits you with everything he's got and it seems it's too much for you")
       time.sleep(delay*2)
       print("don't give up. Head on back into the Underground to try again")
       dead = True
   else:
       print("Before the monster can reach you it is blasted out of the way.")
       time.sleep(delay)
       print("The monster runs away in fear and out of the darkness comes a figure.")
       time.sleep(delay)
       print()
       print("Don't worry young one. Everything is going to be okay.")
       time.sleep(delay)
       print("You live to see another day here in the Underground")

else:
   print("You walk to the end of the hallway. You walk into a room and see a alter right in the center")
   time.sleep(delay)
   print("Inside the alter is a toy knife. You grab the knife for your safety and head back into the Undergraoung.")


if dead == True:
    quit()

#####################################################################################################################

if dead == True:
    quit()

######################################################################################################################
#  TODO Once you've tested your code (all three or more paths), copy your code between the blocks of ###'s,
# TODO plus the death code above, into your Google Doc.
# TODO The instructor will be combining it all into the master program.
