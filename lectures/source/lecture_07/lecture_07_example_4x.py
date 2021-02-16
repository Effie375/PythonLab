# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print(f"Η λίστα μας πριν την ταξινόμηση είναι:{lista}")

for i in range(len(lista)):
    for j in range(len(lista) - 1, i, -1):
        if lista[j - 1] > lista[j]:
            # Swap lista
            temp = lista[j - 1]
            lista[j - 1] = lista[j]
            lista[j] = temp

# Εκτύπωση της λίστας μετά την ταξινόμηση
print(f"Η λίστα μας μετά την ταξινόμηση είναι:{lista}")
