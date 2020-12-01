def _main():
    name = input("Δώσε το όνομα σου: ")
    proodos = float(input("Δώσε βαθμό προόδου: "))
    grapta = float(input("Δώσε βαθμό γραπτών: "))

    telikos_vathmos = round(0.2 * proodos + 0.8 * grapta, 1)

    print("Όνομα φοιτητή: %s" % name)
    print("Τελικός βαθμός: %.2f" % telikos_vathmos)


if __name__ == "__main__":
    _main()
