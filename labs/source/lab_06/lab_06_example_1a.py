max_elements = 5
numbers = []
i = 0

while i < max_elements:
    num = int(input("Δώσε έναν αριθμό: ").strip())
    numbers.append(num)
    i += 1

key = int(input("Δώσε τον αριθμό που αναζητάτε: ").strip())

flag = False
i = 0

while ((i < len(numbers)) and not flag):
    if key == numbers[i]:
        index = i
        flag = True
    i += 1

if flag:
    print(f"Ο αριθμός που αναζητάτε {key} βρίσκεται στη θέση{index}.")
else:
    print(f"Ο αριθμός που αναζητάτε {key} δε βρίσκεται στη λίστα.")
