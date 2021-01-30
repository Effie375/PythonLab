# Δημιουργία λιστών
lista1 = [[1, 2, 3],
          [1, 1, 1],
          [2, 3, 4]]
lista2 = [1, 2, 5]
# Δημιούργια κενής λίστας
lista3 = []

# Για κάθε στοιχείο της lista2
for key in lista2:
    # Αρχικοποίηση μεταβλητής
    counter = 0
    # Για κάθε υπολίστας της lista1
    for ypolista in lista1:
        # Για κάθε στοιχείο της υπολίστας
        for i in ypolista:
            # Εάν το στιγμιαίο στοιχείο της υπολίστας είναι ίσο με το key
            if i == key:
                # Αυξάνουμε τον counter κατά 1
                counter += 1
    # Αποθηκεύουμε τον counter στη lista3
    lista3.append(counter)

# Eκτυπώση της lista3
print(lista3)
