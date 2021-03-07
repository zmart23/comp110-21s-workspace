"""EX03 - palindromify function."""

__author__: str = "730317621"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))

def palindromify(word: str, factual: bool) -> str:
    i: int = 0
    mirror: int = int(len(word)/2)
    while i <= len(word) - 1:
        if len(word) % 2 == 0:
            return 
                i += 1
        else:
            return
                i += 1
        return True

if __name__ == "__main__":
    main()