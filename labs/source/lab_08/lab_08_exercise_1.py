# Αρχικοποίηση μεταβλητών
lista = []

for i in range(10):
    # Εισαγωγή στοιχείων
    num = int(input("Δώσε στοιχεία: "))
    lista.append(num)

# Εισαγωγή στοιχείων
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

for i in lista:
    if i == key:
        # Εκτύπωση θέσης
        print(thesi)
        done = False
    thesi += 1

if done == True:
    print("To στοιχείο που αναζητάς δεν είναι στη λίστα.")
