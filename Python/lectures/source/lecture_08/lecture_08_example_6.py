# Αρχικοποίηση μεταβλητών
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]
MAX_ELEMENTS = 4

# Για MAX_ELEMENTS
for j in range(MAX_ELEMENTS):
    # Αρχικοποίηση μεταβλητής
    sumSthlhs = 0
    # Για MAX_ELEMENTS + 1
    for i in range(MAX_ELEMENTS + 1):
        sumSthlhs += lista[i][j]

    # Εκτύπωση το άθροισμα στήλης
    print("Άθροισμα στήλης: %d" % sumSthlhs)
