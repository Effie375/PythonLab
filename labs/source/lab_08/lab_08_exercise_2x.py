# Αρχικοποίηση μεταβλητών
MAX_PLAYERS = 7
players = []

# Για MAX_PLAYERS
for i in range(MAX_PLAYERS):
    # Ζητάμε από το χρήστη να δώσει το όνομά του
    player = input("Δώσε όνομα παίκτη: ").strip()
    # Αποθηκεύουμε το όνομα στη λίστα players
    players.append(player)

# Εκτύπωση της μη ταξινομημένης λίστας με τα ονόματα
print(f"Μη ταξινομημένοι παίκτες: {players}")

for i in range(1, MAX_PLAYERS):
    for j in range(MAX_PLAYERS - 1, i - 1, -1):
        if players[j - 1] < players[j]:
            # Swap players
            temp = players[j - 1]
            players[j - 1] = players[j]
            players[j] = temp

# Εκτύπωση της μη ταξινομημένης λίστας με τα ονόματα
print(f"Ταξινομημένοι παίκτες: {players}")
