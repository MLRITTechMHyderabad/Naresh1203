"""You are given a date. Your task is to find what the day is on that date.
Input
A single line of input containing the space separated month, day and year,
respectively, in MM DD YYYY format.
08 05 2015
Output
Output the correct day in capital letters.
WEDNESDAY"""

import datetime
mm, dd, yyyy = map(int, input().split())
date_obj = datetime.date(yyyy, mm, dd)
day_name = date_obj.strftime("%A").upper()
print(day_name)
