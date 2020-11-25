temps = []

i = 0

while i < 30:
    tem = int(input("Enter a temperature:"))
    temps.append(tem)
    i += 1

max= 0
min = 0
i = 0

while i < len(temps):
    if temps[i] > temps[max]:
        max = i
    elif temps[i] < temps[min]:
        min = i
    i += 1

print("The lowest temperature was %d degrees on %d day." % (temps[min],min+1))
print("The highest temperature was %d degrees on %d day." % (temps[max],max+1))

