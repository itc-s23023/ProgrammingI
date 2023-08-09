"""
def color_weekday(weekday):
    if weekday == 5:  # Saturday
        return "\033[92m"  # Green color code
    elif weekday == 6:  # Sunday
        return "\033[91m"  # Red color code
    else:
        return "\033[0m"  # Reset color code


def color_calendar(year, month):
    import calendar

    cal = calendar.monthcalendar(year, month)
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                day_str = str(day).rjust(2)
                weekday = calendar.weekday(year, month, day)
                week_str += f"{color_weekday(weekday)}{day_str}\033[0m "
        print(week_str)


color_calendar(2023, 8)
"""
s1 = "{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}\033[32m{:>4s}\033[0m\033[31m{:>4s}\033[0m".format(
    "Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"
)
s1 += "\n"
s2 = "{:4s}".format(" ")
for i in range(1, 32):
    if i % 7 == 5:
        s2 += "\033[32m{:>4s}\033[0m".format(str(i))
    elif i % 7 == 6:
        s2 += "\033[31m{:>4s}\033[0m".format(str(i))
    else:
        s2 += "{:>4s}".format(str(i))
print(s1 + s2)
