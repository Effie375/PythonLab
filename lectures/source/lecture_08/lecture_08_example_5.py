# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
    # Αρχικοποίηση μεταβλητής
    sumGrammhs = 0
    # Για κάθε στοιχείο της υπολίστας
    for item in ypolista:
        # Αυξάνουμε το sumGrammhs κατά το item
        sumGrammhs += item

    # Εκτύπωση το άθροισμα γραμμής
    print("Άθροισμα γραμμής: %d" % sumGrammhs)
