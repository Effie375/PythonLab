list = [5,7,8,9,3]
maxThesi = i = 0

while i < len(list):
    if list[i] > list[maxThesi]:
        maxThesi = i
    i += 1

print(f"H max θέση είναι: {maxThesi}")