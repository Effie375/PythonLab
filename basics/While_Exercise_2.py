counter = sum = 0

age = int(input("Δώσε την ηλικία σου: "))

while age > 0:
    counter += 1
    sum += age
    age = int(input("Δώσε την ηλικία σου: "))
  
if counter != 0:
    average = sum / counter
    print("Ο μέσος όρος των ηλικιών είναι %.1f." % average)
else:
    print("Δε έχετε δώσει καμία ηλικία.")
