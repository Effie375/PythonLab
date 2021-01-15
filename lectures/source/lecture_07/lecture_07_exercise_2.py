# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

while counter < MAX_ELEMENTS:
    name = input("Δώσε όνομα μαθητή: ")
    vathmos = int(input("Δώσε βαθμό: "))
    # Εισαγωγή στοιχείων στη λίστα των φοιτητών και των βαθμών
    names.append(name)
    vathmoi.append(vathmos)
    counter += 1


for i in range(len(vathmoi)-1):
    for j in range(len(vathmoi)-1, i,-1):
        if vathmoi[j-1] < vathmoi[j]:
            # Swap vathmous
            temp1 = vathmoi[j-1]
            vathmoi[j-1] = vathmoi[j]
            vathmoi[j] = temp1
            # Swap names
            temp2 = names[j-1]
            names[j-1] = names[j]
            names[j] = temp2

for i in range(BEST_FOITITES):
    print("Ο %dος καλύτερος είναι ο/η %s." % (i+1, names[i]))
