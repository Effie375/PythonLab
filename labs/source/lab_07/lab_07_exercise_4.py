leksi = input("Δώσε λέξη: ").lower()

grammata = "abcdefghijklmnopqrstuvwxyz"

for letter in grammata:
    counter = 0
    for grammaLeksis in leksi:
        if grammaLeksis == letter:
            counter += 1
    if counter != 0:
        print("To γράμμα <%s> εμφανίστηκε %d φορές." % (letter, counter))
