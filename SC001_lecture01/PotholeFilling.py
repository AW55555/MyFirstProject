"""
File: PotholeFilling.py
Name: Ann Wu
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()
    turn_around()
    for i in range(3):
        go_in_again()
        pick_99()
        go_out_again()
    turn_around()


def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole, facing East.
    post-condition:Karel is in the pothole, facing South.
    """
    move()
    turn_right()
    move()


def go_in_again():
    """
    per-condition:Karel is at the upper right of the pothole, facing West
    post-condition:Karel is in the pothole, facing South.
    """
    move()
    turn_left()
    move()


def go_out():
    """
    pre-condition:Karel is in the pothole, facing South.
    post-condition:Karel is at the upper left of the pothole, facing East.
    """
    turn_around()
    move()
    turn_right()
    move()


def go_out_again():
    """
    pre-condition:Karel is in the pothole, facing South.
    post-condition:Karel is in the upper left of the pothole, facing West.
    """
    turn_around()
    move()
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def put_99():
    for i in range(99):
        put_beeper()


def pick_99():
    for i in range(99):
        pick_beeper()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
