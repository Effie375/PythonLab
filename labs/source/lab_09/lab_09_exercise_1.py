list = []

for i in range(10):
    num = int(input("Δώσε στοιχεία: "))
    list.append(num)

key = int(input("Δώσε στοιχείο που αναζητάς: "))

done = True
thesi = 0

for i in list:
    if i == key:
        print(thesi)
        done = False
    thesi += 1

if done == True:
    print("To στοιχείο που αναζητάς δεν είναι στη λίστα.")
