# Διαβάζουμε έναν αριθμό και ελέγχουμε αν είναι 0 - 10
def readAndCheck():
    goon = True
    while goon:
        num = input("Δώσε αριθμό: ").strip()
        while not num.isdigit():
            num = input("Δώσε αριθμό: ").strip()
        num = int(num)
        if 0 <= num <= 10:
            goon = False
        return num


def sort(A):
    for i in range(1, len(A)):
        for j in range(len(A)-1, 0, -1):
            if A[j-1] > A[j]:
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
    return A


def readMarks():
    vathmoi = []
    for i in range(10):
        vathmoi.append(readAndCheck())
    return vathmoi


# MAIN
for i in range(10):
    vathmoi = readMarks()
    print(sort(vathmoi))
