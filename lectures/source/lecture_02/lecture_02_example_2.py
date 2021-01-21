onoma = input('Δώσε όνομα υπαλλήλου: ')
arxikosMisthos = int(input('Δώσε μισθό: '))
foros = int(input('Δώσε ποσοστό φόρου: '))

telikosMisthos = arxikosMisthos - arxikosMisthos * (foros / 100)

print('Όνομα:', onoma)
print('Μισθός:', telikosMisthos)
