import calendar


def has_friday_13(month, year):
    for i in range(1, calendar.monthrange(year, month)[1]):
        if calendar.weekday(year, month, i) == 4 and int(i) == 13:
            return True
    return False
