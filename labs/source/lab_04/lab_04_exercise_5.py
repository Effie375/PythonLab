# Αρχικοποίηση μεταβλητών
athroisma = 0

# Διάβασμα από τον χρ΄ήστη και μετατροπ΄ή από str σε int
number = int(input("Δώσε αριθμό: "))

while number != 0:
    telPshfio = number % 10
    number = number // 10
    athroisma += telPshfio

# Eκτύπωση αποτελέσματος
print("Άθροισμα:", athroisma)
