num = int(input("Enter a number: "))
numbers = []

while num != 0:
    numbers.append(num)
    num = int(input("Enter a number: "))
    

i = 0
counter = 0

key = int(input("Enter the number you are looking for: "))

while i < len(numbers):
    if key == numbers[i]:
        counter += 1
    i += 1

print("Τhe number %d has been entered %d times." % (key, counter))