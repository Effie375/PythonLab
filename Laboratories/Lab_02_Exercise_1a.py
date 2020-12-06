name = input("Δώσε το όνομα σου: ")
proodos = float(input("Δώσε βαθμό προόδου: "))
grapta = float(input("Δώσε βαθμό γραπτών: "))

telikos_vathmos = 0.2 * proodos + 0.8 * grapta

print("Όνομα φοιτητή: %s" % name)
print("Τελικός βαθμός: %.1f" % telikos_vathmos)