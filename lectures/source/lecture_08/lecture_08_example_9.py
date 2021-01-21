ls = [[2, 3, 4, 1], [7, 3, 3, 9], [6, 5, 5, 8], [1, 9, 4, 1], [0, 4, 7, 4]]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

keyCounter = 0

for i in range(5):
    for j in range(4):
        if key == ls[i][j]:
            print(i, j)
            keyCounter += 1
print("Βρέθηκε %d φορές." % (keyCounter))
