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

## [Αναζήτηση στοιχείων I](source/lecture_07/lecture_07_example_1a.py)

---

**1ος τρόπος:**

```python
lista = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

thesi = 0

for i in lista:
  if i == key:
    print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
  thesi += 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_1a.py).

**2ος τρόπος:**

```python
lista = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

k = 0

for i in lista:
  if i == key:
    k += 1

print("Το %d έχει εισαχθεί %d φορές." % (key, k))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_1b.py).

## [Αναζήτηση στοιχείων II](source/lecture_07/lecture_07_example_2.py)

---

```python
lista = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0

while (i < 5) and (found is False):
  if lista[i] == key:
    thesi = i
    found = True
  else:
    i += 1

if found == True:
  print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
else:
  print("Το %d δε βρίσκεται στη λίστα %d." % (key, thesi))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_2.py).

## [Αναζήτηση στοιχείων III](source/lecture_07/lecture_07_example_3.py)

---

```python
lista = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0

while (i < 5) and (found is False):
  if lista[i] == key:
    thesi = i
    found = True
  i += 1

if found == True:
  print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
else:
  print("Το %d δε βρίσκεται στη λίστα %s." % (key, lista))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_3.py).

## [7.4 Ταξινόμηση - Bubble Sort](source/lecture_07/lecture_07_example_4.py)

---

```python
lista = [5, 7, 8, 9, 3]

print("Η λίστα μας πριν τη ταξινόμηση είναι: %s" % lista)

for i in range(len(lista)):
  for j in range(len(lista) - 1, i, -1):
    if lista[j - 1] > lista[j]:
      temp = lista[j - 1]
      lista[j - 1] = lista[j]
      lista[j] = temp

print("Η λίστα μας μετά τη ταξινόμηση είναι: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_4.py).

## [7.5 Ταξινόμηση - Διπλή αντιμετάθεση](source/lecture_07/lecture_07_example_5.py)

---

```python
names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
grades = [1, 2, 5, 7, 9]

for i in range(1, 5):
  for j in range(4, i - 1, -1):
    if grades[j - 1] > grades[j]:
      temp = grades[j - 1]
      grades[j - 1] = grades[j]
      grades[j] = temp
      temp2 = names[j - 1]
      names[j - 1] = names[j]
      names[j] = temp2

print(names)
print(grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_5.py).

## [7.6 Διπλή ταξινόμηση](source/lecture_07/lecture_07_example_6.py)

---

```python
names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
grades = [1, 2, 5, 7, 9]

for i in range(1, 5):
  for j in range(4, i - 1, -1):
    if grades[j - 1] > grades[j]:
      temp = grades[j - 1]
      grades[j - 1] = grades[j]
      grades[j] = temp
      temp2 = names[j - 1]
      names[j - 1] = names[j]
      names[j] = temp2
    if grades[j - 1] == grades[j]:
      if names[j - 1] > names[j]:
        temp3 = names[j - 1]
        names[j - 1] = names[j]
        names[j] = temp3

print(names)
print(grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_6.py).

## 7.7 Ασκήσεις

---

## [Άσκηση 1](source/lecture_07/lecture_07_exercise_1.py)

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθµούς και να εµφανίζει τον µέγιστο και τον ελάχιστο µε χρήση ταξινόµησης.

```python
def sort_function(plist):
  try:
    for index in range(len(plist) - 1):
      for j in range(len(plist) - 1, index, -1):
        if plist[j - 1] > plist[j]:
          temp = plist[j - 1]
          plist[j - 1] = plist[j]
          plist[j] = temp
  except:
    print("Κάτι πήγε στραβά!")
    return 1
  else:
    return 0


# Αρχικοποίηση μεταβλητών
MAX_NUMBERS = 100
lista = []

for i in range(MAX_NUMBERS):
  num = input("Δώσε αριθμό: ")
  # Έλεγχος ορθότητας
  while not num.isdigit():
    num = input("Είπα δώσε αριθμό: ")
  # Μετατροπή αλφαριθμητικής τιμής σε ακέραια
  num = int(num)
  # Προσθήκη στοιχείου στη λίστα
  lista.append(num)


if not sort_function(lista):
  print("\nΟ μεγαλύτερος αριθμός είναι το %d." % (lista[len(lista) - 1]))
  print("Ο μικρότερος αριθμός είναι το %d." % lista[0])
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_exercise_1.py).

## [Άσκηση 2](source/lecture_07/lecture_07_exercise_2.py)

Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τα ονόµατα και τους βαθµούς απολυτηρίου των µαθητών και θα εµφανίζει τα ονόµατα των τριών καλύτερων µαθητών.

```python
def sort_function(pnames, pvathmoi):
  try:
    for i in range(len(pvathmoi) - 1):
      for j in range(len(pvathmoi) - 1, i, -1):
        if pvathmoi[j - 1] < pvathmoi[j]:
          # Swap vathmous
          temp1 = pvathmoi[j - 1]
          pvathmoi[j - 1] = pvathmoi[j]
          pvathmoi[j] = temp1
          # Swap names
          temp2 = pnames[j - 1]
          pnames[j - 1] = pnames[j]
          pnames[j] = temp2
  except:
    print("Κάτι πήγε στραβά!")
    return 1
  else:
    return 0


# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

while counter < MAX_ELEMENTS:
  name = input("Δώσε όνομα μαθητή: ")
  vathmos = input("Δώσε βαθμό: ")
  # Έλεγχος ορθότητας
  while not vathmos.isdigit():
    vathmos = input("Είπα δώσε βαθμό: ")
  # Μετατροπή αλφαριθμητικής τιμής σε ακέραια
  vathmos = int(vathmos)
  # Εισαγωγή στοιχείων στη λίστα των φοιτητών και των βαθμών
  names.append(name)
  vathmoi.append(vathmos)
  counter += 1


if not sort_function(names, vathmoi):
  try:
    for i in range(BEST_FOITITES):
      print("Ο %dος καλύτερος είναι ο/η %s." % ((i + 1), names[i]))
  except:
    print("Δεν υπάρχει άλλος φοιτητής στη λίστα!")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_exercise_2.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
