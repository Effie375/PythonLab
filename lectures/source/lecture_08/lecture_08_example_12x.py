lista = [[2, 3, 4, 1],
         [7, 8, 9, 2],
         [6, 5, 1, 8],
         [1, 2, 4, 3],
         [0, 4, 7, 5]]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print(f"Η λίστα πριν την ταξινόμηση είναι: {lista}")

for k in range(4):
    for i in range(1, 5):
        for j in range(4, i - 1, -1):
            if lista[j - 1][k] > lista[j][k]:
                # Swap lista
                temp = lista[j - 1][k]
                lista[j - 1][k] = lista[j][k]
                lista[j][k] = temp

# Εκτύπωση της λίστας μετά την ταξινόμηση
print(f"Η λίστα μετά την ταξινόμηση είναι: {lista}")
