# Διαβάζουμε έναν αριθμό και ελέγχουμε αν είναι 0 - 10
def readAndCheck():
    good = True
    while good:
        num = input("Δώσε αριθμό: ").strip()
        while not num.isdigit():
            num = input("Δώσε αριθμό: ").strip()
        num = int(num)
        if 0 <= num <= 10:
            good = False
    return num
