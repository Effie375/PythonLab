# Αρχικοποίηση μεταβλητών
max_players = 7
players = []

for i in range(max_players):
    # Διάβασμα από τον χρήστη
    player = input("Δώσε όνομα παίκτη: ").strip()
    players.append(player)

print(f"Μη ταξινομημένοι παίκτες: {players}")

for i in range(1, max_players):
    for j in range(max_players-1, i-1, -1):
        if players[j-1] < players[j]:
            temp = players[j-1]
            players[j-1] = players[j]
            players[j] = temp

# Εκτύπωση αποτελεσμάτων
print(f"Ταξινομημένοι παίκτες: {players}")
