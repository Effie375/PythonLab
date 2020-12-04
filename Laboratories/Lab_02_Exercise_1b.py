name = input("Δώσε το ονομά σου: ")

try:
    proodos = float(input("Δώσε βαθμό προόδου: "))
    grapta = float(input("Δώσε βαθμό γραπτών: "))
except:
    print("Μη έγκυρος βαθμός!")
else: 
    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)
    print("Όνομα φοιτητή: %s" % name)
    print("Τελικός βαθμός: %.1f" % telikos_vathmos)