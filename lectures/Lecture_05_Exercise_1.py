max_elements = 100
i = 0
list=[]
new_list=[]

while i < max_elements:
    num = int(input("Enter a number: "))
    list.append(num)
    i += 1

j = len(list)

while j > 0:
    new_list.append(list[j-1])
    j -= 1

print("\nThe new list is %s." % new_list)