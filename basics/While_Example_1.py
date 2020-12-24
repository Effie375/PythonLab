counter = sum = 0

sal = float(input("Δώσε το μισθό σου: "))

while sal > 0:
    counter += 1
    sum += sal
    sal = float(input("Δώσε το μισθό σου: "))

if counter != 0:
    average = sum / counter
    print("Ο μέσος όρος των μισθών των υπαλλήλων είναι %.2f $." % average)
else:
    print("Δε δώσατε μισθό!")
