"""An exercise in remainders and boolean logic."""

__author__ = "730317621"


college:int = int(input("Enter an int: "))


if college % 2 == 0:
    print("TAR")
else:
    if college % 7 == 0:
        print("HEELS")
    else:
        print("TAR HEELS")# Begin your solution here...
