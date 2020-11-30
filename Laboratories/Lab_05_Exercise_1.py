odd = 0
even = 0
i = 0 
sum = 0

list = []

while i < 10:
    num = int(input("Enter a number: "))
    list.append(num)
    sum += num 
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print("The sum of the numbers is:", sum)
print("The number of odd numbers is:", odd)
print("The number of even numbers is:",even)

i = 0
max = 0
min = 0

while i < 10:
    if list[i] > list[max]:
        max = i
    elif list[i] < list[min] :
        min = i
    i += 1

diff = list[max] - list[min]
print("Τhe difference between the %d and the %d number is %d." % (list[max], list[min], diff))