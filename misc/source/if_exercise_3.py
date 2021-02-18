first_attempt = float(input("Πόσα μέτρα πήδηξες στην πρώτη προσπάθεια; "))
second_attempt = float(input("Πόσα μέτρα πήδηξες στη δεύτερη προσπάθεια; "))
third_attempt = float(input("Πόσα μέτρα πήδηξες στην τρίτη προσπάθεια; "))

mo = (first_attempt + second_attempt + third_attempt)/3

print("Ο μέσος όρος είναι %.2f μέτρα." % mo)

if mo > 8:
    print("Προκριθήκατε στον επόμενο αγώνα!")
