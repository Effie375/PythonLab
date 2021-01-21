# Διαβάζουμε από το χρήστη έναν αριθμό
number = input("Δώσε έναν αριθμό (int): ").strip()

# Ελέγχουμε αν είναι ακέραιος αριθμός
if number.isdigit():
    # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
    number = int(number)
    # εάν ο αριθμός είναι 0
    if number == 0:
        print("Ο αριθμός είναι μηδέν.")
    # Αλλίως εάν ο αριθμός είναι άρτιος
    elif(number % 2) == 0:
        print("Ο αριθμός είναι άρτιος.")
    # Αλλίως είναι περιττός
    else:
        print("Ο αριθμός είναι περιττός.")
