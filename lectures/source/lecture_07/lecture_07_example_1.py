list = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

thesi = 0

for i in list:
    if i == key:
        print(thesi)
    thesi += 1
