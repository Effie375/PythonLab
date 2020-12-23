names = []
marks = []
i = 0

while i < 20:
    onoma = input("Δώσε όνομα: ")
    vathmos = int(input("Δώσε βαθμό: "))
    names.append(onoma)
    marks.append(vathmos)
    i += 1

maxThesi = 0
i = 0

while i < len(names):
    if marks[i] > marks[maxThesi]:
        maxThesi = i
    i += 1

print(names[maxThesi])
