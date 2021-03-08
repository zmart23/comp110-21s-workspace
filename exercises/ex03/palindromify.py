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
    """Returns a palindrome of string input and boolean."""
    new_string: str = ""
    length = len(word)
    if factual is True:
        while length > 0:
            new_string += word[length - 1]
            length -= 1
            new_string = word[length] + new_string
    else:
        while length > 0:
            if length >= len(word):
                new_string = ""
                length -= 1
                new_string = word[length] + new_string
            else:
                new_string += word[length - 1]
                length -= 1
                new_string = word[length] + new_string
    return new_string


if __name__ == "__main__":
    main()