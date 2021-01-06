# Διαβάζουμε από το χρήστη έναν αριθμό
number = input("Δώσε έναν αριθμό: ").strip()

# Ελέγχουμε αν είναι αριθμός
if number.isdigit() is True:
   # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
    number = int(number)
    if number == 0:
        print("Μηδέν")
    elif(number % 2) == 0:
        print("Άρτιος")
    else:
        print("Περιττός")
