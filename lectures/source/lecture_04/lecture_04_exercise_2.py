aksia = 3000
weeks = 0
dosi = 20
tameio = 0

while tameio <= aksia:
    tameio += dosi
    weeks += 1
    dosi *= 2

print(weeks)

if tameio > aksia:
    print(f"Περίσσεψαν {tameio - aksia} Ευρώ.")
