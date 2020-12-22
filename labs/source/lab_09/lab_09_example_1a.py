list = [9,3,7,5,2] 

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

found = False
thesi = 0

for i in list:
    if i == key:
        print(f"Το {key} βρίσκεται στη {thesi} θέση της λίστας.")
        found = True
    thesi += 1 

if found == False:
    print(f"Το {key} δε βρίσκεται στη λίστα.")
