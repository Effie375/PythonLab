list = [1, 4, 6, 9, 7, 2]

megisto = list[0]
i = 0

while i < len(list):
    if list[i] > megisto:
        megisto = list[i]
    i += 1

print("Μέγιστο:", megisto)
