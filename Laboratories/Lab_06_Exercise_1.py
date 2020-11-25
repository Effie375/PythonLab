"""
Να γραφεί πρόγραμμα το οποίο θα διαβάζει αριθμούς μέχρι να δωθεί 
ο αριθμός 0. Μετά θα δέχεται έναν αριθμό και θα εμφανίζει στον 
χρήστη πόσες φορές είχε εισαχθεί αυτός ο αριθμός. Να μην γίνει 
χρήση της μεθόδου count().
"""

num = int(input("Enter a number: "))
numbers = []

while num != 0:
    numbers.append(num)
    num = int(input("Enter a number: "))
    

i = 0
counter = 0

key = int(input("Enter the number you are looking for: "))

while i < len(numbers):
    if key == numbers[i]:
        counter += 1
    i += 1

print("Τhe number %d has been entered %d times." % (key, counter))
