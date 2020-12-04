odd = even = sum = i = 0
max_elements = 10
list = []

while i < max_elements:
    number = int(input("Δώσε έναν αριθμό: "))
    list.append(number)
    sum += number 
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print("Tο άθροισμα των αριθμών είναι %d." % sum)
print("Tο πλήθος των περιττών είναι %d. " % odd)
print("Το πλήθος των άρτιων είναι %d." % even)

max = min = i = 0

while i < 10:
    if list[i] > list[max]:
        max = i
    elif list[i] < list[min] :
        min = i
    i += 1

diff = list[max] - list[min]

print("H διαφορά μεταξύ του %d και του %d είναι %d." % (list[max], list[min], diff))