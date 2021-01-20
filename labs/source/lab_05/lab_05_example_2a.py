# Αρχικοποίηση μεταβλητών
max_elements = 5
numbers = []
i = 0

while i < max_elements:
    num = int(input("Δώσε έναν αριθμό: ").strip())
    numbers.append(num)
    i += 1

# Εισαγωγή δεδομένων
key = int(input("Δώσε τον αριθμό που αναζητάτε: ").strip())

# Αρχικοποίηση μεταβλητών
flag = False
i = 0

while ((i < len(numbers)) and not flag):
    if key == numbers[i]:
        index = i
        flag = True
    i += 1

# Εκτύπωση αποτελεσμάτων
if flag == True:
    print(f"Ο αριθμός που αναζητάς {key} βρίσκεται στη θέση {index}.")
else:
    print(f"Ο αριθμός που αναζητάς {key} δεν βρίσκεται στη λίστα.")
