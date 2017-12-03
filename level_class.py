import random
import time

class Level:
    """
    This is the class I created to manipulate my idea of levels in my simulation game.
    """
    def __init__(self):
        self.name = ""
        self.positions = {}
        self.points = 0

    def level_one(num_points):               # first you are told how many points you have
        num_points = 20
        print("You start with", num_points, ".")

        print("Hello, and welcome to the first level")   # then you are giving the three choices, you choose ONE
        time.sleep(2)
        print("You have THREE choices in order to proceed")
        choice_one = input("Do you wish to {Run/Hide/Fight}?")
        if choice_one == "Run":
            num_points = num_points - 2  # you lose 2 points no matter what
            print("You choose to RUN.")
            time.sleep(1)
            print("You lost 2 points and are now at", num_points, ". You may now continue dearest player.")
        if choice_one == "Hide":
            gain_lose = [3, 5]
            while random.choice(gain_lose) == 3:
                num_points = num_points - 3
                print(num_points)
            num_points = num_points + 5
            print(num_points)
                                                              # next your points are affected by the choice you make
                                                              # finally you move to the next level

