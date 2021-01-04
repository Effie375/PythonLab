onoma = input('Δώσε όνομα υπαλλήλου: ')
arxikos_misthos = int(input('Δώσε μισθό: '))
foros = int(input('Δώσε ποσοστό φόρου: '))

telikos_misthos = arxikos_misthos - arxikos_misthos * (foros / 100)

print('Όνομα:', onoma)
print('Μισθός:', telikos_misthos)
