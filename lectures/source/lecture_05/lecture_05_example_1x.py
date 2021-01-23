MAX_ELEMENTS = 5
lista = []
i = 0

while i < MAX_ELEMENTS:
    num = int(input("Δώσε στοιχείο για την θέση %d: " % i))
    lista.append(num)
    i += 1

print("Η λίστα μας είναι: %s" % lista)
