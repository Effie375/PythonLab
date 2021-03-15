[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FEffie375%2FTPTE_PLR&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# 10.2 Ασκήσεις

---

Εδώ θα βρείτε ένα σύνολο με ασκήσεις που βασίζονται στην ύλη του κεφαλαίου και αναδεικνύουν τις ιδιαιτερότητες του. Οι λύσεις των ασκήσεων βρίσκονται ακριβώς κάτω από κάθε εκφωνήση.

## 10.2.1 Άσκηση 1

---

Αρχικά ζητάμε από το χρήστη να δώσει αριθμό για διαίρεση με το 5. Στη συνέχεια καλούμε τη συνάρτηση `foo` και παίρνει σαν παράμετρο τον αριθμό που δήλωσε ο χρήστης προηγουμένος. Τέλος εμφανίζουμε το αποτέλεσμα της διάιρεσης της παραμέτρου με το 5 στην οθόνη του χρήστη.

Για να δείτε τη **ΛΥΣΗ** πατήστε [εδώ](../lectures/source/lecture_10/lecture_10_exercise_1.py)

## 10.2.2 Άσκηση 2

---

Τι θα εµφανιστεί αν δώσουµε ως τιµή εισόδου στο πρόγραµµα την τιµή 5 και τι την τιµή 10.

```python
def apot(x):
    return x % 2


def foo(n):
  apot1 = n * 2
  n = apot1 * 2
  return n, apot1


a = int(input("Δώσε αριθμό: "))

if apot(a) == 0:
  a, n = foo(a)
  print(a, n)
else:
  print(apot(a))
```

Για να δείτε τη **ΛΥΣΗ** πατήστε [εδώ](../lectures/source/lecture_10/lecture_10_exercise_2.py)

## 10.2.3 Άσκηση 3

---

Να γραφεί µια συνάρτηση η οποία θα δέχεται µια λίστα µε αριθµούς και θα την ταξινοµεί.

Για να δείτε τη **ΛΥΣΗ** πατήστε [εδώ](../lectures/source/lecture_10/lecture_10_exercise_3.py)

<!--
## 9.2.4 Άσκηση 4

---

Ένας μεταπτυχιακός φοιτητής για να μπορέσει να πάρει πτυχίο πρέπει να περάσει συγκεκριμένο αριθμό μαθημάτων ανάλογα με το Τμήμα που φοιτά. Στο παρακάτω πρόγραμμα ένας φοιτητής δίνει τον αριθμό των μαθημάτων που χρειάζεται για να πάρει πτυχίο και στη συνέχεια καταχωρεί τη βαθμολογία των μαθημάτων σε μία λίστα με τη χρήση συνάρτησης. Το πρόγραμμα με τη χρήση συνάρτησης υπολογίζει το μέσο όρο. Ο μέσος όρος εμφανίζεται στην οθόνη και έπειτα χρησιμοποιώντας εκ νέου μία συνάρτηση εμφανίζει αν ο φοιτητής πέρασε ή κόπηκε. Βρείτε όλα τα λάθη (συντακτικά ή λογικά) που υπάρχουν στον παρακάτω κώδικα.

```python
def readNums(x):
lista = []
for numbers in range():
arithmos = float(input("Δώσε αριθμό: "))
lista.append(arithmos)
return list

def mesosOros(y):
athroisma = 0
for stoixeio in x:
athroisma = stoixeio
mo = athroisma / len(x)
return mo

def vathmologia(a):
if a >= 5:
print("Πέρασες")
else
print("Κόπηκες")


stoixeio = int(input("Δώσε στοιχεία που περιέχει η λίστα: ")
numbers = readNums()
mesosoros = mesosOros(numbers)
print("Ο μέσος όρος είναι", mesooros)
vatmologia(mesosoros)
```

Για να δείτε τη **ΛΥΣΗ** πατήστε [εδώ](../lectures/source/lecture_10/lecture_10_exercise_4.py)
-->
