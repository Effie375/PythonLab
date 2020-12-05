try:
    miktes_apodoxes = float(input("Δώσε τις μεικτές αποδοχές: "))
except:
    print("Μη έγκυρες μεικτές αποδοχές!")
else:
    asfaleia = round(miktes_apodoxes * 0.03, 2)
    foros = round(miktes_apodoxes * 0.05, 2)
    loipes_kratiseis = round(miktes_apodoxes * 0.09, 2)
    kathares_apodoxes = round(miktes_apodoxes - asfaleia - foros - loipes_kratiseis, 2)
    
    print("Μεικτές αποδοχές: %d" % miktes_apodoxes)
    print("Ασφάλεια 3%%: %d" % asfaleia)
    print("Φόρος 5%%: %d" % foros)
    print("Λοιπές κρατήσεις 9%%: %d" % loipes_kratiseis)
    print("Καθαρές αποδοχές: %d" % kathares_apodoxes)