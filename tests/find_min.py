list = [6, 5, 41, 2, 7]

index = 0
min = list[index]

while index < len(list):
    if list[index] < min:
        min = list[index]
    index += 1

print("The min element in the list is:", min)
