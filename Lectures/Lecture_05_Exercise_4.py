"""
Σε ένα διαγωνισµό πληροφορικής συµµετέχουν 20 µαθητές. Να γραφεί πρόγραµµα το οποίο 
θα αποθηκεύει σε µία λίστα τα ονόµατα των µαθητών και σε µία άλλη λίστα τους βαθµούς 
που έλαβε ο κάθε µαθητής στο διαγωνισµό. Το πρόγραµµα θα εµφανίζει το όνοµα του µαθητή 
που κέρδισε το διαγωνισµό.
"""

# Το πρόγραμμα δεν έχει τελειώσει ακόμα!

stund=[]
grades=[]

i = 0 

while i < 20:
    stundets = input("\nEnter your Name: ")
    stund.append(stundets)
    grad = int(input("Enter your grade: "))
    grades.append(grad)
    i += 1

max_index = 0
i = 0

while i < len(grades):
    if grades[i] > grades[max_index]:
        max_index = i
    i += 1

print("%s won the competition with an excellent %d." % (stund[max_index], grades[max_index]) )






