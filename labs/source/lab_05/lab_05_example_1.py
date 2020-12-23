i = 0
ls = []

while i < 10:
    number = int(input("Δώσε νούμερο: "))
    ls.append(number)
    i += 1

j = 9
new_ls = []

while j >= 0:
    new_ls.append(ls[j])
    j -= 1

print(new_ls)
