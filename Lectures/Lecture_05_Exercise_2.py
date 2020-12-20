max_students = 200
sum = i = 0
grades = []
stund = []

while i < max_students:
    name = input("Δώσε το όνομά σου: ").strip()
    grad = int(input("Δώσε τον βαθμό σου: ").strip()) 
    stund.append(name)
    grades.append(grad)
    sum += grad
    i += 1

# να ελέγξετε τη διαίρεση με μηδέν!
average = sum / i

i = 0

while i < len(grades):
    if grades[i] > average:
        print(f"Οι μαθητές που έχουν υψηλές βαθμολογίες είνα: {stund[i]}")
    i += 1