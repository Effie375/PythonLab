numbers = []

num = int(input("Δώσε έναν αριθμό: ").strip())

while num != 0:
    numbers.append(num)
    num = int(input("Δώσε έναν αριθμό: ").strip())  

counter = i = 0

key = int(input("Δώσε έναν αριθμό που αναζητάς: ").strip())

while i < len(numbers):
    if key == numbers[i]:
        counter += 1
    i += 1

print(f"Ο αριθμός {key} έχει εισαχθεί {counter} φορές.")