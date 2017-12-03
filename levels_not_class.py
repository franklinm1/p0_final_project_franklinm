import random
import time

def level_one():               # first you are told how many points you have
    num_points = 20
    print("Hello, and welcome to the first level.")
    print("You start with", num_points, "points.")
    time.sleep(2)
    print("You have THREE choices in order to proceed")   # then you are giving the three choices, you choose ONE
    player_choice = input("Do you wish to {Run/Hide/Fight]: ")
    if player_choice == "Run":
        num_points = num_points - 2  # you lose 2 points no matter what
        print("You choose to RUN.")
        time.sleep(1)
        print("You lost 2 points and are now at", num_points, ". You may now continue dearest player.")
    if player_choice == "Hide":
        print("You choose to HIDE.")
        time.sleep(2)
        gain_lose = [2, 3]
        if random.choice(gain_lose) == 2:
            num_points = num_points - 2
            time.sleep(2)
            print("You lost 2 points and are now at", num_points, ". Shall we continue, dearest player.")
        else:
            num_points = num_points + 3
            print("You gained 3 points and are now at", num_points, ". This is getting fun! Let's keep going.")
    if player_choice == "Fight":
        print("You choose to FIGHT.")
        time.sleep(2)
        gain_lose = [3, 5]
        if random.choice(gain_lose) == 3:
            num_points = num_points - 3
            time.sleep(2)
            print("You lost 3 points and are now at", num_points, ". Don't worry, everyone has one of those days. Lets keep going.")
        else:
            num_points = num_points + 5
            print("You gained 5 points and are now at", num_points, ". You did it!! More fun awaits.")

def level_two():
    time.sleep(3)
    num_points = 20
    print("You made it to the next level. CONGRATS.")
    print("Just as a reminder you have", num_points, "points.")
    time.sleep(2)
    choice_one = input("Do you wish to {Run/Hide/Fight]: ")
    if choice_one == "Run":
        num_points = num_points - 2  # you lose 2 points no matter what
        print("You choose to RUN.")
        time.sleep(1)
        print("You lost 2 points and are now at", num_points, ". You may now continue dearest player.")
    if choice_one == "Hide":        # you have a choice to lose 2 points or gain 3 points
        print("You choose to HIDE.")
        time.sleep(2)
        gain_lose = [2, 3]
        if random.choice(gain_lose) == 2:
            num_points = num_points - 2
            time.sleep(2)
            print("You lost 2 points and are now at", num_points, ". Shall we continue, dearest player.")
        else:
            num_points = num_points + 3
            print("You gained 3 points and are now at", num_points, ". This is getting fun! Let's keep going.")
    if choice_one == "Fight":        # you have a choice to lose 3 points or gain 5 points
        print("You choose to FIGHT.")
        time.sleep(2)
        gain_lose = [3, 5]
        if random.choice(gain_lose) == 3:
            num_points = num_points - 3
            time.sleep(2)
            print("You lost 3 points and are now at", num_points, ". Don't worry, everyone has one of those days. Lets keep going.")
        else:
            num_points = num_points + 5
            print("You gained 5 points and are now at", num_points, ". You did it!! More fun awaits.")

def level_three():
    time.sleep(3)
    num_points = 20
    print("You made it to the next level. CONGRATS.")
    print("Just as a reminder you have", num_points, "points.")
    time.sleep(2)
    choice_one = input("Do you wish to {Run/Hide/Fight]: ")
    if choice_one == "Run":
        num_points = num_points - 2  # you lose 2 points no matter what
        print("You choose to RUN.")
        time.sleep(1)
        print("You lost 2 points and are now at", num_points, ". You may now continue dearest player.")
    if choice_one == "Hide":        # you have a choice to lose 2 points or gain 3 points
        print("You choose to HIDE.")
        time.sleep(2)
        gain_lose = [2, 3]
        if random.choice(gain_lose) == 2:
            num_points = num_points - 2
            time.sleep(2)
            print("You lost 2 points and are now at", num_points, ". Shall we continue, dearest player.")
        else:
            num_points = num_points + 3
            print("You gained 3 points and are now at", num_points, ". This is getting fun! Let's keep going.")
    if choice_one == "Fight":        # you have a choice to lose 3 points or gain 5 points
        print("You choose to FIGHT.")
        time.sleep(2)
        gain_lose = [3, 5]
        if random.choice(gain_lose) == 3:
            num_points = num_points - 3
            time.sleep(2)
            print("You lost 3 points and are now at", num_points, ". Don't worry, everyone has one of those days. Lets keep going.")
        else:
            num_points = num_points + 5
            print("You gained 5 points and are now at", num_points, ". You did it!! More fun awaits.")

def level_four():
    time.sleep(3)
    num_points = 20
    print("You made it to the next level. CONGRATS.")
    print("Just as a reminder you have", num_points, "points.")
    time.sleep(2)
    choice_one = input("Do you wish to {Run/Hide/Fight]: ")
    if choice_one == "Run":
        num_points = num_points - 2  # you lose 2 points no matter what
        print("You choose to RUN.")
        time.sleep(1)
        print("You lost 2 points and are now at", num_points, ". You may now continue dearest player.")
    if choice_one == "Hide":        # you have a choice to lose 2 points or gain 3 points
        print("You choose to HIDE.")
        time.sleep(2)
        gain_lose = [2, 3]
        if random.choice(gain_lose) == 2:
            num_points = num_points - 2
            time.sleep(2)
            print("You lost 2 points and are now at", num_points, ". Shall we continue, dearest player.")
        else:
            num_points = num_points + 3
            print("You gained 3 points and are now at", num_points, ". This is getting fun! Let's keep going.")
    if choice_one == "Fight":        # you have a choice to lose 3 points or gain 5 points
        print("You choose to FIGHT.")
        time.sleep(2)
        gain_lose = [3, 5]
        if random.choice(gain_lose) == 3:
            num_points = num_points - 3
            time.sleep(2)
            print("You lost 3 points and are now at", num_points, ". Don't worry, everyone has one of those days. Lets keep going.")
        else:
            num_points = num_points + 5
            print("You gained 5 points and are now at", num_points, ". You did it!! More fun awaits.")

def level_five():
    time.sleep(3)
    num_points = 20
    print("You made it to the next level. CONGRATS.")
    print("Just as a reminder you have", num_points, "points.")
    time.sleep(2)
    choice_one = input("Do you wish to {Run/Hide/Fight]: ")
    if choice_one == "Run":
        num_points = num_points - 2  # you lose 2 points no matter what
        print("You choose to RUN.")
        time.sleep(1)
        print("You lost 2 points and are now at", num_points, ". You may now continue dearest player.")
    if choice_one == "Hide":        # you have a choice to lose 2 points or gain 3 points
        print("You choose to HIDE.")
        time.sleep(2)
        gain_lose = [2, 3]
        if random.choice(gain_lose) == 2:
            num_points = num_points - 2
            time.sleep(2)
            print("You lost 2 points and are now at", num_points, ". Shall we continue, dearest player.")
        else:
            num_points = num_points + 3
            print("You gained 3 points and are now at", num_points, ". This is getting fun! Let's keep going.")
    if choice_one == "Fight":        # you have a choice to lose 3 points or gain 5 points
        print("You choose to FIGHT.")
        time.sleep(2)
        gain_lose = [3, 5]
        if random.choice(gain_lose) == 3:
            num_points = num_points - 3
            time.sleep(2)
            print("You lost 3 points and are now at", num_points, ". Don't worry, everyone has one of those days. Lets keep going.")
        else:
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
    level_one()
    level_two()
    level_three()
    level_four()
    level_five()
    final_outcome()

main()
