list = [5,7,8,9,3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

for i in range(len(list)):
    if list[i] == key:
        thesi = i

print("Το %d βρίσκεται στη %d θέση." % (key, thesi))