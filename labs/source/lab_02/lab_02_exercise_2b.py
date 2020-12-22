try:
    miktes_apodoxes = float(input("Δώσε τις μεικτές αποδοχές: "))
except:
    print("Μη έγκυρες μεικτές αποδοχές!")
else:
    asfaleia = round(miktes_apodoxes * 0.03, 2)
    foros = round(miktes_apodoxes * 0.05, 2)
    loipes_kratiseis = round(miktes_apodoxes * 0.09, 2)
    kathares_apodoxes = round(miktes_apodoxes - asfaleia - foros - loipes_kratiseis, 2)
    
    print(f"Μεικτές αποδοχές: {miktes_apodoxes}" )
    print(f"Ασφάλεια 3%: {asfaleia}")
    print(f"Φόρος 5% {foros}")
    print(f"Λοιπές κρατήσεις 9%: {loipes_kratiseis}")
    print(f"Καθαρές αποδοχές: {kathares_apodoxes}")
    