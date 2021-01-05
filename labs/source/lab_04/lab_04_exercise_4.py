# Αρχικοποίηση μεταβλητών
ginomeno = 0
arithmos = 1
flag = False

while arithmos != 0:
    # Διάβασμα από τον χρήστη
    arithmos = input("Δώσε αριθμό: ")
    # Έλεγχος ορθότητας
    while not arithmos.isdigit():
        arithmos = input("Δώσε σωστά αριθμό: ")
    # Μετατροπή από str σε int
    arithmos = int(arithmos)
    if flag is False and arithmos != 0:
        ginomeno = 1
        flag = True
    if arithmos != 0:
        ginomeno = ginomeno * arithmos

# Eκτύπωση αποτελέσματος
print("Γινόμενο:", ginomeno)
