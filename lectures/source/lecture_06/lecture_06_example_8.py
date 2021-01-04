list = [3, 4, 1, 9, 4, 2]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0

while (i < len(list)) and (not found):
    if list[i] == key:
        thesi = i
        found = True
    i+=1

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
