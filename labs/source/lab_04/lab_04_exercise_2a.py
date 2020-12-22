total = i = 0

while i < 6:
    degree = input("Δώσε βαθμό: ").strip()
    while not degree.isdigit():
        degree = input("Δώσε ξανά βαθμό: ").strip()
    degree = float(degree)
    total += degree
    i += 1

average = (total/6)

if (average >= 8.5 and average <= 10):
    print("Άριστα με μέσο όρο: %.1f" % average)
elif (average >= 6.5 and average <= 8.49):
    print("Λιαν καλός με μέσο όρο: %.1f" % average)
elif (average >= 5 and average <= 6.49):
    print("Κάλος με μέσο όρο: %.1f" % average)
else:
    print("Κόπηκες!")
