list = [100,200,10,5]

max_index = 0
index = 0

while index < len(list):
    if list[index] > list[max_index]:
        max_index = index
    index += 1

print("The index of the max element is: ", max_index)
print("The max element in the list is:", list[max_index])