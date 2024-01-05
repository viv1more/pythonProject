def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [{"January": 31}, {"February": 28}, {"March": 31}, {"April": 30}, {"May": 31}, {"June": 30},
                  {"July": 31}, {"August": 31},
                  {"September": 30}, {"October": 31}, {"November": 30}, {"December": 31}]

    if is_leap_year(year) and month == 2:
        return {"February": 29}
    return month_days[month - 1]


year = int(input('enter the year - '))
month = int(input("enter the month - "))

days = days_in_month(year, month)

print(days)
