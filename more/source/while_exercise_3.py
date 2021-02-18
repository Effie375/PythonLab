counter = 0
megisto = 0

age = int(input("Δώσε την ηλικία σου: "))

while age > 0:
    counter += 1
    megisto += age
    age = int(input("Δώσε την ηλικία σου: "))

if counter != 0:
    average = megisto / counter
    print("Ο μέσος όρος των ηλικιών είναι %.1f." % average)
else:
    print("Δεν έχετε δώσει καμία ηλικία.")
