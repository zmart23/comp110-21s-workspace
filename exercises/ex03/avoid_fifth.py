"""EX03 - avoid_fifth function."""

__author__: str = "730317621"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("welcome friend"))
    print(avoid_fifth("have a great day mEn and womEn"))

def avoid_fifth(stay_away: str) -> str:
    fifth: str = ""
    i: int = 0
    while i <= len(stay_away) - 1:
        if stay_away[i] != "e" and stay_away[i] != "E":
            fifth += stay_away[i]
        i += 1
    return fifth


if __name__ == "__main__":
    main()