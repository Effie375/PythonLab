# Αρχικοποίηση μεταβλητών
players = []

for i in range(7):
    # Διάβασμα από τον χρήστη
    name = input("Δώσε όνομα παίκτη: ")
    players.append(name)

for i in range(1, 7):
    for j in range(6, i - 1, -1):
        if players[j - 1] < players[j]:
            temp = players[j - 1]
            players[j - 1] = players[j]
            players[j] = temp

# Εκτύπωση αποτελεσμάτων
print("Παίκτες:", players)
