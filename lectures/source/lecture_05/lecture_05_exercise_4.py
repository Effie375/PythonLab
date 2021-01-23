MAX_STUDENTS = 20
student_list = []
grades_list = []
maxIndex = 0
i = 0

while i < MAX_STUDENTS:
    student = input("Δώσε το όνομά σου: ").strip()
    student_list.append(student)
    grad = int(input("Δώσε τον βαθμό σου: ").strip())
    grades_list.append(grad)
    i += 1

i = 0

while i < len(grades_list):
    if grades_list[i] > grades_list[maxIndex]:
        maxIndex = i
    i += 1

print(f"{student_list[maxIndex]} κέρδισε με βαθμό {grades_list[maxIndex]}.")
