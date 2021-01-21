# Αρχικοποίηση μεταβλητών
megisto = 0
lista = []

# Εισαγωγή δεδομένων
number = int(input("Δώσε αριθμό: "))

while number != 0:
    lista.append(number)
    if number > megisto:
        megisto = number
    number = int(input("Δώσε αριθμό: "))
    i = 1

while i <= megisto:
    j = 0
    counter = 0
    while j < len(lista):
        if lista[j] == i:
            counter += 1
        j += 1
    if counter != 0:
        print("Ο αριθμός", i, "εισήχθη", counter, "φορές.")
    i += 1
