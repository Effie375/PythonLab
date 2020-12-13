list = [9,3,7,5,2] 

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
thesi = 0

for i in list:
    if i == key:
        print("Το %d βρίσκεται στη %d θέση της λίστας." % (key, thesi))
        found = True
    thesi += 1 

if found == False:
    print("Το %d δε βρίσκεται στη λίστα." % key)