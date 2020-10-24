#Exercise 1

name = input("Dwse to onoma sou: ")

try:
    proodos = float(input("Dwse vathmo proodou: "))
    grapta = float(input("Dwse vathmo graptwn: "))
except:
    print("Mi egkiros vathmos!")
else: 
    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)
    print("Onoma foititi:", name)
    print("Telikos vathmos:", telikos_vathmos)
