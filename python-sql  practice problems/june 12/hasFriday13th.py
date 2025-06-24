"""Create a function in Python that accepts two parameters. They’ll both be numbers.
The first will be the month as a number, and the second will be the four-digit year.
The function should parse the parameters and return True if the month contains
a Friday the 13th and False if it doesn’t."""

import datetime

def has_friday_13(month, year):
    try:
        date = datetime.date(year, month, 13)
        return date.weekday() == 4  # 4 corresponds to Friday
    except ValueError:
        return False
