# Αρχικοποιούμε τις μεταβλητές
i = 0
synolo = 0

while i < 10:
    number = input("Δώσε αριθμό: ").strip()
    # Κάνουμε τον έλεγχο ορθότητας
    while not number.isdigit():
        number = input("Είπα δώσε αριθμό: ").strip()
    number = int(number)
    synolo = synolo + number
    i = i + 1

# Εκτυπώνουμε το αποτέλεσμα
print(f"Το σύνολο είναι: {synolo}")
