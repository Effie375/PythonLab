list = [5,7,8,9,3]

key = int(input("Dwse stoixeio pou anazitas: "))

found = False
i = 0 

while (i < len(list)) and (not found):
    if list[i] == key:
        thesi = i
        found = True
    else:
        i += 1

"""
Δεν μπορεί να μετατραπεί σε FOR,
καθώς δεν γνωρίζουμε πόσες επαναλήψεις
πρέπει να γίνουν.
"""

print("To %d vrisketai sti %d thesi." % (key, thesi))