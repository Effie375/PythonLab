onoma = input('Δώσε όνομα υπαλλήλου: ').strip()
arxikos_misthos = int(input('Δώσε μισθό: ').strip())
foros = int(input('Δώσε ποσοστό φόρου: ').strip())

telikos_misthos = arxikos_misthos - arxikos_misthos * (foros / 100)

print(f'Όνομα: {onoma}')
print(f'Μισθός: {telikos_misthos}')
