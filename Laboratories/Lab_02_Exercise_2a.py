miktes_apodoxes = float(input("Dwse tis miktes apodoxes: "))

asfaleia = round(miktes_apodoxes * 0.03, 2)
foros = round(miktes_apodoxes * 0.05, 2)
loipes_kratiseis = round(miktes_apodoxes * 0.09, 2)
kathares_apodoxes = round(miktes_apodoxes - asfaleia - foros - loipes_kratiseis, 2)
    
print("Miktes apodoxes:", miktes_apodoxes)
print("Asfaleia 3%:", asfaleia)
print("Foros 5%:", foros)
print("Loipes kratiseis 9%:", loipes_kratiseis)
print("Kathares apodoxes:", kathares_apodoxes)
