stund=[]
grades=[]
i = 0 

while i < 20:
    stundets = input("Enter your Name: ")
    stund.append(stundets)
    grad = int(input("Enter your grade: "))
    grades.append(grad)
    i += 1

maxIndex = 0
i = 0

while i < len(grades):
    if grades[i] > grades[maxIndex]:
        maxIndex = i
    i += 1

print("%s won the competition with %d." % (stund[maxIndex], grades[maxIndex]) )






