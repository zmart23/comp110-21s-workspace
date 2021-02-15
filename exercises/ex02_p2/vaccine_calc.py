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
    future_date(howmanydays)
    length: int = int(days_per_vac)
    date: int = str(future_date)
    print("We will reach " + str(target) + "% vaccination in " + str(length) + " days, which falls on " + str(date) + ".")

def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """How many days until target percentage vaccinated is reached."""
    one_day: timedelta = timedelta(1)
    days_per_vac: int = round(population * 2 * ((target / 100) - (doses / 2 / population)) / doses_per_day)
    return days_per_vac

def future_date(howmanydays: int) -> str:
    """What date desired target percentage vaccinated is reached."""
    today: datetime = datetime.today()
    target_vaccination_length: timedelta = timedelta(howmanydays)
    future: datetime = today + target_vaccination_length
    future_date: datetime = future.strftime("%B %d, %Y")
    return future_date

if __name__ == "__main__":
    main()