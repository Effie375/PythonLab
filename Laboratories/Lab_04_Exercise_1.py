"""
Να γραφεί πρόγραμμα το οποίο:
* Θα διαβάζει το αποτέλεσμα 2 ζαριών.
* Θα ελέγχει αν ο χρήστης εισήγαγε σωστά νούμερα (1-6), αλλιώς θα 
εμφανίζει μήνυμα λάθους και θα τερματίζει.
* Αν τα ζάρια ήταν τεσσάρια, θα τυπώνει «Ντορτια».
* Αν τα ζάρια ήταν 1 και 2, θα τυπώνει «Ασσόδυο».
* Αν τα ζάρια ήταν διπλά, θα τυπώνει «Διπλές» και το αποτέλεσμα.
* Αλλιώς θα τυπώνει το αποτέλεσμα της ζαριάς.
"""

# Το πρόγραμμα δεν έχει τελειώσει ακόμα!

first_dice = int(input("Enter the first dice: "))
second_dice = int(input("Enter the second dice: "))


if (first_dice >= 1 and first_dice <= 6) and (second_dice >= 1 and second_dice <= 6):
    if first_dice and second_dice == 4:
    print("Dortia.")
    elif (first_dice and second_dice) == (1 and 2):
        print("Assodo.")
    elif first_dice == second_dice:
        print("Double.")
    else:
    print("First dice %d." % first_dice)
    print("Second dice %d." % second_dice)
else:
    print(ERROR!!!!)
    





