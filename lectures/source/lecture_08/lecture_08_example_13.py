# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 8, 9, 2],
         [6, 5, 1, 8],
         [1, 2, 4, 3],
         [0, 4, 7, 5]]

# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 4
sum1 = 0
sum2 = 0

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Για MAX_ELEMENTS
    for j in range(MAX_ELEMENTS):
        # Εάν το στιγμιαίο i είναι ίσο με το στιγμιαίο j
        if i == j:
            sum1 += lista[i][j]
        # Εάν το άθροισμα το i και j είναι ίσο με 3
        if i + j == 3:
            sum2 += lista[i][j]

# Εκτύπωση του sum1 και sum2
print(sum1, sum2)
