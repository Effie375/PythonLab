odd = even = sum = i = 0
max_elements = 10
list = []

while i < max_elements:
    number = int(input("Δώσε έναν αριθμό: ").strip())
    list.append(number)
    sum += number 
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print(f"Tο άθροισμα των αριθμών είναι {sum}.")
print(f"Tο πλήθος των περιττών είναι {odd}. ")
print(f"Το πλήθος των άρτιων είναι {even}.")

max = min = i = 0

while i < 10:
    if list[i] > list[max]:
        max = i
    elif list[i] < list[min]:
        min = i
    i += 1

diff = list[max] - list[min]

print(f"H διαφορά μεταξύ του {list[max]} και του {list[min]} είναι {diff}.")
