pl_ar = 0
pl_math = 0
athroisma = 0

b = float(input("Δώσε βαθμό μαθητή: "))

while b != -1:
    if b > 18:
        pl_ar += 1
    athroisma += b
    pl_math += 1
    b = float(input("Δώσε βαθμό μαθητή: "))

if pl_math != 0:
    mo = athroisma / pl_math
    print("Μέσος όρος: %.2f, Αριστούχοι: %d" % (mo, pl_ar))
else:
    print("Δεν δόθηκε κανένας βαθμός")
