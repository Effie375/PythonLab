def readNums(x):
    lista = []
    for numbers in range(x):
        arithmos = float(input("Δώσε αριθμό: "))
        lista.append(arithmos)
    return lista

def mesosOros(x):
    athroisma = 0
    for stoixeio in x:
        athroisma += stoixeio
    mo = athroisma / len(x)
    return mo

def vathmologia(a):
    if a >= 5:
        print("Πέρασες")
    else:
        print("Κόπηκες")


stoixeio = int(input("Δώσε στοιχεία που περιέχει η λίστα: "))
numbers = readNums(stoixeio)
mesosoros = mesosOros(numbers)
print("Ο μέσος όρος είναι", mesosoros)
vathmologia(mesosoros)
