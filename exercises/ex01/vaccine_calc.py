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


pop: int = int(input("Population: "))

doses_admin: int = int(input("Doses Administered: "))

doses_per_day: int = int(input("Doses Per Day: "))

targ_per: int = int(input("Target Percent Vaccinated: "))

one_day: timedelta = timedelta(1)

days_per_vac: int = int((pop) * 2 * ((targ_per / 100) - (doses_admin / 2 / pop)) / doses_per_day)  
target_vaccination_length: timedelta = timedelta(days_per_vac)


today: datetime = datetime.today()
future: datetime = today + target_vaccination_length

targ_vac_date: datetime = future.strftime("%B %d, %Y")

print("We will reach " + str(targ_per) + "% vaccination in " + str(days_per_vac) + " days, which falls on " + str(targ_vac_date) + ".")