"""A vaccination calculator."""

__author__ = "730317621"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))

doses_administered: int = int(input("Doses Administered: "))

doses_per_day: int = int(input("Doses Per Day: "))

target_percent_vaccinated: int = int(input("Target Percent Vaccinated: "))

one_day: timedelta = timedelta(1)

days_to_percent_vaccinated: int = int(2 * population * target_percent_vaccinated / doses_per_day)

target_vaccination_length: timedelta = timedelta(days_to_percent_vaccinated)


today: datetime = datetime.today()
future: datetime = today + target_vaccination_length

target_vaccination_date: datetime = future.strftime("%B %d, %Y")

print("We will reach " + str(target_percent_vaccinated) + "% vaccination in " + str(days_to_percent_vaccinated) + " days, which falls on " + str(target_vaccination_date) + ".")

