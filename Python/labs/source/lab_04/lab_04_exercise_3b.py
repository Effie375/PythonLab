# Διαβάζουμε το έτος που εισάγει ο χρήστης
etos = int(input("Δώσε έτος: "))

# Ελέγχουμε εάν το έτος αυτό είναι δίσεκτο
if (etos % 4 == 0) and (etos % 100 != 0) or (etos % 400 == 0):
    print("Το %d είναι δίσεκτο έτος." % etos)
else:
    print("Το %d δεν είναι δίσεκτο έτος." % etos)