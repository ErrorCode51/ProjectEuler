month = 1
weekday = 1
year = 1900

def getMonthLength(month, year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    if month in [4,6,9,11]:
        return 30
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28

firstSundays = 0

while year <= 2000:
    for day in range(getMonthLength(month, year)):
        if day == 0 and weekday == 7 and year != 1900:
            firstSundays += 1
        weekday += 1
        if weekday > 7:
            weekday = 1

    month += 1
    if month > 12:
        month = 1
        year += 1
        print('Starting year', year, 'with weekday ', weekday)

print('Total first day of months that were sundays:', firstSundays)