# Διαβάζουμε έναν αριθμό και ελέγχουμε αν είναι 0 - 10
def readAndCheck():
    goon = True
    while goon:
        num = input("Δώσε αριθμό: ").strip()
        while not num.isdigit():
            num = input("Δώσε αριθμό: ").strip()
        num = int(num)
        if 0 <= num <= 10:
            goon = false
    return num
