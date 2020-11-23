'''
Ένας μετεωρολόγος καταγράφει τις θερµοκρασίες των ημερών
ενός µήνα 30 ημερών που σηµειώθηκαν στο κέντρο µιας πόλης
στις 12 το μεσημέρι. Να γίνει πρόγραµµα που θα διαβάζει τις
θερµοκρασίες αυτές, θα τις καταχωρεί σε µία λίστα και θα 
υπολογίζει και θα εµφανίζει την ελάχιστη θερµοκρασία και την 
ηµέρα που σημειώθηκε καθώς και τη μέγιστη θερµοκρασία και την ηµέρα που σημειώθηκε.
'''
days = []
temps = []

i = 0

while i < 30:
    day = input("\nEnter a day: ")
    tem = int(input("Enter a temperature:"))
    days.append(day)
    temps.append(tem)
    i += 1


max= 0
i = 0

while i < len(temps):
    if temps[i] > temps[max]:
        max = i
    i += 1
print("\nThe highest temperature was recorded on %s and had %d degrees."% (days[max], temps[max]))

min = 0
i = 0

while i < len(temps):
    if temps[i] < temps[min]:
        min = i
    i += 1
print("The lowest temperature was recorded on %s and had %d degrees" % (days[min], temps[min]))

