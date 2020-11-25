i = 0 
numbers = []

while i < 5:
    num = int(input("Enter a number: "))
    numbers.append(num)
    i += 1

key = int(input("Enter a key number: "))

i = 0
flag = False

while ((i < len(numbers)) and not flag):
    if key == numbers[i]:
        index = i
        flag = True
    i += 1

if flag:
    print("The number %d is in position %d." % (key, index))
else:
    print("The key number %d is not in the list." % key)
