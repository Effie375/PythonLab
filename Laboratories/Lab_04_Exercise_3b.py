year = int(input("Δώσε ένα έτος: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("%d είναι δίσεκτο έτος." % year)
else: 
    print("%d δεν είναι δίσεκτο έτος." % year)