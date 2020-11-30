list = [5,7,8,9,3]

key = int(input("Dwse stoixeio pou anazitas: "))

counter = 0

for k in list:
    if k == key:
        counter += 1

print("O aritmos %d exei eisaxthei %d fores." % (key, counter))
