name = input("Δώσε το όνομά σου: ").split()

try:
    proodos = float(input("Δώσε βαθμό προόδου: ").split)
    grapta = float(input("Δώσε βαθμό γραπτών: ").split)
except:
    print("Μη έγκυρος βαθμός!")
else: 
    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)
    if telikos_vathmos >= 5:
        print("Πέρασες!")
    else:
        print("Απέτυχες!")