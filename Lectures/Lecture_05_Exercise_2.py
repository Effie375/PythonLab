"""
Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. 
Να γίνει πρόγραµµα το οποίο θα διαβάζει τους βαθµούς
απολυτηρίου των µαθητών και θα εµφανίζει τους µαθητές 
που ο βαθµός τους είναι µεγαλύτερος από το µέσο όρο των αποφοίτων.
"""

stund = []
grades = []

i = 0
sum = 0

while i < 4:
    name = input("Enter your name: ")
    grad = int(input("Enter your grade: ")) 
    stund.append(name)
    grades.append(grad)
    sum += grad
    i += 1

# to check division with zero!
average = sum / i

i = 0

while i < len(grades):
    if grades[i] > average:
        print("Students who have high scores are:",stund[i])
    i += 1
    



