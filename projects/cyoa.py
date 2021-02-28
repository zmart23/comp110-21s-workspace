"""Choose Your Own Adventure Project 00.

I made a loop to bring the user back to a decision between 3 game pathways 
and an exit path. Additionally, I looped the points accrued from answering each 
question so that it added to the points global variable after each answer. I also 
made a global named constant that allowed me to use an emoji in my message in my 
exit path waving goodbye to the player(s) of my game.
"""

__author__ = "730317621"


from random import randint


points: int = 0
player: str = ""
WAVING_EMOJI: str = "\U0001F44B"


def main() -> None:
    """The entrypoint of the module, when run as a program."""
    points: int = 0
    response = ""
    greet()
    while response != "Finish Experience.":
        print()
        print("Choose A Game: ")
        print("Which Star Wars Vehicle Are You?")
        print("Bonus Points Game.")
        print("Which Star Wars Planet Do You Live On?")
        print("Finish Experience.")
        print()
        response: str = str(input("Which game would you like to play? "))
        a: str = str("Which Star Wars Vehicle Are You?")
        b: str = str("Bonus Points Game.")
        c: str = str("Which Star Wars Planet Do You Live On?")
        d: str = str("Finish Experience.")
        if response == a:
            points = sw_vehicle_quiz(points)
            print(f"You have {points} points.")
        else:
            if response == b:
                bonus_points_quiz()
                print(f"You have {points} points.")
            else:
                if response == c:
                    points = sw_planet_quiz(points)
                    print(f"You have {points} points.")
                else:
                    if response == d:
                        end_message(points)


def greet() -> None:
    """Greeting message to player."""
    global player
    player = input("What is your name? ")
    print()
    print(f"Hello, {player}, welcome to Star Wars Mania. In this game, there will be two quiz options "
          "available which will ask you various questions and determine something in Star Wars that relates "
          "to you. For each game played, you will receive various amounts of adventure points. Different "
          "prizes will be rewarded for different point totals.")


def sw_vehicle_quiz(veh_game_points: int) -> int:
    """Quiz that takes various inputs to decide what Star Wars vehicle you pilot."""
    print(f"Well, {player}, this game is called 'What Star Wars Vehicle Do You Pilot?.' You will be "
          "asked a series of questions that may seem unrelated but these questions will indeed help me to "
          "determine what Star Wars vehicle you would pilot. For each time you complete the quiz, you will "
          "earn an amount of adventure points based on your answer.")
    material: str = str(input(f"{player}, would you like a ship made of wood or metal? "))
    seats: int = int(input(f"{player}, would you like 2 seats or 4 seats? "))
    speed: str = str(input(f"{player}, would you like a fast vehicle or a slow one? "))
    if material == "wood":
        if seats == 2:
            if speed == "slow":
                print("You pilot a speeder bike.")
                veh_game_points += 1
            elif speed == "fast":
                print("You pilot a snowspeeder.")
                veh_game_points += 2
        elif seats == 4: 
            if speed == "slow":
                print("You pilot the Death Star.")
                veh_game_points += 3
            elif speed == "fast":
                print("You pilot an X-wing Starfighter.")
                veh_game_points += 4
    if material == "metal":
        if seats == 2:
            if speed == "slow":
                print("You pilot the Millennium Falcon.")
                veh_game_points += 5
            elif speed == "fast":
                print("You pilot a medical frigate.")
                veh_game_points += 6
        elif seats == 4:
            if speed == "fast":
                print("You pilot a sandcrawler.")
                veh_game_points += 7
            elif speed == "slow":
                print("You pilot a star destroyer.")
                veh_game_points += 8
    return veh_game_points


def sw_planet_quiz(plan_game_points: int) -> int:
    """Quiz that takes various inputs to decide which Star Wars planet you live on."""
    print(f"Well, {player}, this game is called 'Which Star Wars Planet Do You Live On?.' You will be asked "
          "a series of questions that may seem unrelated but these questions will indeed help me to determine what "
          "Star Wars planet you live on. For each time you complete the quiz, you will earn an amount of adventure "
          "points based on your answer.")
    terrain: str = str(input(f"{player}, what kind of terrain does your planet have: desert or forest? "))
    weather: str = str(input(f"{player}, what kind of weather is frequent on your planet: rainy or sunny? "))
    if terrain == "desert":
        if weather == "rainy":
            print("You live on Naboo.")
            plan_game_points += 1
        elif weather == "sunny":
            print("You live on Hoth.")
            plan_game_points += 2
    if terrain == "forest":
        if weather == "rainy":
            print("You live on Endor.")
            plan_game_points += 3
        elif weather == "sunny":
            print("You live on Coruscant.")
            plan_game_points += 4
    return plan_game_points


def bonus_points() -> None:
    """Procedure Reassigning Points Variable."""
    global points
    points = randint(1, 100)


def bonus_points_quiz() -> None:
    """Quiz that takes various inputs to decide how many bonus round points you can obtain."""
    bonus_points()
    print(f"Welcome, {player}, to the Bonus Round! In this game, you will earn bonus adventure "
          "points for each of the following questions you answer.")
    donkey = int(input("How many legs does a donkey have? "))
    spider = int(input("How many legs does a spider have? "))
    time = int(input("What digit time is noon(without the ':')? "))
    if donkey == 4:
        points
    if spider == 8:
        points
    if time == 12:
        points
    print()


def end_message(end_points: int) -> None:
    """Prints goodbye message with total accumulated adventure points."""
    print(f"Goodbye, you have {end_points} adventure points {WAVING_EMOJI}.")


if __name__ == "__main__":
    main()