try:
    # Διάβασμα μεικτών απολαβών
    miktes_apodoxes = float(input("Δώσε τις μεικτές αποδοχές: ").strip())
except ValueError:
    print("Μη έγκυρες αποδοχές!")
else:
    # Υπολογισμός επί μέρους εισφορών
    asfaleia = round(miktes_apodoxes * 0.03, 2)
    foros = round(miktes_apodoxes * 0.05, 2)
    loipa = round(miktes_apodoxes * 0.09, 2)
    
    # Οι καθαρές απολαβές ειναι οι μεικτές μείον όλες τις εισφορές
    kathara = round(miktes_apodoxes - asfaleia - foros - loipa, 2)
    
    # Εκτύπωση
    print(f"Μεικτές αποδοχές: {miktes_apodoxes}")
    print(f"Ασφάλεια 3%: {asfaleia}")
    print(f"Φόρος 5% {foros}")
    print(f"Λοιπές κρατήσεις 9%: {loipa}")
    print(f"Καθαρές αποδοχές: {kathara}")
