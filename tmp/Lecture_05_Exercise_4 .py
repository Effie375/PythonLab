"""
Σε ένα διαγωνισµό πληροφορικής συµµετέχουν 20 µαθητές. Να γραφεί πρόγραµµα το οποίο 
θα αποθηκεύει σε µία λίστα τα ονόµατα των µαθητών και σε µία άλλη λίστα τους βαθµούς 
που έλαβε ο κάθε µαθητής στο διαγωνισµό. Το πρόγραµµα θα εµφανίζει το όνοµα του µαθητή 
που κέρδισε το διαγωνισµό.
"""

stund=[]
grades=[]

while (len(stund) and len(grades)) <= 2:
    stundets = input("\nEnter your Name: ")
    stund.append(stundets)
    grad = int(input("Enter your grade: "))
    grades.append(grad)

# print(stund, grades)




