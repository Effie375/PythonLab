# Ζητάμε από το χρήστη να δώσει τις μικτές αποδοχές
miktes = input("Δώσε μικτές αποδοχές: ")

# Μετρατρέπουμε τις μικτές αποδοχές από αλφαριθμητική τιμή σε πραγματική
miktes = float(miktes)

# Υπολογίζουμε τις επί μέρους εισφορές
asfaleia = round(miktes * 0.03, 2)
foros = round(miktes * 0.05, 2)
loipa = round(miktes * 0.09, 2)

# Υπολογίζουμε τις καθαρές αποδοχές που είναι οι μικτές μείον τις εισφορές
kathara = round(miktes - asfaleia - foros - loipa)

# Εκτύπωση αποτελεσμάτων
print("\nΜεικτές αποδοχές:\t%.1f" % miktes)
print("Ασφάλεια 3%%:\t\t%.1f" % asfaleia)
print("Φόρος 5%%:\t\t%.1f" % foros)
print("Λοιπές κρατήσεις 9%%:\t%.1f" % loipa)
print("Καθαρές αποδοχές:\t%.1f" % kathara)
