"""
File: BeeperRowAdv.py
Name: Ann Wu
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
   while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
        if not on_beeper():
            put_beeper()






####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)