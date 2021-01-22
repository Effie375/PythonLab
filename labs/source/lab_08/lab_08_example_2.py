# Δημιουργία λίστας
lista = [9, 3, 7, 5, 2]

# Εκτύπωση της μη ταξινομημένης λίστας
print(f"H μη ταξινομημένη λίστα είναι: {lista}")

for i in range(1, 5):
    for j in range(4, i - 1, -1):
        if lista[j - 1] > lista[j]:
            # Swap lista
            temp = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = temp

# Εκτύπωση της ταξινομημένης λίστας
print(f"H ταξινομημένη λίστα είναι: {lista}")
