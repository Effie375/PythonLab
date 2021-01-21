# Αρχικοποίηση μεταβλητών
eksamina = []

for i in range(8):
    vathmoi = []
    for j in range(6):
        # Εισαγωγή δεδομένων
        vathmos = float(input("Δώσε βαθμό: "))
        vathmoi.append(vathmos)
eksamina.append(vathmoi)

# Εισαγωγή δεδομένων
arEksaminou = int(input("Ποιο εξάμηνο θες να δείς;"))

# Aφαιρούμε 1 γιατί ο χρήστης θα δώσει π.χ. 1 για το πρώτο εξάμηνο
# ενώ αυτό είναι στη θέση 0.
eksamino = eksamina[arEksaminou-1]

# Αρχικοποίηση μεταβλητών
souma = 0
perasmena = 0

for mathima in eksamino:
    souma += mathima
    if mathima >= 5:
        perasmena += 1

# Εκτύπωση αποτελεσμάτων
print("Ο μέσος όρος είναι: ", souma/len(eksamino))
print("Πέρασες: ", perasmena)
