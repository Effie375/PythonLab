def readMarks(N):
    marks = []
    for i in range(N):
        mark = int(input("Δώσε βαθμό: "))
        marks.append(mark)
    return marks


def getMax(A):
    megisto = 0
    for i in A:
        if i > megisto:
            megisto = i
    return megisto


def getMO(A):
    souma = 0
    for i in A:
        souma += i
    return souma / len(A)


plithos = int(input("Πόσοι δώσανε το μάθημα:"))

vathmoi = readMarks(plithos)

print("Μέγιστος: ", getMax(vathmoi))
print("Mέσος όρος: ", getMO(vathmoi))
