"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730317621"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")

from random import randint

def fortune_cookie(a: int = int(randint(1, 100))) -> str:
    """Definition of the fortune_cookie function."""
    if a < 60:
        if a < 30:
            return "You will be gifted with a large sum of money."
        return "You will live a long and happy life."
    else:
        if a < 90:
            return "Everything you do today will prosper."
        return "You will find love in the near future."



# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()