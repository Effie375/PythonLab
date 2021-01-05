number = input("Δώσε το όνομά σου: ").strip()

if number.isdigit():
    number = int(number)
    if (number >= 5) and (number <= 10):
        print(f"Πέρασες το μάθημα!")
    else:
        print(f"Κόπηκες, προσπάθησε ξανά!")
else:
    print(f"Μη έγκυρος αριθμός!")
