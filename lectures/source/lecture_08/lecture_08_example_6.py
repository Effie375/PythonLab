Names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
Grades = [1, 2, 5, 7, 9]

for i in range(1, 5):
    for j in range(4, i-1, -1):
        if Grades[j-1] > Grades[j]:
            temp = Grades[j-1]
            Grades[j-1] = Grades[j]
            Grades[j] = temp
            temp2 = Names[j-1]
            Names[j-1] = Names[j]
            Names[j] = temp2
        if Grades[j-1] == Grades[j]:
            if Names[j-1] > Names[j]:
                temp3 = Names[j-1]
                Names[j-1] = Names[j]
                Names[j] = temp3

print(Names)
print(Grades)
