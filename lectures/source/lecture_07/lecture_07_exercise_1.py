MAX_NUMBERS = 100
list = []

for i in range(MAX_NUMBERS):
    num = int(input("Δώσε αριθμό: "))
    list.append(num)


for index in range(len(list)-1):
    for j in range(len(list)-1, index, -1):
        if list[j-1] > list[j]:
            temp = list[j-1]
            list[j-1] = list[j]
            list[j] = temp


print("\nΟ μεγαλύτερος αριθμός είναι το", list[len(list)-1])
print("Ο μικρότερος αριθμός είναι το", list[0])
