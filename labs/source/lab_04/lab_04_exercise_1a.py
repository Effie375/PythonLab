# Διαβάζουμε από το χρήστη να μας δώσει την 1η ζαριά
dice1 = input("Δώσε 1η ζαριά: ").strip()
# Διαβάζουμε από το χρήστη να μας δώσει την 2η ζαριά
dice2 = input("Δώσε 2η ζαριά: ").strip()

# Ελέγχουμε αν αυτό που έγραψε o χρήστης είναι νούμερα.
if dice1.isdigit() and dice2.isdigit():
    # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
    dice1 = int(dice1)
    dice2 = int(dice2)
    # Ελέγχουμε αν τα νούμερα των ζαριών ήταν μεταξύ 1 - 6.
    if (dice1 >= 1 and dice1 <= 6) and (dice2 >= 1 and dice2 <= 6):
        if ((dice1 == 4) and (dice2 == 4)):
            print("Ντόρτια.")
        elif (dice1 == 1 and dice2 == 2) or (dice1 == 2 and dice2 == 1):
            print("Ασσόδυο.")
        elif dice1 == dice2:
            print("Διπλές.")
        else:
            print(f"Πρώτο ζάρι {dice1}.")
            print(f"Δεύτερο ζάρι {dice2}.")
    else:
        print("Γιατί οι ζαριές είναι εκτός ορίων 1 και 6;")
else:
    print("Γιατί έγραψες λέξη;")
