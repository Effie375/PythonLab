flag = False
product = 0
number = 1

while number != 0:
    number = input("Δώσε αριθμό: ").strip()
    while  not arithmos.isdigit(): 
        number = input("Δώσε ξανά αριθμό: ").strip()      
    number = int(arithmos)
    if (flag == False):
        if number != 0:
            product = 1
        flag = True
    if number != 0:
        product *= number

print(f"Γινόμενο: {product}")