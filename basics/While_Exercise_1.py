sum = 0

weight = float(input("Δώσε το βάρος της συσκευασίας σε κιλά: ").strip())

while weight > 0:
    sum += weight
    weight = float(input("Δώσε το βάρος της συσκευασίας σε κιλά: ").strip())

print(f"Το συνολικό βάρος είναι {sum} κιλά.")
