# Αρχικοποίηση μεταβλητών
athroisma = 0

# Διάβασμα από τον χρ΄ήστη και μετατροπ΄ή από str σε int
number = int(input("Δώσε αριθμό: "))

while number != 0:
    tel_pshfio = number % 10
    number = number // 10
    athroisma += tel_pshfio

# Eκτύπωση αποτελέσματος
print("Άθροισμα:", athroisma)
