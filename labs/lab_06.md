# 6 Λίστες (μέρος ΙΙ)

---

## Περιεχόμενα

---

- 6.1 Παράδειγμα
- 6.2 Ασκήσεις

## [6.1 Παράδειγμα](source/lab_06/lab_06_example_1.py)

---

Να γραφεί ένα πρόγραμμα που διαβάζει 5 αριθμούς και θα τους αποθηκεύει σε μία λίστα. Στη συνέχεια θα διαβάζει έναν τυχαίο αριθμό και θα αναζητά αν ο αριθμός βρίσκεται στη λίστα και σε ποια θέση.

```python
i = 0
list = []

while i < 5:
  number = int(input("Δώσε αριθμό: "))
  list.append(number)
  i += 1

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
j = 0

while (j < len(list) and not found):
  if list[j] == key:
    thesi = j
    found = True
  j += 1

if found == True:
  print("Το στοιχείο βρίσκεται στη θέση", thesi)
else:
  print("Το στοιχείο που αναζητάς δεν υπάρχει.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_06/lab_06_example_1.py)

## 6.2 Ασκήσεις

---

### [Άσκηση 1](source/lab_06/lab_06_exercise_1.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει αριθμούς μέχρι να δωθεί ο αριθμός 0. Μετά θα δέχεται έναν αριθμό και θα εμφανίζει στον χρήστη πόσες φορές είχε εισαχθεί αυτός ο αριθμός. Να μην γίνει χρήση της μεθόδου count().

```python
l = []

number = int(input("Δώσε αριθμό: "))

while number != 0:
  l.append(number)
  number = int(input("Δώσε αριθμό: "))

counter = 0
i=0

number = int(input("Δώσε αριθμό για μέτρηση: "))

while i < len(l):
  if l[i] == number:
    counter += 1
  i += 1

print("O αριθμός", number, "είσηχθη", counter, "φορές")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_06/lab_06_exercise_1.py)

### [Άσκηση 2](source/lab_06/lab_06_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει θετικούς αριθμούς μέχρι να δοθεί ο αριθμός 0. Μετά θα εμφανίζει πόσες φορές εισήχθη ο κάθε αριθμός.

```python
megisto = 0
l=[]

number = int(input("Δώσε αριθμό: "))

while number != 0:
  l.append(number)
  if number > megisto:
    megisto = number
  number = int(input("Δώσε αριθμό: "))

i = 1

while i <= megisto:
  j = 0
  counter = 0
  while j < len(l):
    if l[j] == i:
      counter += 1
      j += 1

    if counter != 0 :
      print("Ο αριθμός", i, "εισήχθη", counter, "φορές.")
    i += 1 
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_06/lab_06_exercise_2.py)

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)
