i = 0
athroisma = 0

while i< 6:
    vathmos = int(input("Δώσε βαθμό: "))
    athroisma = athroisma + vathmos
    i = i + 1

mo = athroisma / 6

if mo > 10:
    print("Κάτι δεν πάει καλά...")
elif mo >= 8.5:
    print("Άριστα!")
elif mo >= 6.5:
    print("Λίαν Καλώς")
elif mo >= 5:
    print("Καλώς")
else:
    print("Kόπηκες")
