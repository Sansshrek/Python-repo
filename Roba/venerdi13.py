from datetime import date
from dataclasses import dataclass

@dataclass
class data:
    year = day_year = month = day_month = day_week = 0
today = count = data

def checkMonthMax(month, day):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max = 31
    elif month == 2:  #feb
        if day == 366:  #if leap year
            max = 29
        else:
            max = 28
    else:
        max = 30
    return max

def checkLeap(year):
    day = 365
    r1 = count.year % 4
    r2 = count.year % 400
    if r1 == 0 or r2 == 0:  #leap year
        day = 366
    return day

def NuovoCheck(max):
    year_max = today.year + max  #set the max of the year you want to check
    print("day {}, month {}, year {}, day of week {}, day of year {}, max year {}".format(count.day_month ,count.month ,count.year ,count.day_week ,count.day_year, year_max ))
    print("List of every friday 13th in ", max, "year")
    for count.year in range(count.year, year_max+1):  #years
        print()
        print("Anno {}:".format(count.year))
        day_in_year = checkLeap(count.year)
        while(count.day_year <= day_in_year):  #day in year
            day_month_max = checkMonthMax(count.month, day_in_year)  #how many days are in that month
            for count.day_month in range(count.day_month, day_month_max+1):
                if count.day_month == 13 and count.day_week == 5:  #check friday 13
                    print("- {}/{}/{}".format(count.day_month, count.month, count.year))
                count.day_week += 1  #day in week
                if count.day_week == 8:  #reset week
                    count.day_week = 1
                count.day_year += 1  #add day in year
            count.day_month = 1  #reset day in month
            count.month += 1
            if count.month == 13:
                count.month = 1  #reset month
        count.day_year = 1  #reset day in year


oggi = date.today()
count.day_month = today.day_month = int(oggi.strftime("%d"))
count.month = today.month = int(oggi.strftime("%m"))
count.year = today.year = int(oggi.strftime("%Y"))
count.day_week = today.day_week = int(oggi.strftime("%w"))
count.day_year = today.day_year = int(oggi.strftime("%j"))
print("day =", today.day_month)
print("month =", today.month)
print("year =", today.year)
print("day of week =", today.day_week)
print("day of year =", today.day_year)
max = int(input("Inserire in quanti anni vuoi vedere venerdi 13: "))
NuovoCheck(max)