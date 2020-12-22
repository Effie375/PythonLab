i = 0
l = []

while i < 10:
    number = int(input("Δώσε νούμερο: "))
    l.append(number)
    i += 1

j = 9
new_l = []

while j >= 0:
    new_l.append(l[j])
    j -= 1

print(new_l)
