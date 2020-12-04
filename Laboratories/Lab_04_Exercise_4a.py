product = number = 1 

while number != 0: 
    number = input("Δώσε αριθμό: ") 
    while  not number.isdigit(): 
        number = input("Δώσε ξανά αριθμό: ")         
    number = int(number)    
    if number != 0: 
        product *= number

print("Γινόμενο: %d" % product)