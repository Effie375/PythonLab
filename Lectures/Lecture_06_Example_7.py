list = [5,7,8,9,3]
counter = 0

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

for k in list:
    if k == key:
        counter += 1

print(f"Ο αριθμός {key} έχει εισαχθεί {counter} φορές.")