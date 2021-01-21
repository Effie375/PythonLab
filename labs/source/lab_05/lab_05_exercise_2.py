# Αρχικοποίηση μεταβλητών
cont = True
lista = []

while cont:
    leksi = (input("Δώσε λέξη: "))
    thesi = int(input("Δώσε θέση: "))
    if thesi >= 0 and thesi <= len(lista):
        lista.insert(thesi, leksi)
    else:
        cont = False
        print("Τέλος εισαγωγής δεδομένων.")

# Εκτύπωση αποτελέσματος
print(lista)
