"""Choose Your Own Adventure Project 00"""

__author__ = "730317621"

from random import randint

def main() -> None:
    """The entrypoint of the module, when run as a program."""
    greet()
    points: int = int(adventure_points)
    print("Menu: ")
    print("Which Star Wars Vehicle Are You?")
    print("Which Star Wars Character Are You?")
    print("Finish Experience")
    print()
    response: str = str(input("Which game would you like to play?"))
    a: str = str("Which Star Wars Vehicle Are You?")
    b: str = str("Which Star Wars Character Are You?")
    while True:
        if response == a:
            sw_vehicle_quiz(points: int)
        if response == b:
            sw_character_quiz(points)
        else:
            print(f"You have {points} adventure points.")
    
    
def greet() -> None:
    """Greeting message to player."""
    player: str = input("What is your name?")
    print(f"Hello, {player}, welcome to Star Wars Mania. In this game, there will be two quiz options available which will ask you various questions and determine something in Star Wars that relates to you. For each game played, you will receive a fixed amount of adventure points. Different prizes will be rewarded for different point totals.")


def sw_vehicle_quiz(points: int) -> int:
    """Quiz that takes various inputs to decide what Star Wars vehicle you pilot."""
    main()
    greet()
    print(f"Well, {player}, this game is called 'What Star Wars Vehicle Do You Pilot?.' You will be asked a series of questions that may seem unrelated but these questions will indeed help me to determine what Star Wars vehicle you would pilot. For each time you complete the quiz, you will earn 50 adventure points.")
    material: str = str(input("Would you like a ship made of wood or metal?"))
    seats: str = int(input("Would you like 2 seats or 4 seats?"))
    speed: str = str(input("Would you like a fast vehicle or a slow one?"))
    wood: str = str
    metal: str = str
    fast: str = str
    slow: str = str
    if material = wood:
        if seats = 2:
            if speed = fast:
                print("You pilot a speeder bike.")
    if material = wood:
        if seats = 4:
            if speed = fast:
                print("You pilot a star destroyer.")
    if material = wood:
        if seats = 2:
            if speed = slow:
                print("You pilot a medical frigate.")
    if material = wood:
        if seats = 4:
            if speed = slow:
                print("You pilot the Death Star.")
    if material = metal:
        if seats = 2:
            if speed = fast:
                print("You pilot a snowspeeder.")
    if material = metal:
        if seats = 4:
            if speed = fast:
                print("You pilot the Millennium Falcon.")
    if material = metal:
        if seats = 2:
            if speed = slow:
                print("You pilot an X-wing Starfighter")
    if material = metal:
        if seats = 4:
            if speed = slow:
                print("You pilot a sandcrawler.")
    else:
        print ()


def sw_character_quiz (points):
    """Quiz that takes various characteristic inputs to decide which Star Wars character you are."""
    global points
    points = 


def end_message () -> None:
    "Prints goodbye message with total accumulated adventure points."
    





if __name__ == "__main__":
    main()