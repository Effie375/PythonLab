list = [5, 7, 8, 9, 3]
i = 0

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

while i < len(list):
    if key == list[i]:
        thesi = i
    i += 1
    
print(f"Η θέση βρίσκεται: {thesi}")
