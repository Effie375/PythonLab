try:
    miktes_apodoxes = float(input("Δώσε τις μεικτές αποδοχές: ").strip())
except ValueError:
    print(f"Μη έγκυρες αποδοχές!")
else:
    asfaleia = round(miktes_apodoxes * 0.03, 2)
    foros = round(miktes_apodoxes * 0.05, 2)
    loipa = round(miktes_apodoxes * 0.09, 2)
    kathara = round(miktes_apodoxes - asfaleia - foros - loipa, 2)

    print(f"Μεικτές αποδοχές: {miktes_apodoxes}")
    print(f"Ασφάλεια 3%: {asfaleia}")
    print(f"Φόρος 5% {foros}")
    print(f"Λοιπές κρατήσεις 9%: {loipa}")
    print(f"Καθαρές αποδοχές: {kathara}")
