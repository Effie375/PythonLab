list = [5,7,8,9,3]

megisto = list[0]
i = 0

while i < len(list):
    if list[i] > megisto:
        megisto = list[i]
    i += 1

print("O megistos aritmos einai to:", megisto)

elaxisto = list[0]
i = 0

while i < len(list):
    if list[i] < elaxisto:
        elaxisto = list[i]
    i += 1

print("O elaxistos aritmos einai to:", elaxisto)
