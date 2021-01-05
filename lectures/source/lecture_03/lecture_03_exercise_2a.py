num_1 = int(input("Δώσε έναν αριθμό: ").strip())
num_2 = int(input("Δώσε έναν αριθμό: ").strip())
num_3 = int(input("Δώσε έναν αριθμό: ").strip())

sum = num_1 + num_2

if sum % 2 == 0:
    print(num_1 * (num_2 // num_3))
else:
    mod = num_3 % sum
    print(f"Το υπόλοιπο της διαίρεσης είναι το {mod}.")
