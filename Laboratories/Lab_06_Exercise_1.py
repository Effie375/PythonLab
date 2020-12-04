numbers = []

num = int(input("Δώσε έναν αριθμό: "))

while num != 0:
    numbers.append(num)
    num = int(input("Δώσε έναν αριθμό: "))  

counter = i = 0

key = int(input("Δώσε έναν αριθμό που αναζητάς: "))

while i < len(numbers):
    if key == numbers[i]:
        counter += 1
    i += 1

print("Ο αριθμός %d έχει εισαχθεί %d φορές." % (key, counter))