list = [9,7,8,9,3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

thesi = 0

for i in list:
    if i == key:
        print("Το %d βρίσκεται στη θέση %d." % (key,thesi))
    thesi += 1

k = 0

for i in list: 
    if i == key:
        k += 1

print("Το %d έχει εισαχθεί %d φορές." % (key,k))