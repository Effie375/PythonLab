year = int(input("Δώσε ένα έτος: "))

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
    print("%d είναι δίσεκτο έτος." % year)
else:
    print("%d δεν είναι δίσεκτο έτος." % year)