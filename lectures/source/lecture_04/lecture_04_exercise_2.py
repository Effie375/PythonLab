AKSIA = 3000
weeks = 0
dosi = 20
tameio = 0

while tameio <= AKSIA:
    tameio += dosi
    weeks += 1
    dosi *= 2

print(weeks)

if tameio > AKSIA:
    print(f"Περίσσεψαν {tameio - AKSIA} Ευρώ.")
