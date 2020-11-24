counter = 0 
num = int(input("Enter a number: "))

while num != 0:
    if num % 2:
        counter += 1
    num = int(input("Enter a number: "))

print("Τhe odd numbers are:", counter) 