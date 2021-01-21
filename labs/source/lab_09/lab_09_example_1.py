# Αρχικοποίηση μεταβλητών
lista = []

for i in range(5):
    ypolista = []
    for j in range(10):
        # Εισαγωγή δεδομένων
        n = int(input("Δώσε αριθμό: "))
        ypolista.append(n)
    lista.append(ypolista)

# Αρχικοποίηση μεταβλητών
megAthroisma = 0

for ypolista in lista:
    athroisma = 0
    for i in ypolista:
        athroisma += i
    if athroisma > megAthroisma:
        megAthroisma = athroisma
        megLista = ypolista

# Εκτύπωση αποτελέσματος
print(megLista)
