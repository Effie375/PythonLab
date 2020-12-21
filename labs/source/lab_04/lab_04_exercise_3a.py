year = int(input("Δώσε ένα έτος: ").strip())

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
    print(f"{year}είναι δίσεκτο έτος.")
else:
    print(f"{year} δεν είναι δίσεκτο έτος.")