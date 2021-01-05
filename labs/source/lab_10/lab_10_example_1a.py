# Αρχικοποίηση μεταβλητών
lista = []

for i in range(5):
    ypolista = []
    for j in range(10):
        # Εισαγωγή δεδομένων
        n = int(input("Δώσε αριθμό: ").strip())
        ypolista.append(n)
    lista.append(ypolista)

# Αρχικοποίηση μεταβλητών
meg_athroisma = 0

for ypolista in lista:
    athroisma = 0
    for i in ypolista:
        athroisma += i
    if athroisma > meg_athroisma:
        meg_athroisma = athroisma
        meg_lista = ypolista

# Εκτύπωση αποτελέσματος
print(meg_lista)
