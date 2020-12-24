i = 0
synolo = 0

while i < 10:
    number = input("Δώσε αριθμό: ")
    while not number.isdigit():
        number = input("Δώσε αριθμό: ")
    number = int(number)
    synolo = synolo + number
    i = i + 1

print("Το σύνολο είναι:", synolo)
