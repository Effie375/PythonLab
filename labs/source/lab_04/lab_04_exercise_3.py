# Διάβασμα έτους
etos = int(input("Δώσε έτος: "))

# Αν διαιρείται με 4 είναι δίσεκτο
if etos % 4 == 0:
    # Εκτός και αν διαιρείται και με 100
    if etos % 100 == 0:
        # Aλλα και σε αυτήν την περίπτωση αν διαιρείται με 400 είναι δίσεκτο
        if etos % 400 == 0:
            disekto = True
        else:
            disekto = False
    else:
        disekto = True
else:
    disekto = False

# Eκτύπωση αποτελέσματος
if disekto:
    print("Είναι δίσκετο")
else:
    print("Δεν είναι δίσεκτο")
