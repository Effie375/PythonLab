# Ζητάμε από το χρήστη να δώσει τις μικτές αποδοχές
miktes = input("Δώσε μικτές αποδοχές: ").strip()

# Μετρατρέπουμε τις μικτές αποδοχές από αλφαριθμητική τιμή σε πραγματική
miktes = float(miktes)

# Υπολογίζουμε τις επί μέρους εισφορές
asfaleia = round(miktes * 0.03, 2)
foros = round(miktes * 0.05, 2)
loipa = round(miktes * 0.09, 2)

# Υπολογίζουμε τις καθαρές αποδοχές που είναι οι μικτές μείον τις εισφορές
kathara = round(miktes - asfaleia - foros - loipa)

# Εκτύπωση αποτελεσμάτων
print(f"\nΜεικτές αποδοχές:    {miktes:.1f}")
print(f"Ασφάλεια 3%:         {asfaleia:.1f}")
print(f"Φόρος 5%             {foros:.1f}")
print(f"Λοιπές κρατήσεις 9%: {loipa:.1f}")
print(f"Καθαρές αποδοχές:    {kathara:.1f}")
