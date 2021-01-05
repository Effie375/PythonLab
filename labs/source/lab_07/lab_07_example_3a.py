leksi = input("Δώσε λέξη: ").strip()

counter = 0

for gramma in leksi:
    if gramma == 'e':
        counter += 1

print(counter)
