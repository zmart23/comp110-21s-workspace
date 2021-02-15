"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730317621"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days_to_target(population, doses, doses_per_day, target)
    days_per_vac: int = round(population * 2 * ((target / 100) - (doses / 2 / population)) / doses_per_day)
    length: int = int(days_per_vac)
    how_many_days: timedelta = timedelta(days_per_vac)
    future_date(how_many_days)
    date: int = int(perc_reached)
    print("We will reach " + str(target) + "% vaccination in " + str(length) + " days, which falls on " + str(date) + ".")

def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """How many days until target percentage vaccinated is reached."""
    one_day: timedelta = timedelta(1)
    days_per_vac: int = round(population * 2 * ((target / 100) - (doses / 2 / population)) / doses_per_day)
    how_many_days: timedelta = timedelta(days_per_vac)
    return days_per_vac

def future_date(how_many_days: int) -> str:
    """What date desired target percentage vaccinated is reached."""
    today: datetime = datetime.today()
    future: datetime = today + how_many_days
    perc_reached: datetime = future.strftime("%B %d, %Y")
    return perc_reached

if __name__ == "__main__":
    main()
