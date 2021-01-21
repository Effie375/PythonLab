# Διαβάζουμε έναν αριθμό και ελέγχουμε αν είναι 0 - 10
def readAndCheck():
    good = True
    while good:
        num = input("Δώσε αριθμό: ")
        while not num.isdigit():
            num = input("Δώσε αριθμό: ")
        num = int(num)
        if 0 <= num <= 10:
            good = False
        return num


def sort(listaP):
    for i in range(1, len(listaP)):
        for j in range(len(listaP) - 1, 0, -1):
            if listaP[j - 1] > listaP[j]:
                temp = listaP[j - 1]
                listaP[j - 1] = listaP[j]
                listaP[j] = temp
    return listaP


def readMarks():
    vathmoi = []
    for i in range(10):
        vathmoi.append(readAndCheck())
    return vathmoi


# MAIN
for i in range(10):
    vathmoi = readMarks()
    print(sort(vathmoi))
