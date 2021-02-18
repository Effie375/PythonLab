counter = 0
megisto = 0

sal = float(input("Δώσε το μισθό σου: "))

while sal > 0:
    counter += 1
    megisto += sal
    sal = float(input("Δώσε το μισθό σου: "))

if counter != 0:
    average = megisto / counter
    print("Ο μέσος όρος των μισθών των υπαλλήλων είναι %.2f $." % average)
else:
    print("Δε δώσατε μισθό!")
