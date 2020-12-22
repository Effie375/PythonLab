number = input("Δώσε έναν αριθμό: ")

if number.isdigit() == True:
    number = int(number)
    if number == 0:
        print("Μηδέν")
    elif(number % 2) == 0:
        print("Άρτιος")
    else:
        print("Περιττός")
