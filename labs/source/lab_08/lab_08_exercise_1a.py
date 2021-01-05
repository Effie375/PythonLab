record = float(input("Δώσε ρεκόρ αγώνων: ").strip())

while record < 0 or record > 10:
    record = float(input("Δώσε το σωστό ρεκόρ αγώνων: ").strip())

jumps = []

for i in range(6):
    prospatheia = float(input("Δώσε προσπάθεια αθλητή: ").strip())
    jumps.append(prospatheia)

elaxisto = jumps[0]
megisto = jumps[0]

for i in jumps:
    if i < elaxisto:
        elaxisto = i
    if i > megisto:
        megisto = i

print(f"H χειρότερη προσπάθεια είναι: {elaxisto}")

if megisto > record:
    print(f"Το νέο ρεκόρ είναι {megisto}")
elif record - megisto < 0.5:
    print(f"H καλύτερη προσπάθεια είναι: {megisto}")
else:
    print("Oι προσπάθειες του αθλητή δεν ήταν ικανοποιητικές.")
