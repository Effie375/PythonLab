list = []
i = 0

while i < 10:
    number = int(input("Δώσε νούμερο: "))
    list.append(number)
    i += 1

print(list)

new_list = []

j = 9

while j >= 0:
    new_list.append(list[j])
    j -= 1

print(new_list)
