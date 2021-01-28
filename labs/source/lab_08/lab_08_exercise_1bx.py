# Aρχικοποίηση μεταβλητών
MAX_ELEMENTS = 10
lista = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Ζητάμε από το χρήστη να δώσει στοιχείο και τα μετατρεπουμε σε ακέραια
    num = int(input("Δώσε στοιχείο: "))
    # Αποθηκεύουμε το στοιχείο στη λίστα
    lista.append(num)

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά στη λίστα
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

while(thesi < len(lista)) and done:
    if lista[thesi] == key:
        print("Το στοιχείο είναι στη θέση:", thesi)
        # Το done γίνεται False
        done = False
    # Αυξάνουμε τη μεταβλητή thesi κατά 1
    thesi += 1

# Εάν το done παραμείνει True
if done == True:
    print("To στοιχείο που αναζητάς δεν είναι στη λίστα.")
