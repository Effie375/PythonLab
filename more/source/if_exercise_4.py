car_displacement = int(input("Πόσα κυβικά έχει το αυτοκίνητό σου; "))

if car_displacement <= 1100:
    print("Ο φόρος αντιστοιχεί στα 100€.")
elif car_displacement <= 1400:
    print("Ο φόρος αντιστοιχεί στα 150€.")
elif car_displacement <= 2000:
    print("Ο φόρος αντιστοιχεί στα 225€.")
else:
    print("Ο φόρος αντιστοιχεί στα 600€.")
