name = input("Enter your name: ")

try:
    proodos = float(input("Dwse vathmo proodou: "))
    grapta = float(input("Dwse vathmo graptwn: "))
except:
    print("Mi egkiros vathmos!")
else: 
    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)
    if telikos_vathmos >= 5:
        print("perases")
    else:
        print("apetixes")