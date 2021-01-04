max_elements = 5
lista = []
i = 0

while i < max_elements:
    num = int(input(f"Δώσε στοιχείο για την {i} θέση: ").strip())
    lista.append(num)
    i += 1

print(f"Η λίστα μας είναι: {lista}")
