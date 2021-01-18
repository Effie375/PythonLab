# 5 Εισαγωγή στις λίστες

---

## Περιεχόμενα

---

- 5.1 Μονοδιάστατη λίστα
- 5.2 Αποθήκευση στοιχείων
- 5.3 Άθροισμα στοιχείων
- 5.4 Έυρεση MAX
- 5.5 Έυρεση MIN
- 5.6 Έυρεση MAX με θέση
- 5.7 Αναζήτηση στοιχείων I
- 5.8 Αναζήτηση στοιχείων II
- 5.9 Αναζήτηση αριθμού στοιχείων
- 5.10 Ασκήσεις

## 5.1 Μονοδιάστατη λίστα

---

- Δυναμική δομή δεδομένων για διατεταγμένη συλλογή στοιχείων.
- Όχι απαραίτητα του ίδιου τύπου.
- Τα στοιχεία μέσα σε [ ].
- Χρησιμοποιούμε λίστες στην python για την αναπαράσταση πινάκων.

**Χαρακτηριστικά:**

- Ένα Όνομα
- Πολλές Θέσεις
- Μια Δομή

```python
list = [5, 7, 8, 9, 3]

list[2] = 4
list[0] = input("Δώσε τιμή: ")
```

## [5.2 Αποθήκευση στοιχείων](source/lecture_05/lecture_05_example_1.py)

---

```python
list = []
i = 0

while i < 5:
  num = int(input("Δώσε στοιχείο για την θέση %d: " % i))
  list.append(num)
  i += 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_1.py).

## [5.3 Άθροισμα στοιχείων](source/lecture_05/lecture_05_example_2.py)

---

```python
list = [1, 2, 3, 4, 5]
sum = 0
i = 0

while i < len(list):
  sum += list[i]
  i += 1

print("Άθροισμα:", sum)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_2.py).

## [5.4 Έυρεση MAX](source/lecture_05/lecture_05_example_3.py)

---

```python
list = [1, 4, 6, 9, 7, 2]
megisto = list[0]
i = 0

while i < len(list):
  if list[i] > megisto:
    megisto = list[i]
  i += 1

print("Μέγιστο:", megisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_3.py).

## [5.5 Έυρεση MIN](source/lecture_05/lecture_05_example_4.py)

---

```python
list = [3, 4, 1, 9, 7, 2]
elaxisto = list[0]
i = 0

while i < len(list):
  if list[i] < elaxisto:
    elaxisto = list[i]
  i += 1

print("Ελάχιστο:", elaxisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_4.py).

## [5.6 Έυρεση MAX με θέση](source/lecture_05/lecture_05_example_5.py)

---

```python
list = [3, 4, 1, 9, 4, 2]
maxThesi = 0
i = 0

while i < len(list):
  if list[i] > list[maxThesi]:
    maxThesi = i
  i += 1

print("Μέγιστη θέση:", maxThesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_5.py).

## [5.7 Αναζήτηση στοιχείων I](source/lecture_05/lecture_05_example_6.py)

---

```python
list = [3, 4, 1, 9, 4, 2]
key = int(input("Δώσε στοιχείο που αναζητάς: "))
i = 0

while i < len(list):
  if key == list[i]:
    thesi = i
  i += 1

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_6.py).

## [5.8 Αναζήτηση στοιχείων II](source/lecture_05/lecture_05_example_7.py)

---

```python
list = [3, 4, 1, 9, 7, 2]
key = int(input("Δώσε στοιχείο που αναζητάς: "))
found = False
i = 0

while (i < len(list)) and (not found):
  if list[i] == key:
    thesi = i
    found = True
  i += 1

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_7.py).

## [5.9 Αναζήτηση αριθμού στοιχείων](source/lecture_05/lecture_05_example_8.py)

---

```python
list = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]
key = int(input("Δώσε στοιχείο που αναζητάς: "))
counter = 0
i = 0

while i < len(list):
  if list[i] == key:
    counter += 1
  i += 1

print("Το στοιχείο που αναζητάς εμφανίζεται", counter, "φορές στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_8.py).

## 5.10 Ασκήσεις

---

### [Άσκηση 1](source/lecture_05/lecture_05_exercise_1.py)

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθµούς και να τους εµφανίζει ανάποδα από τη σειρά που διαβάστηκαν.

```python
list = []
i = 0

while i < 100:
  list.append(int(input("Δώσε αριθμό: ")))
  i += 1

i = 100

while i > 0:
  print(list[i - 1])
  i -= 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_1.py).

### [Άσκηση 2](source/lecture_05/lecture_05_exercise_2.py)

Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τους βαθµούς απολυτηρίου των µαθητών και θα εµφανίζει τους µαθητές που ο βαθµός τους είναι µεγαλύτερος από το µέσο όρο των αποφοίτων.

```python
vath = []
i = 0
sum = 0

while i < 200:
  num = int(input("Δώσε βαθμό: "))
  vath.append(num)
  sum += vath[i]
  i += 1

mo = sum / 200
i = 0

while i < 200:
  if vath[i] > mo:
    print(i)
  i += 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_2.py).

### [Άσκηση 3](source/lecture_05/lecture_05_exercise_3.py)

Ένας μετεωρολόγος καταγράφει τις θερµοκρασίες των ημερών ενός µήνα 30 ημερών που σηµειώθηκαν στο κέντρο µιας πόλης στις 12 το µεσημέρι. Να γίνει πρόγραµµα που θα διαβάζει τις θερµοκρασίες αυτές, θα τις καταχωρεί σε µία λίστα και θα υπολογίζει και θα εµφανίζει την ελάχιστη θερµοκρασία και την ηµέρα που σημειώθηκε καθώς και τη μέγιστη θερµοκρασία και την ηµέρα που σημειώθηκε.

```python
temp = []
i = 0

while i < 30:
  num = int(input("Δώσε θερμοκρασία: "))
  temp.append(num)
  i += 1

maxThesi = 0
minThesi = 0

i = 0

while i < len(temp):
  if temp[i] < temp[minThesi]:
    minThesi = i
  if temp[i] > temp[maxThesi]:
    maxThesi = i
  i += 1

print("Η μέγιστη θερμοκρασία είναι", temp[maxThesi], "την ημέρα", maxThesi)

print("Η ελάχιστη θερμοκρασία είναι", temp[minThesi], "την ημέρα", minThesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_3.py).

### [Άσκηση 4](source/lecture_05/lecture_05_exercise_4.py)

Σε ένα διαγωνισµό πληροφορικής συµµετέχουν 20 µαθητές. Να γραφεί πρόγραµµα το οποίο θα αποθηκεύει σε µία λίστα τα ονόµατα των µαθητών και σε µία άλλη λίστα τους βαθµούς που έλαβε ο κάθε µαθητής στο διαγωνισµό. Το πρόγραµµα θα εµφανίζει το όνοµα του µαθητή που κέρδισε το διαγωνισµό.

```python
names = []
marks = []
i = 0

while i < 20:
  onoma = input ("Δώσε όνομα: ")
  vathmos = int(input("Δώσε βαθμό: "))
  names.append(onoma)
  marks.append(vathmos)
  i += 1

maxThesi = 0
i = 0

while i < len(names):
  if marks[i] > marks[maxThesi]:
    maxThesi = i
  i += 1

print(names[maxThesi])
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_4.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
