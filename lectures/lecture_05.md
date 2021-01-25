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

<!--
## [5.2 Αποθήκευση στοιχείων](source/lecture_05/lecture_05_example_1.py)
-->

## [5.2 Αποθήκευση στοιχείων](source/lecture_05/lecture_05_example_1x.py)

---

<!--
MAX_ELEMENTS = 5
lista = []
i = 0

while i < MAX_ELEMENTS:
  num = int(input(f"Δώσε στοιχείο για την {i} θέση: ").strip())
  lista.append(num)
  i += 1

print(f"Η λίστα μας είναι: {lista}")
-->

```python
MAX_ELEMENTS = 5
lista = []
i = 0

while i < MAX_ELEMENTS:
  num = int(input("Δώσε στοιχείο για την θέση %d: " % i))
  lista.append(num)
  i += 1

print("Η λίστα μας είναι: %s" % lista)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_1.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_1x.py).

<!--
## [5.3 Άθροισμα στοιχείων](source/lecture_05/lecture_05_example_2.py)
-->

## [5.3 Άθροισμα στοιχείων](source/lecture_05/lecture_05_example_2x.py)

---

<!--
lista = [5, 7, 8, 9, 3]
athroisma = 0
i = 0

while i < len(lista):
  athroisma += lista[i]
  i += 1

print(f"Άθροισμα: {athroisma}")
-->

```python
lista = [5, 7, 8, 9, 3]
athroisma = 0
i = 0

while i < len(lista):
  athroisma += lista[i]
  i += 1

print("Άθροισμα: %d" % athroisma)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_2.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_2x.py).

<!--
## [5.4 Έυρεση MAX](source/lecture_05/lecture_05_example_3.py)
-->

## [5.4 Έυρεση MAX](source/lecture_05/lecture_05_example_3x.py)

---

<!--
lista = [5, 7, 8, 9, 3]
elaxisto = lista[0]
megisto = lista[0]
i = 0

while i < len(lista):
  if lista[i] > megisto:
    megisto = lista[i]
  i += 1

print(f"Ο μέγιστος αριθμός είναι το: {megisto}")

i = 0

while i < len(lista):
  if lista[i] < elaxisto:
    elaxisto = lista[i]
  i += 1

print(f"Ο ελάχιστος αριθμός είναι το: {elaxisto}")
-->

```python
lista = [5, 7, 8, 9, 3]
elaxisto = lista[0]
megisto = lista[0]
i = 0

while i < len(lista):
  if lista[i] > megisto:
    megisto = lista[i]
  i += 1

print("Ο μέγιστος αριθμός είναι το: %d" % megisto)

i = 0

while i < len(lista):
  if lista[i] < elaxisto:
    elaxisto = lista[i]
  i += 1

print("Ο ελάχιστος αριθμός είναι το: %d" % elaxisto)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_3.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_3x.py).

<!--
## [5.5 Έυρεση MIN](source/lecture_05/lecture_05_example_4.py)
-->

## [5.5 Έυρεση MIN](source/lecture_05/lecture_05_example_4x.py)

---

<!--
lista = [3, 4, 1, 9, 7, 2]
elaxisto = lista[0]
i = 0

while i < len(lista):
  if lista[i] < elaxisto:
    elaxisto = lista[i]
  i += 1

print(f"Ελάχιστο: {elaxisto}")
-->

```python
lista = [3, 4, 1, 9, 7, 2]
elaxisto = lista[0]
i = 0

while i < len(lista):
  if lista[i] < elaxisto:
    elaxisto = lista[i]
  i += 1

print("Ελάχιστο:", elaxisto)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_4.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_4x.py).

<!--
## [5.6 Έυρεση MAX με θέση](source/lecture_05/lecture_05_example_5.py)
-->

## [5.6 Έυρεση MAX με θέση](source/lecture_05/lecture_05_example_5x.py)

---

<!--
lista = [3, 4, 1, 9, 4, 2]
maxThesi = 0
i = 0

while i < len(lista):
  if lista[i] > lista[maxThesi]:
    maxThesi = i
  i += 1

print(f"Μέγιστη θέση: {maxThesi}")
-->

```python
lista = [3, 4, 1, 9, 4, 2]
maxThesi = 0
i = 0

while i < len(lista):
  if lista[i] > lista[maxThesi]:
    maxThesi = i
  i += 1

print("Μέγιστη θέση:", maxThesi)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_5.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_5x.py).

<!--
## [5.7 Αναζήτηση στοιχείων I](source/lecture_05/lecture_05_example_6.py)
-->

## [5.7 Αναζήτηση στοιχείων I](source/lecture_05/lecture_05_example_6x.py)

---

<!--
list = [3, 4, 1, 9, 4, 2]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())
i = 0

while i < len(list):
  if key == list[i]:
    thesi = i
  i += 1

print(f"Το στοιχείο που αναζητάς βρίσκεται στη θέση: {thesi}")
-->

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

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_6.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_6x.py).

<!--
## [5.8 Αναζήτηση στοιχείων II](source/lecture_05/lecture_05_example_7.py)
-->

## [5.8 Αναζήτηση στοιχείων II](source/lecture_05/lecture_05_example_7x.py)

---

<!--
lista = [3, 4, 1, 9, 7, 2]
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())
found = False
i = 0

while (i < len(lista)) and (not found):
  if lista[i] == key:
    thesi = i
    found = True
  i += 1

print(f"Το στοιχείο που αναζητάς βρίσκεται στη θέση: {thesi}")
-->

```python
lista = [3, 4, 1, 9, 7, 2]
key = int(input("Δώσε στοιχείο που αναζητάς: "))
found = False
i = 0

while (i < len(lista)) and (not found):
  if lista[i] == key:
    thesi = i
    found = True
  i += 1

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_7.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_7x.py).

<!--
## [5.9 Αναζήτηση αριθμού στοιχείων](source/lecture_05/lecture_05_example_8.py)
-->

## [5.9 Αναζήτηση αριθμού στοιχείων](source/lecture_05/lecture_05_example_8x.py)

---

<!--
list = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]
key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())
counter = 0
i = 0

while i < len(list):
  if list[i] == key:
    counter += 1
  i += 1

print(f"Το στοιχείο που αναζητάς εμφανίζεται {counter} φορές στη λίστα.")
-->

```python
list = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]
key = int(input("Δώσε στοιχείο που αναζητάς: "))
counter = 0
i = 0

while i < len(list):
  if list[i] == key:
    counter += 1
  i += 1

print("Το στοιχείο που αναζητάς εμφανίζεται %d φορές στη λίστα." % counter)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_8.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_example_8x.py).

## 5.10 Ασκήσεις

---

<!--
### [Άσκηση 1](source/lecture_05/lecture_05_exercise_1.py)
-->

### [Άσκηση 1](source/lecture_05/lecture_05_exercise_1x.py)

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθµούς και να τους εµφανίζει ανάποδα από τη σειρά που διαβάστηκαν.

<!--
MAX_ELEMENTS = 100
neaLista = []
lista = []
i = 0

while i < MAX_ELEMENTS:
  num = int(input("Δώσε έναν αριθμό: ").strip())
  lista.append(num)
  i += 1

j = len(lista)

while j > 0:
  neaLista.append(lista[j - 1])
  j -= 1

print(f"Η νέα λίστα είναι {neaLista}.")
-->

```python
MAX_ELEMENTS = 100
neaLista = []
lista = []
i = 0

while i < MAX_ELEMENTS:
  num = int(input("Δώσε έναν αριθμό: "))
  lista.append(num)
  i += 1

j = len(lista)

while j > 0:
  neaLista.append(lista[j - 1])
  j -= 1

print("Η νέα λίστα είναι %s." % neaLista)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_1.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_1x.py).

<!--
### [Άσκηση 2](source/lecture_05/lecture_05_exercise_2.py)
-->

### [Άσκηση 2](source/lecture_05/lecture_05_exercise_2x.py)

Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τους βαθµούς απολυτηρίου των µαθητών και θα εµφανίζει τους µαθητές που ο βαθµός τους είναι µεγαλύτερος από το µέσο όρο των αποφοίτων.

<!--
MAX_STUDENTS = 200
sum = i = 0
grades = []
stund = []

while i < MAX_STUDENTS:
  name = input("Δώσε το όνομά σου: ").strip()
  grad = int(input("Δώσε τον βαθμό σου: ").strip())
  stund.append(name)
  grades.append(grad)
  sum += grad
  i += 1

# Να ελέγξετε τη διαίρεση με μηδέν!
average = sum / i

i = 0

while i < len(grades):
  if grades[i] > average:
    print(f"Οι μαθητές που έχουν υψηλές βαθμολογίες είνα: {stund[i]}")
  i += 1
-->

```python
MAX_STUDENTS = 200
sum = i = 0
grades = []
stund = []

while i < MAX_STUDENTS:
  name = input("Δώσε το όνομά σου: ")
  grad = int(input("Δώσε τον βαθμό σου: "))
  stund.append(name)
  grades.append(grad)
  sum += grad
  i += 1

# Να ελέγξετε τη διαίρεση με μηδέν!
average = sum / i

i = 0

while i < len(grades):
  if grades[i] > average:
    print("Οι μαθητές που έχουν υψηλές βαθμολογίες είνα: %s" % stund[i])
  i += 1
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_2.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_2x.py).

<!--
### [Άσκηση 3](source/lecture_05/lecture_05_exercise_3.py)
-->

### [Άσκηση 3](source/lecture_05/lecture_05_exercise_3x.py)

Ένας μετεωρολόγος καταγράφει τις θερµοκρασίες των ημερών ενός µήνα 30 ημερών που σηµειώθηκαν στο κέντρο µιας πόλης στις 12 το µεσημέρι. Να γίνει πρόγραµµα που θα διαβάζει τις θερµοκρασίες αυτές, θα τις καταχωρεί σε µία λίστα και θα υπολογίζει και θα εµφανίζει την ελάχιστη θερµοκρασία και την ηµέρα που σημειώθηκε καθώς και τη μέγιστη θερµοκρασία και την ηµέρα που σημειώθηκε.

<!--
MAX_TEMP = 30
max = 0
min = 0
i = 0
temps = []

while i < MAX_TEMP:
  tem = int(input("Δώσε μια θερμοκρασία: ").strip())
  temps.append(tem)
  i += 1

i = 0

while i < len(temps):
  if temps[i] > temps[max]:
    max = i
  elif temps[i] < temps[min]:
    min = i
  i += 1

print(f"Η χαμηλότερη θερμοκρασία ήταν {temps[min]} βαθμούς την {min + 1} μέρα.")
print(f"Η υψηλότερη θερμοκρασία ήταν {temps[max]} βαθμούς την  {max + 1} μέρα.")
-->

```python
MAX_TEMP = 30
max = 0
min = 0
i = 0
temps = []

while i < MAX_TEMP:
  tem = int(input("Δώσε μια θερμοκρασία: "))
  temps.append(tem)
  i += 1

i = 0

while i < len(temps):
  if temps[i] > temps[max]:
    max = i
  elif temps[i] < temps[min]:
    min = i
  i += 1

print("Η χαμηλότερη θερμοκρασία ήταν %d βαθμούς την %d μέρα." % (temps[min], (min + 1)))
print("Η υψηλότερη θερμοκρασία ήταν %d βαθμούς την  %d μέρα." % (temps[max], (max + 1)))
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_3.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_3x.py).

<!--
### [Άσκηση 4](source/lecture_05/lecture_05_exercise_4.py)
-->

### [Άσκηση 4](source/lecture_05/lecture_05_exercise_4x.py)

Σε ένα διαγωνισµό πληροφορικής συµµετέχουν 20 µαθητές. Να γραφεί πρόγραµµα το οποίο θα αποθηκεύει σε µία λίστα τα ονόµατα των µαθητών και σε µία άλλη λίστα τους βαθµούς που έλαβε ο κάθε µαθητής στο διαγωνισµό. Το πρόγραµµα θα εµφανίζει το όνοµα του µαθητή που κέρδισε το διαγωνισµό.

<!--
MAX_STUDENTS = 20
student_list = []
grades_list = []
maxIndex = 0
i = 0

while i < MAX_STUDENTS:
  student = input("Δώσε το όνομά σου: ").strip()
  student_list.append(student)
  grad = int(input("Δώσε τον βαθμό σου: ").strip())
  grades_list.append(grad)
  i += 1

i = 0

while i < len(grades_list):
  if grades_list[i] > grades_list[maxIndex]:
    maxIndex = i
  i += 1

print(f"{student_list[maxIndex]} κέρδισε με βαθμό {grades_list[maxIndex]}.")
-->

```python
MAX_STUDENTS = 20
student_list = []
grades_list = []
maxIndex = 0
i = 0

while i < MAX_STUDENTS:
  student = input("Δώσε το όνομά σου: ")
  student_list.append(student)
  grad = int(input("Δώσε τον βαθμό σου: "))
  grades_list.append(grad)
  i += 1

i = 0

while i < len(grades_list):
  if grades_list[i] > grades_list[maxIndex]:
    maxIndex = i
  i += 1

print("%s κέρδισε με βαθμό %d." % (student_list[maxIndex], grades_list[maxIndex]))
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_4.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_05/lecture_05_exercise_4x.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
