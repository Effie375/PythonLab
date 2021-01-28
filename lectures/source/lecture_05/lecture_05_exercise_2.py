MAX_STUDENTS = 200
sum = i = 0
grades = []
stund = []

while i < MAX_STUDENTS:
    name = input("Δώσε το όνομά σου: ")
    grad = int(input("Δώσε τον βαθμό σου: "))
    stund.append(name)
    grades.append(grad)
    sum += grad
    i += 1

# Να ελέγξετε τη διαίρεση με μηδέν!
average = sum / i

i = 0

while i < len(grades):
    if grades[i] > average:
        print("Οι μαθητές που έχουν υψηλές βαθμολογίες είνα: %s" % stund[i])
    i += 1
