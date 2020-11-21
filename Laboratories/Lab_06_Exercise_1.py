"""
Να γραφεί πρόγραμμα το οποίο θα διαβάζει αριθμούς μέχρι να δωθεί 
ο αριθμός 0. Μετά θα δέχεται έναν αριθμό και θα εμφανίζει στον 
χρήστη πόσες φορές είχε εισαχθεί αυτός ο αριθμός. Να μην γίνει 
χρήση της μεθόδου count().
"""

# Το πρόγραμμα δεν έχει τελειώσει ακόμα!

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