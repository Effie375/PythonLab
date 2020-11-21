year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else: 
        leap_year = True    

else:
     leap_year = False

if leap_year:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")