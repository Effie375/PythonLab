ls = []

number = int(input("Δώσε αριθμό: "))

while number != 0:
    ls.append(number)
    number = int(input("Δώσε αριθμό: "))

counter = 0
i = 0

number = int(input("Δώσε αριθμό για μέτρηση: "))

while i < len(ls):
    if ls[i] == number:
        counter += 1
    i += 1

print("O αριθμός", number, "είσηχθη", counter, "φορές")
