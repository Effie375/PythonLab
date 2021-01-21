# Αρχικοποίηση μεταβλητών
lista = []

for i in range(10):
    # Εισαγωγή δεδομένων
    lista.append(int(input("Δώσε αριθμό: ")))

# Εισαγωγή δεδομένων
num = int(input("Δώσε αριθμό για έλεγχο διαιρετέων: "))

for arithmos in lista:
    if arithmos % num == 0:
        # Εκτύπωση αριθμού
        print(arithmos)
