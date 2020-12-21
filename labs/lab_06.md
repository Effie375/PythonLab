# 6 Λίστες (μέρος ΙΙ)

---

## Περιεχόμενα

---

- 6.1 Παράδειγμα
- 6.2 Ασκήσεις

## 6.1 Παράδειγμα

---

Να γραφεί ένα πρόγραμμα που διαβάζει 5αριθμούς και θα τους αποθηκεύει σε μία λίστα. Στη συνέχεια θα διαβάζει έναν τυχαίο αριθμό και θα αναζητά αν ο αριθμός βρίσκεται στη λίστα και σε ποια θέση.

```python
i = 0
list = []
while i < 5:
    number = int(input("Dwse arithmo: "))
    list.append(number)
    i += 1
key = int(input("Dwse stoixeio pou anazitas: "))
found = False
j = 0
while (j < len(list) and not found):
    if list[j] == key:
        thesi = j
        found = True
    j += 1
if found == True:
    print("To stoixeio vriskete sti thesi", thesi)
else:
    print("To stoixeio pou anazitas den iparxei")
```

## 6.2 Ασκήσεις

---

### [6.2.1 Άσκηση 1](source/lab_06/lab_06_exercise_1.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει αριθμούς μέχρι να δωθεί ο αριθμός 0. Μετά θα δέχεται έναν αριθμό και θα εμφανίζει στον χρήστη πόσες φορές είχε εισαχθεί αυτός ο αριθμός. Να μην γίνει χρήση της μεθόδου count().

```python

```

### [6.2.2 Άσκηση 2](source/lab_06/lab_06_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει θετικούς αριθμούς μέχρι να δοθεί ο αριθμός 0. Μετά θα εμφανίζει πόσες φορές εισήχθη ο κάθε αριθμός.

```python

```

[Εργαστήριο 5](lab_05.md) | [Home](../README.md) | [Εργαστήριο 7](lab_07.md)
