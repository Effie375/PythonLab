counter = 0

num = int(input("Δώσε έναν αριθμό: "))

while num != 0:
    if num % 2:
        counter += 1
    num = int(input("Δώσε έναν αριθμό: "))

print("Οι περιττόι αριθμοί είναι %d." % counter)
