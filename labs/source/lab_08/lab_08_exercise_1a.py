# Αρχικοποίηση μεταβλητών
list = []

for i in range(10):
    # Εισαγωγή στοιχείων
    num = int(input("Δώσε στοιχεία: ").strip())
    list.append(num)

# Εισαγωγή στοιχείων
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητών
done = True
thesi = 0

for i in list:
    if i == key:
        # Εκτύπωση θέσης
        print(thesi)
        done = False
    thesi += 1

if done == True:
    print("To στοιχείο που αναζητάς δεν είναι στη λίστα.")
