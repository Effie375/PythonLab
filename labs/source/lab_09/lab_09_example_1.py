# Δημιουργία λίστας
list = [1, 6, 3, 5, 4, 6]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

done = True
thesi = 0

for arithmos in list:
    if arithmos == key:
        print(thesi)
        done = False
    thesi += 1

if done is True:
    print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
