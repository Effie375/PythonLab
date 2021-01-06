import datetime


# Υπολογισμός χρονιάς που θα γίνει 100
def ipologismosXronias(xronon):
    twrinoEtos = datetime.datetime.today().year
    return twrinoEtos + 100 - xronon


# Διάβασμα από το χρήστη
onoma = input("Δώσε το όνομα σου: ").strip()

try:
    ilikia = int(input("Δώσε την ηλικία σου: ").strip())
except ValueError:
    print("Παρακαλώ δώσε ακέραιο αριθμό!")
else:
    ekatoXronwn = ipologismosXronias(ilikia)
    # Εκτύπωση αποτελέσματος
    print(f"{onoma} το {ekatoXronwn} θα είναι 100 ετών.")
