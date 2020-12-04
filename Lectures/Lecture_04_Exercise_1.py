counter = 0
num = 1

while num != 0:
    num = float(input("Δώσε έναν αριθμό: "))
    if num > 0:
        counter += 1

if counter > 0:
    print("Οι θετικοί αριθμοί είναι %d." % counter)
else:
    print("Δεν δώσατε θετικούς αριθμούς.")