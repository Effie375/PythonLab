year = int(input("Δώσε ένα έτος: ").strip())

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year} είναι δίσεκτο έτος.")
else:
    print(f"{year} δεν είναι δίσεκτο έτος.")
