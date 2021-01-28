# Αρχικοποίηση μεταβλητών
counter = 0

# Ζητάμε από το χρήστη να δώσει μια λέξη
leksi = input("Δώσε λέξη με λατινικούς χαρακτήρες: ").strip()

# Για κάθε γράμμα της λέξης
for gramma in leksi:
    # Εάν το γράμμα είναι το 'e'
    if gramma == 'e':
        # Αυξάνουμε το μετρητή κατά 1
        counter += 1

# Eάν ο μετρητής είναι 1
if counter == 1:
    print(f"Το γράμμα 'e' εισήχθη {counter} φορά.")
# Αλλιώς εάν ο μετρητής δεν είναι ουτε 0 ούτε 1
elif counter != 0:
    print(f"Το γράμμα 'e' εισήχθη {counter} φορές.")
# Αλλιώς το γράμμα 'e' δεν εισήχθη
else:
    print("Το γράμμα 'e' δεν εισήχθη.")
