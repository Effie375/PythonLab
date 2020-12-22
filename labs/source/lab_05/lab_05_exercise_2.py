cont=True
l=[]

while cont:
    leksi = (input("Δώσε λέξη: "))
    thesi = int(input("Δώσε θέση: "))
    if thesi>=0 and thesi<=len(l):
        l.insert(thesi,leksi)
    else:
        cont = False
        print("Τέλος εισαγωγής δεδομένων.")

print(l)
