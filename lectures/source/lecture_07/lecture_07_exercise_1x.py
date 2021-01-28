def sort_function(plist):
    try:
        for index in range(len(plist) - 1):
            for j in range(len(plist) - 1, index, -1):
                if plist[j - 1] > plist[j]:
                    temp = plist[j - 1]
                    plist[j - 1] = plist[j]
                    plist[j] = temp
    except:
        print("Κάτι πήγε στραβά!")
        return 1
    else:
        return 0


# Αρχικοποίηση μεταβλητών
MAX_NUMBERS = 100
lista = []

for i in range(MAX_NUMBERS):
    num = input("Δώσε αριθμό: ").strip()
    # Έλεγχος ορθότητας
    while not num.isdigit():
        num = input("Είπα δώσε αριθμό: ").strip()
    # Μετατροπή αλφαριθμητικής τιμής σε ακέραια
    num = int(num)
    # Προσθήκη στοιχείου στη λίστα
    lista.append(num)


if not sort_function(lista):
    print(f"\nΟ μεγαλύτερος αριθμός είναι το {lista[len(lista) - 1]}.")
    print(f"Ο μικρότερος αριθμός είναι το {lista[0]}.")
