# Δημιουργία λιστών
names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
grades = [1, 2, 5, 7, 9]

for i in range(1, 5):
    for j in range(4, i - 1, -1):
        if grades[j - 1] > grades[j]:
            # Swap grades
            temp = grades[j - 1]
            grades[j - 1] = grades[j]
            grades[j] = temp
            # Swap names
            temp2 = names[j - 1]
            names[j - 1] = names[j]
            names[j] = temp2
        if grades[j - 1] == grades[j]:
            if names[j - 1] > names[j]:
                # Swap names
                temp3 = names[j - 1]
                names[j - 1] = names[j]
                names[j] = temp3

# Εκτύπωση της ταξινομημένης λίστας names
print(names)
# Εκτύπωση της ταξινομημένης λίστας grades
print(grades)
