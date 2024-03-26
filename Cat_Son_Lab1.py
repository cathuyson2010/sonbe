def gregorian_calendar(year):
    if (year % 4 == 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))

if gregorian_calendar(year):
    print(f"{year} - leap year")
else:
    print(f"{year} - not a leap year")
