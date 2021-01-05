# Αρχικοποίηση μεταβλητών
megisto = 0
ls = []

# Εισαγωγή δεδομένων
number = int(input("Δώσε αριθμό: ").strip())

while number != 0:
    ls.append(number)
    if number > megisto:
        megisto = number
    number = int(input("Δώσε αριθμό: ").strip())
    i = 1

while i <= megisto:
    j = 0
    counter = 0
    while j < len(ls):
        if ls[j] == i:
            counter += 1
        j += 1
    if counter != 0:
        print(f"Ο αριθμός {i} εισήχθη {counter} φορές.")
    i += 1
