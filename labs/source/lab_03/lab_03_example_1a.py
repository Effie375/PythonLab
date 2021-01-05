# Διάβασμα από τον χρήστη
number = input("Δώσε έναν αριθμό: ").strip()

if number.isdigit() is True:
    # Μετατροπή από str σε int
    number = int(number)
    if number == 0:
        print("Μηδέν!")
    else:
        print("Άλλος αριθμός.")
