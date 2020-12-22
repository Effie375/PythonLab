list = [3, 4, 1, 9, 7, 2]
elaxisto = list[0]
i = 0

while i < len(list):
    if list[i] < elaxisto:
        elaxisto = list[i]
    i += 1

print("Ελάχιστο:", elaxisto)
