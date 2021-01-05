flag = False
ginomeno = 0
number = 1

while number != 0:
    number = input("Δώσε αριθμό: ").strip()
    while not number.isdigit():
        number = input("Δώσε σωστά αριθμό: ").strip()
    number = int(number)
    if (flag is False):
        if number != 0:
            ginomeno = 1
        flag = True
    if number != 0:
        ginomeno *= number

# Eκτύπωση αποτελέσματος
print(f"Γινόμενο: {ginomeno}")
