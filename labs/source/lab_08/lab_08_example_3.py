# Αρχικοποίηση μεταβλητών
lista = []

for i in range(5):
    num = int(input("Δώσε στοιχείο: "))
    lista.append(num)

print("H μη ταξινομημένη λίστα είναι:", lista)

for i in range(1, 5):
    for j in range(4, i - 1, -1):
        if lista[j - 1] > lista[j]:
            temp = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = temp

# Εκτύπωση αποτελέσματος
print("H ταξινομημένη λίστα είναι:", lista)
