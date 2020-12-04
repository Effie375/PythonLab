max_elements = 5
numbers = []
i = 0 

while i < max_elements:
    num = int(input("Δώσε έναν αριθμό: "))
    numbers.append(num)
    i += 1

key = int(input("Δώσε τον αριθμό που αναζητάτε: "))

flag = False
i = 0

while ((i < len(numbers)) and not flag):
    if key == numbers[i]:
        index = i
        flag = True
    i += 1

if flag:
    print("Ο αριθμός που αναζητάτε %d βρίσκεται στη θέση %d." % (key, index))
else:
    print("Ο αριθμός που αναζητάτε %d δε βρίσκεται στη λίστα." % key)