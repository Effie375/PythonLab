name = input("Δώσε το όνομά σου: ").strip()

try:
    proodos = float(input("Δώσε βαθμό προόδου: ").strip())
    grapta = float(input("Δώσε βαθμό γραπτών: ").strip())
except:
    print("Μη έγκυρος βαθμός!")
else:
    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)
    if telikos_vathmos >= 5:
        print("Πέρασες!")
    else:
        print("Απέτυχες!")
