counter = 0
sum = 0

age = int(input("Enter your age: "))

while age > 0:
    counter += 1
    sum += age
    age = int(input("Enter your age: "))
    
if counter != 0:
    average = sum / counter
    print("The average age is %.1f." % average)
else:
    print("You don't enter any age.")
