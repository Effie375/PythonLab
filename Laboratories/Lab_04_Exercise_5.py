sum = 0

number = int(input("Δώσε έναν αριθμό: ")) 

while number:
   digit = number % 10
   number /= 10 
   sum += digit

print("Το άθροισμα των ψηφίων είναι %d." % sum)