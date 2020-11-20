list = []

num = 1

while num != 0:
    num = int(input("Dwse arithmo: "))
    if num != 0:
        list.append(num)

i = 0
counter = 0

key = int(input('Dwse stoixeio pou anazhtas: '))

while i < len(list):
    if list[i] ==  key:
        counter += 1
    i += 1

print("Plithos stoixeion: ", counter)