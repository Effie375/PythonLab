num_1 = int(input("Δώσε έναν αριθμό: "))
num_2 = int(input("Δώσε έναν αριθμό: "))
num_3 = int(input("Δώσε έναν αριθμό: "))

sum = num_1 + num_2 

if sum % 2 == 0:
    print(num_1 * (num_2 // num_3))
else: 
    mod = num_3 % sum
    print("Το υπόλοιπο της διαίρεσης του %d με το άθροισμα του %d και του %d είναι το %d." % (num_3, num_1, num_2, mod))