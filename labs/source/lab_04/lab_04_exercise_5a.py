sum = 0

number = int(input("Δώσε έναν αριθμό: ").strip()) 

while number:
    digit = number % 10
    number /= 10 
    sum += digit

print(f"Το άθροισμα των ψηφίων είναι {sum}.")