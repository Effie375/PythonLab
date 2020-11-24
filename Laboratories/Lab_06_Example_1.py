"""
Να γραφεί ένα πρόγραμμα που διαβάζει 5 αριθμούς 
και θα τους αποθηκεύει σε μία λίστα. Στη συνέχεια 
θα διαβάζει έναν τυχαίο αριθμό και θα αναζητά αν 
ο αριθμός βρίσκεται στη λίστα και σε ποια θέση.
"""

i = 0 
numbers = []

while i < 5:
    num = int(input("Enter a number: "))
    numbers.append(num)
    i += 1

key = int(input("Enter a random number: "))

i = 0

while i < len(numbers):
    if key == numbers[i]:
        index = i
    i += 1

print("The number %d is in position: %d" % (key, index))