product = number = 1 

while number != 0: 
    number = input("Δώσε αριθμό: ").strip()
    while  not number.isdigit(): 
        number = input("Δώσε ξανά αριθμό: ").strip()         
    number = int(number)    
    if number != 0: 
        product *= number

print(f"Γινόμενο: {product}")