# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_days_ly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_diff(day1, day2):
    return max(day1,day2) - min(day1,day2)

#def month_diff(month,day):

def is_leap_year(year):
    if year % 4 != 0:
        return 365
    if year % 100 != 0:
        return 366
    if year % 400 != 0:
        return 365
    return 366

def days_year(year1,year2):
    days = 0
    while year1 != year2:
        days = is_leap_year(year1) + days
        year1 = year1 + 1
    return days

def days_month(year, month1,month2):
    days = 0
    while month1 != month2:
        if is_leap_year(year) == 366:
            days = month_days_ly[month1 - 1] + days
        days = month_days[month1 - 1] + days
    return days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##

    return days_year(year1,year2) + days_month(year2,month1,month2) + day_diff(day1,day2)


#print daysBetweenDates(2015,1,1,2015,3,5)

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
