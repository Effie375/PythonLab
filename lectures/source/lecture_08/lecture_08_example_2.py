list = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

counter = 0

for i in list: 
    if i == key:
        counter += 1

print("Το %d έχει εισαχθεί %d φορές." % (key, counter))
