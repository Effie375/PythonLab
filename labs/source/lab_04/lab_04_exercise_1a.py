first_dice = input("Δώσε το πρώτο ζάρι: ").strip()
second_dice = input("Δώσε το δεύτερο ζάρι: ").strip()

if first_dice.isdigit() and second_dice.isdigit():
    first_dice = int(first_dice)
    second_dice = int(second_dice)
    if (first_dice >= 1 and first_dice <= 6) and (second_dice >= 1 and second_dice <= 6):
        if ((first_dice == 4) and (second_dice == 4)):
            print("Ντόρτια.")
        elif ((first_dice == 1) and (second_dice == 2)) or ((first_dice == 2) and (second_dice == 1)):
            print("Ασσόδυο.")
        elif first_dice == second_dice:
            print("Διπλές.")
        else:
            print(f"Πρώτο ζάρι {first_dice}.")
            print(f"Δεύτερο ζάρι {second_dice}.")
    else:
        print("Λάθος!!")
else:
    print("Λάθος!!")
