MAX_ELEMENTS = 5
lista = []
i = 0

while i < MAX_ELEMENTS:
    num = int(input(f"Δώσε στοιχείο για την {i} θέση: ").strip())
    lista.append(num)
    i += 1

print(f"Η λίστα μας είναι: {lista}")
