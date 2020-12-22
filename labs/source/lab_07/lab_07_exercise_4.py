leksi = input("Δώσε λέξη: ")

leksi = leksi.lower()

grammata = "abcdefghijklmnopqrstuvwxyz"

for letter in grammata:
    counter = 0
    for grammaLeksis in leksi:
        if grammaLeksis == letter:
            counter += 1
    print("To γράμμα %s εμφανίστηκε %d φορές." % (letter, counter))
 counter = 0
