first_attempt = int(input("Πόσα μέτρα πήδηξες στην πρώτη προσπάθεια; "))
second_attempt = int(input("Πόσα μέτρα πήδηξες στη δεύτερη προσπάθεια; "))
third_attempt = int(input("Πόσα μέτρα πήδηξες στην τρίτη προσπάθεια; "))

average = (first_attempt + second_attempt + third_attempt)/3

print("Ο μέσος όρος είναι", round(average, 2), "μέτρα.")

if average > 8:
    print("Προκριθήκατε στον επόμενο αγώνα!")