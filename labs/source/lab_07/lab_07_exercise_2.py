# Αρχικοποίηση μεταβλητών
list = []

for i in range(10):
    # Εισαγωγή δεδομένων
    list.append(int(input("Δώσε αριθμό: ")))

# Εισαγωγή δεδομένων
num = int(input("Δώσε αριθμό για έλεγχο διαιρετέων: "))

for arithmos in list:
    if arithmos % num == 0:
        # Εκτύπωση αριθμού
        print(arithmos)
