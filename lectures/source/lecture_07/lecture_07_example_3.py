list = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0

while (i < 5) and (found is False):
    if list[i] == key:
        thesi = i
        found = True
    i += 1

if found is True:
    print("Το %d βρίσκεται στη %d θέση." % (key, thesi))
else:
    print("Το %d δε βρίσκεται στη λίστα %s." % (key, list))
