# Εισαγωγή δεδομένων
record = float(input("Δώσε ρεκόρ αγώνων: "))

while record < 0 or record > 10:
    record = float(input("Δώσε το σωστό ρεκόρ αγώνων: "))

# Αρχικοποίηση μεταβλητών
jumps = []

for i in range(6):
    prospatheia = float(input("Δώσε προσπάθεια αθλητή: "))
    jumps.append(prospatheia)

# Αρχικοποίηση μεταβλητών
elaxisto = jumps[0]
megisto = jumps[0]

for i in jumps:
    if i < elaxisto:
        elaxisto = i
    if i > megisto:
        megisto = i

# Εκτύπωση αποτελεσμάτων
print("H χειρότερη προσπάθεια είναι:", elaxisto)

if megisto > record:
    print("Το νέο ρεκόρ είναι ", megisto)
elif record - megisto < 0.5:
    print("H καλύτερη προσπάθεια είναι:", megisto)
else:
    print("Oι προσπάθειες του αθλητή δεν ήταν ικανοποιητικές.")
