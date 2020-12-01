list = [5,7,8,9,3]

key = int(input("Dwse stoixeio pou anazitas: "))

found = False
i = 0 

while (i < len(list)) and (not found):
    if list[i] == key:
        thesi = i
        found = True
    else:
        i += 1


print("To %d vrisketai sti %d thesi." % (key, thesi))