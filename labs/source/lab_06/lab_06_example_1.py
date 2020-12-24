i = 0
list = []

while i < 5:
    number = int(input("Δώσε αριθμό: "))
    list.append(number)
    i += 1

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
j = 0

while (j < len(list) and not found):
    if list[j] == key:
        thesi = j
        found = True
    j += 1

if found is True:
    print("Το στοιχείο βρίσκεται στη θέση", thesi)
else:
    print("Το στοιχείο που αναζητάς δεν υπάρχει.")
