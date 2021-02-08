"""An exercise in remainders and boolean logic."""

__author__ = "730317621"


college:int = int(input("Enter an int: "))


output = ""

if college % 2 == 0:
    output = output + "TAR"
if college % 14 == 0: 
    output = output + " "
if college % 7 == 0:
    output = output + "HEELS"
if college % 7 == 0 or college % 2 == 0: 
    print(output)
else:
    print("CAROLINA")
