first_dice = input("Enter the first dice: ")
second_dice = input("Enter the second dice: ")

if first_dice.isdigit() and second_dice.isdigit():
    first_dice = int(first_dice)
    second_dice = int(second_dice)
    if (first_dice >= 1 and first_dice <= 6) and (second_dice >= 1 and second_dice <= 6):
        if ((first_dice == 4) and (second_dice == 4)):
            print("Dortia.")
        elif ((first_dice == 1) and (second_dice == 2)) or ((first_dice == 2) and (second_dice == 1)) :
            print("Assodyo.")
        elif first_dice == second_dice:
            print("Double.")
        else:
            print("First dice %d." % first_dice)
            print("Second dice %d." % second_dice)
    else:
        print("ERROR!!!!")
else: 
    print("ERROR!!")
