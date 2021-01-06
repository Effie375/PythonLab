try:
    # Ζητάμε από τον χρήστη να δώσει τις μικτές αποδοχές
    miktes = float(input("Δώσε τις μεικτές αποδοχές: ").strip())
except ValueError:
    print("Μη έγκυρες αποδοχές!")
else:
    # Υπολογίζουμε τις επί μέρους εισφορές
    asfaleia = round(miktes * 0.03, 2)
    foros = round(miktes * 0.05, 2)
    loipa = round(miktes * 0.09, 2)

    # Υπολογίζουμε τις καθαρές αποδοχές που είναι οι μικτές μείον τις εισφορές
    kathara = round(miktes - asfaleia - foros - loipa, 2)

    # Εκτύπωση αποτελεσμάτων
    print(f"Μεικτές αποδοχές: {miktes}")
    print(f"Ασφάλεια 3%: {asfaleia}")
    print(f"Φόρος 5% {foros}")
    print(f"Λοιπές κρατήσεις 9%: {loipa}")
    print(f"Καθαρές αποδοχές: {kathara}")
