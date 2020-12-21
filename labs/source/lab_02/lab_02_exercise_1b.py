name = input("Δώσε το ονομά σου: ").strip()

try:
    proodos = float(input("Δώσε βαθμό προόδου: ").strip())
    grapta = float(input("Δώσε βαθμό γραπτών: ").strip())
except:
    print("Μη έγκυρος βαθμός!")
else: 
    telikos_vathmos = 0.2 * proodos + 0.8 * grapta
    print(f"Όνομα φοιτητή: {name}.")
    print(f"Τελικός βαθμός: {telikos_vathmos:.1f}")