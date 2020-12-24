record = float(input("Δώσε ρεκόρ αγώνων: "))

while record < 0 or record > 10:
    record = float(input("Δώσε το σωστό ρεκόρ αγώνων: "))

jumps = []

for i in range(6):
    prospatheia = float(input("Δώσε προσπάθεια αθλητή: "))
    jumps.append(prospatheia)

elaxisto = jumps[0]
megisto = jumps[0]

for i in jumps:
    if i < elaxisto:
        elaxisto = i
    if i > megisto:
        megisto = i

print("H χειρότερη προσπάθεια είναι:", elaxisto)

if megisto > record:
    print("Το νέο ρεκόρ είναι ", megisto)
elif megisto > record - 0.5:
    print("H καλύτερη προσπάθεια είναι:", megisto)
else:
    print("Oι προσπάθειες του αθλητή δεν ήταν ικανοποιητικές.")
