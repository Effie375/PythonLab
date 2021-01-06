# Αρχικοποιούμε τις μεταβλητές
total = 0
i = 0

while i < 6:
    vathmos = input("Δώσε βαθμό: ").strip()
    while not vathmos.isdigit():
        # Εισάγουμε το βαθμού
        vathmos = input("Δώσε ξανά βαθμό: ").strip()
    # Εισάγουμε το βαθμό και μετατρέπουμε την αλφαριθμητική τιμή σε πραγματική
    vathmos = float(vathmos)
    total += vathmos
    i += 1

# Υπολογίζουμε το μέσο όρο
mo = total / 6

if mo > 10:
    print("Κάτι δεν πάει καλά...")
elif mo >= 8.5:
    print(f"Άριστα με μέσο όρο {mo:.1f}!")
elif mo >= 6.5:
    print(f"Λίαν Καλώς με μέσο όρο {mo:.1f}")
elif mo >= 5:
    print(f"Καλώς με μέσο όρο {mo:.1f}")
else:
    print("Kόπηκες")
