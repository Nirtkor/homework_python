
def date_verify(day, month, year):
    month_1 = [1, 3, 5, 7, 8, 10, 12]
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0 and month == 2 and day < 30:
            return False
        else:
            if month == 2 and day < 30:
                return True
    else:
        if month in month_1 and 0 < day < 32:
            return True
        elif 0 < month < 13 and 0 < day < 31 and month != 2:
            return True
        elif month == 2 and 0 < day < 29:
            return True
    return False
