list = [5,7,8,9,3]

maxThesi = 0
i = 0

while i < len(list):
    if list[i] > list[maxThesi]:
        maxThesi = i
    i += 1

print("H max thesi einai:", maxThesi)
