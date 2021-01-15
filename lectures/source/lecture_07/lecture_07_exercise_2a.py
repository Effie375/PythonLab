def sort_function(pnames, pvathmoi):
    try:
        for i in range(len(pvathmoi)-1):
            for j in range(len(pvathmoi)-1, i,-1):
                if pvathmoi[j-1] < pvathmoi[j]:
                    # Swap vathmous
                    temp1 = pvathmoi[j-1]
                    pvathmoi[j-1] = pvathmoi[j]
                    pvathmoi[j] = temp1
                    # Swap names
                    temp2 = pnames[j-1]
                    pnames[j-1] = pnames[j]
                    pnames[j] = temp2
        return 0
    except:
        return 1


# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

while counter < MAX_ELEMENTS:
    name = input("Δώσε όνομα μαθητή: ").strip()
    vathmos = input("Δώσε βαθμό: ").strip()
    # Έλεγχος ορθότητας
    while not vathmos.isdigit():
        vathmos = input("Είπα δώσε βαθμό: ").strip()
    # Μετατροπή αλφαριθμητικής τιμής σε ακέραια
    vathmos = int(vathmos)
    # Εισαγωγή στοιχείων στη λίστα των φοιτητών και των βαθμών
    names.append(name)
    vathmoi.append(vathmos)
    counter += 1


if not sort_function(names, vathmoi):
    for i in range(BEST_FOITITES):
        print(f"Ο {i+1}ος καλύτερος είναι ο/η {names[i]}.")
else:
    print("Κάτι πήγε στραβά!")
