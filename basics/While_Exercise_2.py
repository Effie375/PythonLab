counter = sum = 0

age = int(input("Δώσε την ηλικία σου: ").strip())

while age > 0:
    counter += 1
    sum += age
    age = int(input("Δώσε την ηλικία σου: ").strip())

if counter != 0:
    average = sum / counter
    print(f"Ο μέσος όρος των ηλικιών είναι {average:.1f}.")
else:
    print(f"Δεν έχετε δώσει καμία ηλικία.")
