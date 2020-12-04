max_students = 20
student_list =[]
grades_list=[]
maxIndex = 0
i = 0 

while i < max_students:
    student = input("Δώσε το όνομά σου: ")
    student_list.append(student)
    grad = int(input("Δώσε τον βαθμό σου: "))
    grades_list.append(grad)
    i += 1

i = 0

while i < len(grades_list):
    if grades_list[i] > grades_list[maxIndex]:
        maxIndex = i
    i += 1

print("%s κέρδισε τον διαγωνισμό με βαθμό %d." % (student_list[maxIndex], grades_list[maxIndex]))