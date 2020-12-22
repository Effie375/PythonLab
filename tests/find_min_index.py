list = [100, 2, 10, 5]

min_index = 0
index = 0

while index < len(list):
    if list[index] < list[min_index]:
        min_index = index
    index += 1

print("The index of the min element is: ", min_index)
print("The min element in the list is:", list[min_index])
