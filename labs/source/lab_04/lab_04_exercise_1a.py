dice1 = input("Δώσε το πρώτο ζάρι: ").strip()
dice2 = input("Δώσε το δεύτερο ζάρι: ").strip()

if dice1.isdigit() and dice2.isdigit():
    dice1 = int(dice1)
    dice2 = int(dice2)
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
        print("Λάθος!!")
else:
    print("Λάθος!!")
