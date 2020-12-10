maxThesi = thesi = 0
list = [5,7,8,9,3]

for item in list:
    if item > list[maxThesi]:
        maxThesi = thesi
    thesi +=1 

print("H maxThesi με τον 1ο τρόπο: %d" % maxThesi)

for i in range(len(list)):
    if list[i] > list[maxThesi]:
        maxThesi = i

print("H maxThesi με τον 2ο τρόπο: %d" % maxThesi)