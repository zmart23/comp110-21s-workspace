"""Choose Your Own Adventure Project 00."""

__author__ = "730317621"


def main() -> None:
    """The entrypoint of the module, when run as a program."""
    points = 0
    trials = 0
    player = ""
    response = ""
    greet()
    while response !=  "Finish Experience.":
        print()
        print("Choose A Game: ")
        print("Which Star Wars Vehicle Are You?")
        print("Which Star Wars Character Are You?")
        print("Which Star Wars Planet Do You Live On?")
        print("Finish Experience.")
        print()
        response: str = str(input("Which game would you like to play? "))
        a: str = str("Which Star Wars Vehicle Are You?")
        b: str = str("Which Star Wars Character Are You?")
        c: str = str("Which Star Wars Planet Do You Live On?")
        d: str = str("Finish Experience.")
    #  sw_vehicle_quiz(points)
        # while True:
        if response == a:
            points = sw_vehicle_quiz(points)
            print(f"You have {points} points.")
        else:
            if response == b:
                sw_character_quiz()
                print(f"You have {points} points.")
            else:
                if response == c:
                    sw_planet_quiz(points)
                    print(f"You have {points} points.")
                else:
                    if response == d:
                        end_message(points)


def greet() -> None:
    """Greeting message to player."""
    global player
    player = input("What is your name? ")
    print()
    print(f"Hello, {player}, welcome to Star Wars Mania. In this game, there will be two quiz options available which will ask you various questions and determine something in Star Wars that relates to you. For each game played, you will receive a fixed amount of adventure points. Different prizes will be rewarded for different point totals.")


def sw_vehicle_quiz(game_points: int) -> int:
    """Quiz that takes various inputs to decide what Star Wars vehicle you pilot."""
    #main()
    #greet()
    print(f"Well, {player}, this game is called 'What Star Wars Vehicle Do You Pilot?.' You will be asked a series of questions that may seem unrelated but these questions will indeed help me to determine what Star Wars vehicle you would pilot. For each time you complete the quiz, you will earn 50 adventure points.")
    material: str = str(input(f"{player}, would you like a ship made of wood or metal?"))
    seats: int = int(input(f"{player}, would you like 2 seats or 4 seats?"))
    speed: str = str(input(f"{player}, would you like a fast vehicle or a slow one?"))
    if material == "wood":
        if seats == 2:
            if speed == "slow":
                print("You pilot a speeder bike.")
                game_points += 4
            elif speed == "fast":
                print("You pilot a snowspeeder.")
        elif seats == 4: 
            if speed == "slow":
                print("You pilot the Death Star.")
            elif speed == "fast":
                print("You pilot an X-wing Starfighter")
    if material == "metal":
        if seats == 2:
            if speed == "slow":
                print("You pilot the Millennium Falcon.")
            elif speed == "fast":
                print("You pilot a medical frigate.")
        elif seats == 4:
            if speed == "fast":
                print("You pilot a sandcrawler.")
            elif speed == "slow":
                print("You pilot a star destroyer.")
    return game_points

def sw_planet_quiz(points: int) -> int:
    """Quiz that takes various inputs to decide which Star Wars planet you live on."""
    main()
    greet()
    print(f"Well, {player}, this game is called 'Which Star Wars Planet Do You Live On?.' You will be asked a series of questions that may seem unrelated but these questions will indeed help me to determine what Star Wars planet you live on. For each time you complete the quiz, you will earn 50 adventure points.")
    terrain: str = str(input(f"{name}, what kind of terrain does your planet have: desert or forest?"))
    weather: str = str(input(f"{name}, what kind of weather is frequent on your planet: rainy or sunny?"))
    desert: str = str
    forest: str = str
    rainy: str = str
    sunny: str = str
    if terrain == desert:
        if weather == rainy:
            print("You live on Naboo.")
    if terrain == desert:
        if weather == sunny:
            print("You live on Hoth.")
    if terrain == forest:
        if weather == rainy:
            print("You live on Endor.")
    if terrain == forest:
        if weather == sunny:
            print("You live on Coruscant.")


def sw_character_quiz() -> None:
    """Quiz that takes various inputs to decide which Star Wars character you are."""
    main()
    greet()
    print(f"Well, {player}, this game is called 'Which Star Wars Character Are You?.'You will be asked a series of questions that may seem unrelated but these questions will indeed help me to determine what Star Wars character you are. For each time you complete the quiz, you will earn 50 adventure points.")
    clothes: str = str(input(f"{name}, what kind of clothes do you wear: fancy or common?"))
    height: str = str(input(f"{name}, what is the height of your character: short or tall?"))
    fancy: str = str
    common: str = str
    short: str = str
    tall: str = str
    if clothes == fancy:
        if height == tall:
            print("You are Anakin Skywalker.")
    if clothes == fancy:
        if height == short:
            print("You are Han Solo.")
    if clothes == common:
        if height == tall:
            print("You are Mace Windu.")
    if clothes == common:
        if height == short:
            print("You are Count Dooku.")


def end_message(end_points: int) -> None:
    """Prints goodbye message with total accumulated adventure points."""
    print(f"Goodbye, you have {end_points} adventure points.")


if __name__ == "__main__":
    main()
