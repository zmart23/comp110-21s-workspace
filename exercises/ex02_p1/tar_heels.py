"""Tar Heels exercise redux as a structured program."""

__author__ = "730317621"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(tarithmetic: int) -> str:
    """Function that checks divisibility of various numbers by 2 and 7."""

    output = ""

    if tarithmetic % 2 == 0:
        output = output + "TAR"
    if tarithmetic % 14 == 0: 
        output = output + " "
    if tarithmetic % 7 == 0:
        output = output + "HEELS"
    if tarithmetic % 7 == 0 or tarithmetic % 2 == 0: 
        return output
    else:
        return "CAROLINA"


if __name__ == "__main__":
    main()