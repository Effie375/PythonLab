import my_functions as func

list = [8, 3, 70, 9, 4]

print("The max element in the list is:", func.find_max(list))
print("The min element in the list is:", func.find_min(list))

max_idx, max_value = func.find_max_idx_val(list)

print("\nThe index of the max element is: ", max_idx)
print("The max element in the list is:", max_value)

min_idx, min_value = func.find_min_idx_val(list)

print("\nThe index of the min element is: ", min_idx)
print("The min element in the list is:", min_value)

index = 0

while index < len(list):
    if func.check_num(list[index]):
        print("o arithmos %d einai monos!" % list[index])
    else:
        print("o arithmos %d einai zigos!" % list[index])
    index += 1
