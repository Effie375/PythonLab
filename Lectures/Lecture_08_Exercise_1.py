max_elements = 100
list = []

for i in range(max_elements):
    num = int(input("Δώσε στοιχείο: "))
    list.append(num)

for i in range(len(list)):
    for j in range(len(list)-1,i,-1):
        if list[j-1] > list[j]:
            temp = list[j-1]
            list[j-1] = list[j]
            list[j] = temp 

print("Ο ελάχιστος αριθμός της λίστας είναι: %s" % list[0])
print("Ο μέγιστος αριθμός της λίστας είναι: %s" % list[i])