# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True

def days_per_month(year,month):
    if is_leap_year(year) == True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days

def day_of_year (year,month,day):
    month_days = days_per_month(year,month)
    m = 0
    days = 0
    while m < month - 1:
        days = month_days[m] + days
        m = m + 1
    days = days + day
    return days

def year_total (year1, year2, month, day):
    days = 0
    while year1 < year2:
        days = sum(days_per_month(year1,month)) + days - day_of_year(year1,month,day)
        month = 0
        day = 0
        year1 = year1 + 1
    return days


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1 == year2:
        return day_of_year(year2,month2,day2) - day_of_year(year1,month1,day1)
    return year_total(year1, year2, month1, day1) + day_of_year(year2,month2,day2)

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
