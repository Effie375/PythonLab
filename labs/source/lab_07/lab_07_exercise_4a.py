leksi = input("Δώσε λέξη: ").lower().strip()

grammata = "abcdefghijklmnopqrstuvwxyz"

for letter in grammata:
    counter = 0
    for grammaLeksis in leksi:
        if grammaLeksis == letter:
            counter += 1
    if counter != 0:
        print(f"To γράμμα '{letter}' εμφανίστηκε {counter} φορές.")
