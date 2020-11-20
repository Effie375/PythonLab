# Να γραφτεί πρόγραμμα σε γλώσσα Python που να διαβάζει
# το βάρος δεμάτων και να υπολογίζει και να εμφανίζει
# το συνολικό βάρος που διαβάστηκε. Το πρόγραμμα θα 
# τερματίζεται όταν πληκτρολογηθεί αριθμός μικρότερος 
# ή ίσος με το μηδέν.

sum = 0

weight = float(input("Enter the package weight in kg: "))

while weight > 0:
    sum += weight
    weight = float(input("Enter the package weight in kg: "))
    
print("The total weight is %d kg." % sum)