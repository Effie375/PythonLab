# Αρχικοποίηση μεταβλητών
athroisma = 0

# Διάβασμα από τον χρ΄ήστη και μετατροπ΄ή από str σε int
number = int(input("Δώσε έναν αριθμό: ").strip())

while number:
    tel_pshfio = number % 10
    number /= 10
    athroisma += tel_pshfio

# Eκτύπωση αποτελέσματος
print(f"Το άθροισμα των ψηφίων είναι {athroisma}.")
