megisto = 0

weight = float(input("Δώσε το βάρος της συσκευασίας σε κιλά: "))

while weight > 0:
    megisto += weight
    weight = float(input("Δώσε το βάρος της συσκευασίας σε κιλά: "))

print("Το συνολικό βάρος είναι %d κιλά." % megisto)
