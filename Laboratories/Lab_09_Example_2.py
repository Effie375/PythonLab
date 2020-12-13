list = [9,3,7,5,2]

print("H μη ταξινομημένη λίστα είναι: %s" % list)

for i in range(1,5):
    for j in range(4, i-1, -1):
        if list[j-1] > list[j]:
            temp = list[j-1]
            list[j-1] = list[j]
            list[j] = temp

print("H ταξινομημένη λίστα είναι: %s" % list)