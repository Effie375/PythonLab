# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 8, 9, 2],
         [6, 5, 1, 8],
         [1, 2, 4, 3],
         [0, 4, 7, 5]]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print("Η λίστα πριν την ταξινόμηση είναι: %s" % lista)

for k in range(5):
    for i in range(1, 4):
        for j in range(3, i - 1, -1):
            if lista[k][j - 1] > lista[k][j]:
                # Swap lista
                temp = lista[k][j - 1]
                lista[k][j - 1] = lista[k][j]
                lista[k][j] = temp

# Εκτύπωση της λίστας μετά την ταξινόμηση
print("Η λίστα μετά την ταξινόμηση: %s" % lista)
