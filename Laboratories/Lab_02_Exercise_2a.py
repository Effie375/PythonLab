def _main():
    miktes_apodoxes = float(input("Δώσε τις μεικτές αποδοχές: "))

    asfaleia = miktes_apodoxes * 0.03
    foros = miktes_apodoxes * 0.05
    loipes_kratiseis = miktes_apodoxes * 0.09
    kathares_apodoxes = miktes_apodoxes - asfaleia - foros - loipes_kratiseis
        
    print("Μεικτές αποδοχές: %.2f" % miktes_apodoxes)
    print("Ασφάλεια 3%%: %.2f" % asfaleia)
    print("Φόρος 5%%: %.2f" % foros)
    print("Λοιπές κρατήσεις 9%%: %.2f" % loipes_kratiseis)
    print("Καθαρές αποδοχές: %.2f" % kathares_apodoxes)


if __name__ == "__main__":
    _main()
