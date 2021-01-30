# 7 Μονοδιάστατες λίστες - Αναζήτηση - Ταξινόμηση

---

## Περιεχόμενα

---

- 7.1 Αναζήτηση στοιχείων I
- 7.2 Αναζήτηση στοιχείων II
- 7.3 Αναζήτηση στοιχείων III
- 7.4 Ταξινόμηση - Bubble Sort
- 7.5 Ταξινόμηση - Διπλή αντιμετάθεση
- 7.6 Διπλή ταξινόμηση
- 7.7 Ασκήσεις

## Αναζήτηση στοιχείων I

---

**1ος τρόπος:**

<!--
# Δημιουργία λίστας
lista = [9, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητής
thesi = 0

# Για κάθε στοιχείο της λίστας
for i in lista:
  # Εάν το στιγμιαίο στοιχείο είναι ίσο με το key
  if i == key:
    print(f"Το {key} βρίσκεται στη θέση {thesi}.")
  # Αυξάνουμε τη thesi κατά 1
  thesi += 1
-->

```python
# Δημιουργία λίστας
lista = [9, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητής
thesi = 0

# Για κάθε στοιχείο της λίστας
for i in lista:
  # Εάν το στιγμιαίο στοιχείο είναι ίσο με το key
  if i == key:
    # Εκτύπωση σε ποια θέση βρίσκεται το key
    print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
  # Αυξάνουμε τη thesi κατα 1
  thesi += 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_1a.py).

**2ος τρόπος:**

<!--
# Δημιουργία λίστας
lista = [9, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητής
k = 0

# Για κάθε στοιχείο της λίστας
for i in lista:
  # Εάν το στιγμιαίο στοιχείο είναι ίσο με το key
  if i == key:
    # Αυξάνουμε το k κατά 1
    k += 1

# Εκτύπωση το πόσες φορές εισήχθη το key
print(f"Το {key} έχει εισαχθεί {k} φορές.")
-->

```python
# Δημιουργία λίστας
lista = [9, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητής
k = 0

# Για κάθε στοιχείο της λίστας
for i in lista:
  # Εάν το στιγμιαίο στοιχείο είναι ίσο με το key
  if i == key:
    # Αυξάνουμε το k κατά 1
    k += 1

# Εκτύπωση το πόσες φορές εισήχθη ο αριθμός
print("Το %d έχει εισαχθεί %d φορές." % (key, k))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_1b.py).

## Αναζήτηση στοιχείων II

---

<!--
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found είναι ίσο με False
while (i < 5) and (found == False):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Εκχωρούμε στη thesi το i
    thesi = i
    # Το found γίνεται True
    found = True
  # Αλλιώς σε οποιαδήποτε άλλη περίπτωση
  else:
    # Αυξάνουμε το i κατά 1
    i += 1

# Εάν το found είναι ίσο με True
if found == True:
  # Εκτύπωση τη θέση που βρίσκεται το key
  print(f"Το {key} βρίσκεται στη {thesi} θέση.")
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Εκτύπωση ότι το key δε βρίσκεται στη λίστα
  print(f"Το {key} δε βρίσκεται στη λίστα {lista}.")
-->

```python
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found είναι ίσο με False
while (i < 5) and (found == False):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Εκχωρούμε στη thesi το i
    thesi = i
    # Το found γίνεται True
    found = True
  # Αλλιώς σε οποιαδήποτε άλλη περίπτωση
  else:
    i += 1

# Εάν το found είναι ίσο με True
if found == True:
  # Εκτύπωση τη θέση που βρίσκεται το key
  print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Εκτύπωση ότι το key δε βρίσκεται στη λίστα
  print("Το %d δε βρίσκεται στη λίστα %d." % (key, thesi))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_2.py).

## Αναζήτηση στοιχείων III

---

<!--
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found είναι ίσο με False
while (i < 5) and (found == False):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Εκχωρούμε στη thesi το i
    thesi = i
    # Το found γίνεται True
    found = True
  # Αυξάνουμε το i κατά 1
  i += 1

# Εάν το found είναι ίσο με True
if found == True:
  # Εκτύπωση τη θέση που βρίσκεται το key
  print(f"Το {key} βρίσκεται στη {thesi} θέση.")
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Εκτύπωση ότι το key δε βρίσκεται στη λίστα
  print(f"Το {key} δε βρίσκεται στη λίστα {lista}.")
-->

```python
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
i = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found είναι ίσο με False
while (i < 5) and (found == False):
  # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
  if lista[i] == key:
    # Εκχωρούμε στη thesi το i
    thesi = i
    # Το found γίνεται True
    found = True
  # Αυξάνουμε το i κατά 1
  i += 1

# Εάν το found είναι ίσο με True
if found == True:
  # Εκτύπωση τη θέση που βρίσκεται το key
  print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Εκτύπωση ότι το key δε βρίσκεται στη λίστα
  print("Το %d δε βρίσκεται στη λίστα %s." % (key, lista))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_3.py).

## 7.4 Ταξινόμηση - Bubble Sort

---

<!--
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print(f"Η λίστα μας πριν την ταξινόμηση είναι:{lista}")

for i in range(len(lista)):
  for j in range(len(lista) - 1, i, -1):
    if lista[j - 1] > lista[j]:
      # Swap lista
      temp = lista[j - 1]
      lista[j - 1] = lista[j]
      lista[j] = temp

# Εκτύπωση της λίστας μετά την ταξινόμηση
print(f"Η λίστα μας μετά την ταξινόμηση είναι:{lista}")
-->

```python
# Δημιουργία λίστας
lista = [5, 7, 8, 9, 3]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print("Η λίστα μας πριν την ταξινόμηση είναι: %s" % lista)

for i in range(len(lista)):
  for j in range(len(lista) - 1, i, -1):
    if lista[j - 1] > lista[j]:
      # Swap lista
      temp = lista[j - 1]
      lista[j - 1] = lista[j]
      lista[j] = temp

# Εκτύπωση της λίστας πριν την ταξινόμηση
print("Η λίστα μας μετά την ταξινόμηση είναι: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_4.py).

## 7.5 Ταξινόμηση - Διπλή αντιμετάθεση

---

<!--
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

# Εκτύπωση της ταξινομημένης λίστας names
print(names)
# Εκτύπωση της ταξινομημένης λίστας grades
print(grades)
-->

```python
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

# Εκτύπωση της ταξινομημένης λίστας names
print(names)
# Εκτύπωση της ταξινομημένης λίστας grades
print(grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_5.py).

## 7.6 Διπλή ταξινόμηση

---

<!--
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
-->

```python
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
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_6.py).

## 7.7 Ασκήσεις

---

## Άσκηση 1

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθµούς και να εµφανίζει τον µέγιστο και τον ελάχιστο µε χρήση ταξινόµησης.

<!--
# Δημιουργία συνάρτησης sortFunction
def sortFunction(plist):
  try:
    for index in range(len(plist) - 1):
      for j in range(len(plist) - 1, index, -1):
          if plist[j - 1] > plist[j]:
            # Swap plist
            temp = plist[j - 1]
            plist[j - 1] = plist[j]
            plist[j] = temp
  except:
    # Εκτύπωση κάτι πήγε στραβά
    print("Κάτι πήγε στραβά!")
    # Επιστρέφει 1
    return 1
  else:
    # Επιστρέφει 0
    return 0


# Αρχικοποίηση μεταβλητών
MAX_NUMBERS = 100
lista = []

# Για MAX_NUMBERS
for i in range(MAX_NUMBERS):
  # Ζητάμε από το χρήστη να δώσει αριθμό
  num = input("Δώσε αριθμό: ").strip()
  # Έλεγχος ορθότητας
  while not num.isdigit():
    # Ξανά ζητάμε από το χρήστη να δώσει αριθμό
    num = input("Είπα δώσε αριθμό: ").strip()
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  num = int(num)
  # Αποθηκεύουμε τον αριθμό στη λίστα
  lista.append(num)

if not sortFunction(lista):
  # Εκτύπωση του μεγαλύτερου αριθμού της λίστας
  print(f"\nΟ μεγαλύτερος αριθμός είναι το {lista[len(lista) - 1]}.")
  # Εκτύπωση του μικρότερου αριθμού της λίστας
  print(f"Ο μικρότερος αριθμός είναι το {lista[0]}.")
-->

```python
# Δημιουργία συνάρτησης sortFunction
def sortFunction(plist):
  try:
    for index in range(len(plist) - 1):
      for j in range(len(plist) - 1, index, -1):
        if plist[j - 1] > plist[j]:
          # Swap plist
          temp = plist[j - 1]
          plist[j - 1] = plist[j]
          plist[j] = temp
  except:
    # Εκτύπωση κάτι πήγε στραβά
    print("Κάτι πήγε στραβά!")
    # Επιστρέφει 1
    return 1
  else:
    # Επιστρέφει 0
    return 0


# Αρχικοποίηση μεταβλητών
MAX_NUMBERS = 100
lista = []

# Για MAX_NUMBERS
for i in range(MAX_NUMBERS):
  # Ζητάμε από το χρήστη να δώσει αριθμό
  num = input("Δώσε αριθμό: ")
  # Έλεγχος ορθότητας
  while not num.isdigit():
    # Ξανά ζητάμε από το χρήστη να δώσει αριθμό
    num = input("Είπα δώσε αριθμό: ")
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  num = int(num)
  # Αποθηκεύουμε τον αριθμό στη λίστα
  lista.append(num)


if not sortFunction(lista):
  # Εκτύπωση του μεγαλύτερου αριθμού της λίστας
  print("\nΟ μεγαλύτερος αριθμός είναι το %d." % (lista[len(lista) - 1]))
  # Εκτύπωση του μικρότερου αριθμού της λίστας
  print("Ο μικρότερος αριθμός είναι το %d." % lista[0])
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_exercise_1.py).

## Άσκηση 2

Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τα ονόµατα και τους βαθµούς απολυτηρίου των µαθητών και θα εµφανίζει τα ονόµατα των τριών καλύτερων µαθητών.

<!--
# Δημιουργία συνάρτησης sortFunction
def sortFunction(pnames, pvathmoi):
  try:
    for i in range(len(pvathmoi) - 1):
      for j in range(len(pvathmoi) - 1, i, -1):
        if pvathmoi[j - 1] < pvathmoi[j]:
          # Swap pvathmoi
          temp1 = pvathmoi[j - 1]
          pvathmoi[j - 1] = pvathmoi[j]
          pvathmoi[j] = temp1
          # Swap pnames
          temp2 = pnames[j - 1]
          pnames[j - 1] = pnames[j]
          pnames[j] = temp2
  except:
    # Eκτύπωση κάτι πήγε στραβά
    print("Κάτι πήγε στραβά!")
    # Επιστρέφει 1
    return 1
  else:
    # Επιστρέφει 0
    return 0


# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

# Για όσο ο counter είναι μικρότερος από το MAX_ELEMENTS
while counter < MAX_ELEMENTS:
  # Ζητάμε από το φοιτητή να δώσει το όνομά του
  name = input("Δώσε όνομα μαθητή: ").strip()
  # Ζητάμε από το φοιτητή να δώσει το βαθμό του
  vathmos = input("Δώσε βαθμό: ").strip()
  # Έλεγχος ορθότητας
  while not vathmos.isdigit():
    # Ξανά ζητάμε από το φοιτητή να δώσει το βαθμό του:
    vathmos = input("Είπα δώσε βαθμό: ").strip()
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  vathmos = int(vathmos)
  # Αποθηκεύουμε το όνομα στη λίστα names
  names.append(name)
  # Αποθηκεύουμε το βαθμό στη λίστα vathmoi
  vathmoi.append(vathmos)
  # Αυξάνουμε τον counter κατά 1
  counter += 1


if not sortFunction(names, vathmoi):
  try:
    # Για BEST_FOITITES
    for i in range(BEST_FOITITES):
      # Εκτύπωση του καλύτερου φοιτητή
      print(f"Ο {i + 1}ος καλύτερος είναι ο/η {names[i]}.")
  except:
    # Εκτύπωση δεν υπάρχει άλλος φοιτητής στη λίστα
    print("Δεν υπάρχει άλλος φοιτητής στη λίστα!")
-->

```python
# Δημιουργία συνάρτησης sortFunction
def sort_function(pnames, pvathmoi):
  try:
    for i in range(len(pvathmoi) - 1):
      for j in range(len(pvathmoi) - 1, i, -1):
        if pvathmoi[j - 1] < pvathmoi[j]:
          # Swap pvathmoi
          temp1 = pvathmoi[j - 1]
          pvathmoi[j - 1] = pvathmoi[j]
          pvathmoi[j] = temp1
          # Swap pnames
          temp2 = pnames[j - 1]
          pnames[j - 1] = pnames[j]
          pnames[j] = temp2
  except:
    # Eκτύπωση κάτι πήγε στραβά
    print("Κάτι πήγε στραβά!")
    # Επιστρέφει 1
    return 1
  else:
    # Επιστρέφει 0
    return 0


# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

# Για όσο ο counter είναι μικρότερος από το MAX_ELEMENTS
while counter < MAX_ELEMENTS:
  # Ζητάμε από το φοιτητή να δώσει το όνομά του
  name = input("Δώσε όνομα μαθητή: ")
  # Ζητάμε από το φοιτητή να δώσει το βαθμό του
  vathmos = input("Δώσε βαθμό: ")
  # Έλεγχος ορθότητας
  while not vathmos.isdigit()
    # Ξανά ζητάμε από το φοιτητή να δώσει το βαθμό του:
    vathmos = input("Είπα δώσε βαθμό: ")
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  vathmos = int(vathmos)
  # Αποθηκεύουμε το όνομα στη λίστα names
  names.append(name)
  # Αποθηκεύουμε το βαθμό στη λίστα vathmoi
  vathmoi.append(vathmos)
  # Αυξάνουμε τον counter κατά 1
  counter += 1


if not sort_function(names, vathmoi):
  try:
    # Για BEST_FOITITES
    for i in range(BEST_FOITITES):
      # Εκτύπωση του καλύτερου φοιτητή
      print("Ο %dος καλύτερος είναι ο/η %s." % ((i + 1), names[i]))
  except:
    # Εκτύπωση δεν υπάρχει άλλος φοιτητής στη λίστα
    print("Δεν υπάρχει άλλος φοιτητής στη λίστα!")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_exercise_2.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
