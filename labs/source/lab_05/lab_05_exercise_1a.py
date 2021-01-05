# Αρχικοποίηση μεταβλητών
odd = even = sum = i = 0
max_elements = 10
list = []

# Δίαβασμα πίνακα
while i < max_elements:
    number = int(input("Δώσε αριθμό: ").strip())
    list.append(number)
    sum += number
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

# Εκτύπωση αποτελεσμάτων
print(f"Tο άθροισμα των αριθμών είναι {sum}.")
print(f"Tο πλήθος των περιττών είναι {odd}. ")
print(f"Το πλήθος των άρτιων είναι {even}.")

# Αρχικοποίηση μεταβλητών
megistos = elaxistos = i = 0

# Yπολογισμός ζητούμενων
while i < 10:
    if list[i] > list[megistos]:
        megistos = i
    elif list[i] < list[elaxistos]:
        elaxistos = i
    i += 1

# Υπολογισμός διαφοράς
diafora = list[megistos] - list[elaxistos]

# Εκτύπωση αποτελέσματος
print(f"H διαφορά max και min είναι {diafora}.")
