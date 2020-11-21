# Υπολογισμός αθροίσματος
sum = 0

weight = float(input("Enter the package weight in kg: "))

while weight > 0:
    sum += weight
    weight = float(input("Enter the package weight in kg: "))
    
print("The total weight is %d kg." % sum)