# Διαβάζουμε από το χρήστη έναν αριθμό
number = input("Δώσε έναν αριθμό: ").strip()

if number.isdigit():
    # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
    number = int(number)
    if number == 0:
        print("Μηδέν!")
    else:
        print("Άλλος αριθμός.")
