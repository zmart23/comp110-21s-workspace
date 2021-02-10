"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730317621"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")

def fortune_cookie() -> str:
    """Definition of the fortune_cookie function."""
    a: int = int(randint(1, 100))
    if a < 60:
        if a < 30:
            return "You will be gifted with a large sum of money."
        return "You will live a long and happy life."
    else:
        if a < 90:
            return "Everything you do today will prosper."
        return "You will find love in the near future."

 
if __name__ == "__main__":
    main()