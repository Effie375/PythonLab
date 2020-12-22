key = int(input("Δώσε στοιχείο που αναζητάς: "))

done = True
thesi = 0

for i in list:
    if i == key:
        print(thesi)
        done = False
    thesi += 1

if done == True:
    print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
