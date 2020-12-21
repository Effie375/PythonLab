miktes_apodoxes = float(input("Δώσε τις μεικτές αποδοχές: ").strip())

asfaleia = miktes_apodoxes * 0.03
foros = miktes_apodoxes * 0.05
loipes_kratiseis = miktes_apodoxes * 0.09
kathares_apodoxes = miktes_apodoxes - asfaleia - foros - loipes_kratiseis
    
print(f"Μεικτές αποδοχές: {miktes_apodoxes:.2f}")
print(f"Ασφάλεια 3%: {asfaleia.2f}")
print(f"Φόρος 5%: {foros:.2f}")
print(f"Λοιπές κρατήσεις 9% {loipes_kratiseis:.2f}")
print(f"Καθαρές αποδοχές: {kathares_apodoxes:.2f}")