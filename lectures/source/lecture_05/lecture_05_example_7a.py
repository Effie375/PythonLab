list = [5, 7, 8, 9, 3]
counter = i = 0

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

while i < len(list):
    if list[i] == key:
        counter += 1
    i += 1

print(f"Το στοιχείο που αναζητάς έχει εισαχθεί {counter} φορές.")
