names = []
marks = []

for i in range(20):
    onoma = input("Δώσε όνομα: ")
    vathmos = int(input("Δώσε βαθμό: "))
    names.append(onoma)
    marks.append(vathmos)

maxThesi = 0

for i in range(len(names)):
    if marks[i] > marks[maxThesi]:
        maxThesi = i

print(names[maxThesi])
