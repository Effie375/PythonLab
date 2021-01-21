# Αρχικοποίηση μεταβλητών
lista = []

number = int(input("Δώσε αριθμό: "))

while number != 0:
    lista.append(number)
    number = int(input("Δώσε αριθμό: "))

# Αρχικοποίηση μεταβλητών
counter = 0
i = 0

# Εισαγωγή δεδομένων
number = int(input("Δώσε αριθμό για μέτρηση: "))

while i < len(lista):
    if lista[i] == number:
        counter += 1
    i += 1

# Εκτύπωση αποτελεσμάτων
print("O αριθμός", number, "είσηχθη", counter, "φορές")
