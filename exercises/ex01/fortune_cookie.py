"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730317621"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")

fortune:int = int(randint(1,100))


if fortune < 60:
    if fortune < 30:
        print("You will be gifted with a large sum of money.")
    else:
        print("You will live a long and happy life.")
else:
    if fortune < 90:
        print("Everything you do today will prosper.")
    else:
        print("You will find love in the near future.")

print("Now, go spread positive vibes!")
