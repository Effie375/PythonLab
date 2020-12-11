"""
Έστω ότι δημιουργείτε ένα πρόγραμμα το οποίο κρατά το όνομα επτά
παικτών.
Να δημιουργηθεί πίνακας players στον οποίο θα αποθηκεύονται τα
ονόματα των 7 παικτών.
Θα ταξινομεί τα ονόματα σε φθίνουσα σειρά και θα εμφανίζει τα
ονόματα των παικτών ταξινομημένα.
"""

players = []

for i in range(7):
    paiktis = input("Dwse onoma paikti: ")
    players.append(paiktis)
print(players)

for i in range(1,7):
    for j in range(6,i-1,-1):
        if players[j-1] < players[j]:
            temp = players[j-1]
            players[j-1]= players[j]
            players[j] = temp
print(players)