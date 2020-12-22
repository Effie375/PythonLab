temp = []
i = 0

while i < 30:
    num = int(input("Δώσε θερμοκρασία: "))
    temp.append(num)
    i += 1

maxThesi = 0
minThesi = 0

i = 0

while i < len(temp):
    if temp[i] < temp[minThesi]:
        minThesi = i
    if temp[i] > temp[maxThesi]:
        maxThesi = i
    i += 1

print("Η μέγιστη θερμοκρασία είναι", temp[maxThesi , "την ημέρα", maxThesi)

print("Η ελάχιστη θερμοκρασία είναι", temp[minThesi , "την ημέρα", minThesi)
