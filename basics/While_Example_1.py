counter = sum = 0

sal = float(input("Δώσε το μισθό σου: ").strip())

while sal > 0:
    counter += 1
    sum += sal
    sal = float(input("Δώσε το μισθό σου: ").strip())

if counter != 0:
    average = sum / counter
    print(f"Ο μέσος όρος των μισθών των υπαλλήλων είναι {average:.2f}$.")
else:
    print(f"Δε δώσατε μισθό!")
