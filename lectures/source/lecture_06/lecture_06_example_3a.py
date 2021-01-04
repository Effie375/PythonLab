list = [5, 7, 8, 9, 3]

megisto = list[0]
elaxisto = list[0]

for item in list:
    if item > megisto:
        megisto = item

for item in list:
    if item < elaxisto:
        elaxisto = item

print(f"Μέγιστο: {megisto}")
print(f"Ελάχιστο: {elaxisto}")
