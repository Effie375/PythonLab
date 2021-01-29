# Αρχικοποίηση των μεταβλητών
MAX_STUDENTS = 20
studentList = []
gradesList = []
maxIndex = 0
i = 0

# Για όσο το i είναι μικρότερο από το MAX_STUDENTS
while i < MAX_STUDENTS:
    # Ζητάμε από το χρήστη να δώσει το όνομά του
    student = input("Δώσε το όνομά σου: ").strip()
    # Απoθηκεύουμε το όνομα στη λίστα studentList
    studentList.append(student)
    # Ζητάμε από το χρήστη να δώσει το βαθμό του και το μετατρέπουμε σε ακέραιο
    grad = int(input("Δώσε τον βαθμό σου: ").strip())
    # Απoθηκεύουμε το βαθμό στη λίστα gradesList
    gradesList.append(grad)
    # Αυξάνουμε το i κατά 1
    i += 1

# Αρχικοποίηση μεταβλητής
i = 0

# Για όσο το i είναι μικρότερο από το μήκος της λίστας
while i < len(gradesList):
    if gradesList[i] > gradesList[maxIndex]:
        # Εκχωρούμε στο maxIndex το στιγμιαίο i
        maxIndex = i
    # Αυξάνουμε το i κατά 1
    i += 1

# Eκτύπωση όνοματος και βαθμού του νικητή
print(f"{studentList[maxIndex]} κέρδισε με βαθμό {gradesList[maxIndex]}.")
