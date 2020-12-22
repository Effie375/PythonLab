e_counter = 0

word = input("Δώσε λέξη: ")

for i in word:
    if i == 'e':
        e_counter += 1

print(e_counter)