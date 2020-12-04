number = input("Δώσε το όνομά σου: ")

if number.isdigit():
    number = int(number)
    if (number >= 5) and (number <= 10):
        print("Πέρασες το μάθημα!")
    else:
        print("Κόπηκες, προσπάθησε ξανά!")
else:
    print("Μη έγκυρος αριθμός!")