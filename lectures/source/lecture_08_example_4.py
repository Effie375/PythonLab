# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Αρχικοποίηση μεταβλητών
megistoX = 0
megistoY = 0

# Για όσο είναι το μήκος της λίστας
for x in range(len(lista)):
    # Για όσο είναι το μήκος της υπολίστας
    for y in range(len(lista[x])):
        if lista[x][y] > lista[megistoX][megistoY]:
            megistoX = x
            megistoY = y

# Εκτύπωση το megistoX
print(megistoX)
# Εκτύπωση το megistoY
print(megistoY)
