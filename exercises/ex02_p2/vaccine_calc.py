"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730317621"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    daytota = days_to_target(population, doses, doses_per_day, target)
    fudat = future_date(daytota)
    leng: int = int(daytota)
    dat: int = int(fudat)
    print("We will reach " + str(target) + "% vaccination in " + str(leng) + " days, which falls on " + str(dat) + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """How many days until target percentage vaccinated is reached."""
    days_per_vac: int = round(population * 2 * ((target / 100) - (doses / 2 / population)) / doses_per_day)
    return days_per_vac


def future_date(howmanydays: int) -> str:
    """What date desired target percentage vaccinated is reached."""
    today: datetime = datetime.today()
    target_vaccination_length: timedelta = timedelta(howmanydays)
    future: datetime = today + target_vaccination_length
    time: datetime = future.strftime("%B %d, %Y")
    fut_time: str = int(time)
    return fut_time


if __name__ == "__main__":
    main()