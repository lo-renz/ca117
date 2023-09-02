#!/usr/bin/env python3

import sys
import calendar

def output(n):
    sentence = "You were born on a "
    if n == 0:
        print(sentence + "Monday and Monday's child is fair of face")
    elif n == 1:
        print(sentence + "Tuesday and Tuesday's child is full of grace")
    elif n == 2:
        print(sentence + "Wednesday and Wednesday's child is full of woe")
    elif n == 3:
        print(sentence + "Thursday and Thursday's child has far to go")
    elif n == 4:
        print(sentence + "Friday and Friday's child is loving and giving")
    elif n == 5:
        print(sentence + "Saturday and Saturday's child works hard for a living")
    elif n == 6:
        print(sentence + "Sunday and Sunday's child is fair and wise and good in every way")

for numbers in sys.stdin:
    date = numbers.strip().split()
    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    calendarday = calendar.weekday(year, month, day)
    print(output(calendarday).strip())
