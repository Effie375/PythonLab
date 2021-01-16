ls = [[1, 2, 3], [1, 1, 1], [2, 3, 4]]
A = [1, 2, 5]
B = []

for key in A:
    counter = 0
    for ypolista in ls:
        for i in ypolista:
            if i == key:
                counter += 1
    B.append(counter)

print(B)
