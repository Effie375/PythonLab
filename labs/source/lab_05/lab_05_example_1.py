# Αρχικοποίηση μεταβλητών
list = []
i = 0

while i < 10:
    number = int(input("Δώσε έναν αριθμό: "))
    list.append(number)
    i += 1

# Αρχικοποίηση μεταβλητών
newList = []
j = 9

while j >= 0:
    newList.append(list[j])
    j -= 1

# Εκτύπωση αποτελεσμάτων
print("Η νέα λίστα είναι:", newList)
