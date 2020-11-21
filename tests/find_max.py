list = [8,45,7,9,4]

index = 0
max = list[index]

while index < len(list):
    if list[index] > max:
        max = list[index]
    index += 1

print("The max element in the list is:", max)