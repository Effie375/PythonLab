'''
Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους 
αριθμούς και να τους εμφανίζει ανάποδα από τη σειρά 
που διαβάστηκαν.
'''

# To πρόγραμμα δεν έχει τελείωσει.

list = []

for item in range(100):
    num = int(input("Enter a number: "))
    list.append(num)
print("Your list is:", list)
