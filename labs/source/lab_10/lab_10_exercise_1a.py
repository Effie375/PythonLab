eksamina = []

for i in range(8):
    vathmoi = []
    for j in range(6):
        vathmos = float(input("Δώσε βαθμό: ").strip())
        vathmoi.append(vathmos)
eksamina.append(vathmoi)

ar_eksaminou = int(input("Ποιο εξάμηνο θες να δείς;").strip())

# Aφαιρούμε 1 γιατί ο χρήστης θα δώσει π.χ. 1 για το πρώτο εξάμηνο
# ενώ αυτό είναι στη θέση 0.
eksamino = eksamina[ar_eksaminou-1]

souma = 0
perasmena = 0

for mathima in eksamino:
    souma += mathima
    if mathima >= 5:
        perasmena += 1

print(f"Ο μέσος όρος είναι: {souma/len(eksamino)}")
print(f"Πέρασες: {perasmena}")
