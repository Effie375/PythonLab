'''
Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους
αριθμούς και να τους εμφανίζει ανάποδα από τη σειρά
που διαβάστηκαν.
'''

max_elements = 5 # --> 100
list = []

for item in range(max_elements):
    num = int(input("Δώσε έναν αριθμό: ").strip())
    list.append(num)

print(f"Η λίστα σου είναι:{list}")

for list in range(max_elements, 0, -1):
    print(list)
