name = input("Δώσε το όνομα σου: ").strip()
proodos = float(input("Δώσε βαθμό προόδου: ").strip())
grapta = float(input("Δώσε βαθμό γραπτών: ").strip())

telikos_vathmos = 0.2 * proodos + 0.8 * grapta

print(f"Όνομα φοιτητή: {name}")
print("Τελικός βαθμός: %.1f" % telikos_vathmos)