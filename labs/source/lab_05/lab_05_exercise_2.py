cont = True
ls = []

while cont:
    leksi = (input("Δώσε λέξη: "))
    thesi = int(input("Δώσε θέση: "))
    if thesi >= 0 and thesi <= len(ls):
        ls.insert(thesi, leksi)
    else:
        cont = False
        print("Τέλος εισαγωγής δεδομένων.")

print(ls)
