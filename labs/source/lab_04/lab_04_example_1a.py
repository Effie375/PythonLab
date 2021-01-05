# Διάβασμα από τον χρήστη
number = input("Δώσε έναν αριθμό: ").strip()

# Έλεγχος αν είναι αριθμός
if number.isdigit() is True:
    # Μετατροπή από str σε int
    number = int(number)
    if number == 0:
        print("Μηδέν")
    elif(number % 2) == 0:
        print("Άρτιος")
    else:
        print("Περιττός")
