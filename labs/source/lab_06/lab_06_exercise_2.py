megisto = 0
ls = []

number = int(input("Δώσε αριθμό: "))

while number != 0:
    ls.append(number)
    if number > megisto:
        megisto = number
    number = int(input("Δώσε αριθμό: "))

    i = 1

while i <= megisto:
    j = 0
    counter = 0
    while j < len(ls):
        if ls[j] == i:
            counter += 1
        j += 1

    if counter != 0:
        print("Ο αριθμός", i, "εισήχθη", counter, "φορές.")
    i += 1
