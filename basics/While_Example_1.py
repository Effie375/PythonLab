counter = 0 
sum = 0
sal = float(input("Enter a salary: "))

while sal > 0:
    counter += 1
    sum += sal
    sal = float(input("Enter a salary: "))


if counter != 0:
    average = sum / counter
    print("The average salary of the employees is %.2f $." % average)
else:
    print("You did not enter a salary!")
