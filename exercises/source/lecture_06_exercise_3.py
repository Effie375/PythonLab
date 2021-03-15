# Aρχικοποίηση μεταβλητών
MAX_ELEMENTS = 30
temp = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
    # Ζητάμε απο το χρήστη να δώσει θερμοκρασία και τη μετατρέπουμε σε ακέραιο
    num = int(input("Δώσε θερμοκρασία: "))
    # Αποθηκεύουμε τη θερμοκρασία στη λίστα temp
    temp.append(num)

# Aρχικοποίηση μεταβλητών
maxThesi = 0
minThesi = 0

# Για όσο είναι το μήκος της λίστας
for i in range(len(temp)):
    if temp[i] < temp[minThesi]:
        # Εκχωρούμε στη minThesi το i
        minThesi = i
    if temp[i] > temp[maxThesi]:
        # Εκχωρούμε στη maxThesi το i
        maxThesi = i

# Eκτύπωση της max θερμοκρασίας και ήμερα
print("Η max θερμοκρασία είναι %d την ημέρα %d" % (temp[maxThesi], (maxThesi + 1)))
# Eκτύπωση της min θερμοκρασίας και ήμερα
print("Η min θερμοκρασία είναι %d την ημέρα %d" % (temp[minThesi], (minThesi + 1)))
