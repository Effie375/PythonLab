# 6 Προκαθορισμένη επανάληψη (for loop)

---

## Περιεχόμενα

---

- 6.1 Η εντολή for
- 6.2 Η συνάρτηση range
- 6.3 Αποθήκευση στοιχείων
- 6.4 Άθροισμα στοιχείων
- 6.5 Έυρεση MAX
- 6.6 Έυρεση MIN
- 6.7 Έυρεση MAX με θέση Ι
- 6.8 Έυρεση MAX με θέση ΙΙ
- 6.9 Αναζήτηση στοιχείων I
- 6.10 Αναζήτηση στοιχείων II
- 6.11 Αναζήτηση αριθμού στοιχείων
- 6.12 Ασκήσεις

## 6.1 Η εντολή for

---

Προκαθορισμένος αριθμός επαναλήψεων.

```python
for (Επαναλήπτης) in (Λίστα):
  Εντολές

for item in list:
  print(item)

for i in range(10):
  print(i)
```

## 6.2 Η συνάρτηση range

---

Δημιουργεί ένα είδος λίστας (iterable), το οποίο περιέχει ακέραιους αριθμούς από το start μέχρι το stop.

```python
range([start], stop, [step])
```

- start, ο αριθμός εκκίνησης (Προαιρετικό, Αρχική Τιμή = 0)
- stop, δημιούργησε αριθμούς μέχρι (αλλά χωρίς) τον stop
- step, η διαφορά μεταξύ δύο αριθμών (Προαιρετικό, Αρχική Τιμή = 1)

<!--
## [6.3 Αποθήκευση στοιχείων](source/lecture_06/lecture_06_example_1.py)
-->

## [6.3 Αποθήκευση στοιχείων](source/lecture_06/lecture_06_example_1x.py)

---

<!--
lista = []

for n in range(5):
  num = int(input(f"Δώσε στοιχείο για την {n} θέση: ").strip())
  lista.append(num)

print(lista)
-->

```python
lista = []

for n in range(5):
  num = int(input("Δώσε στοιχείο για την θέση %d: " % n))
  lista.append(num)

print(lista)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_1.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_1x.py).

<!--
## [6.4 Άθροισμα στοιχείων](source/lecture_06/lecture_06_example_2.py)
-->

## [6.4 Άθροισμα στοιχείων](source/lecture_06/lecture_06_example_2x.py)

---

<!--
lista = [1, 5, 6, 3]
athroisma = 0

for item in lista:
  athroisma += item

print(f"Άθροισμα: {athroisma}")
-->

```python
lista = [1, 5, 6, 3]
athroisma = 0

for item in lista:
  athroisma += item

print("Άθροισμα:", athroisma)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_2.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_2x.py).

<!--
## [6.5 Έυρεση MAX](source/lecture_06/lecture_06_example_3.py)
-->

## [6.5 Έυρεση MAX](source/lecture_06/lecture_06_example_3x.py)

---

<!--
lista = [5, 7, 8, 9, 3]

megisto = lista[0]
elaxisto = lista[0]

for item in lista:
  if item > megisto:
    megisto = item

for item in lista:
  if item < elaxisto:
    elaxisto = item

print(f"Μέγιστο: {megisto}")
print(f"Ελάχιστο: {elaxisto}")
-->

```python
lista = [5, 7, 8, 9, 3]

megisto = lista[0]
elaxisto = lista[0]

for item in lista:
  if item > megisto:
    megisto = item

for item in lista:
  if item < elaxisto:
    elaxisto = item

print("Μέγιστο: %d" % megisto)
print("Ελάχιστο: %d" % elaxisto)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_3.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_3x.py).

<!--
## [6.6 Έυρεση MIN](source/lecture_06/lecture_06_example_4.py)
-->

## [6.6 Έυρεση MIN](source/lecture_06/lecture_06_example_4x.py)

---

<!--
maxThesi = 0
thesi = 0

lista = [5, 7, 8, 9, 3]

for item in lista:
  if item > lista[maxThesi]:
    maxThesi = thesi
  thesi += 1

print(f"H maxThesi με τον 1ο τρόπο: {maxThesi}")

for i in range(len(lista)):
  if lista[i] > lista[maxThesi]:
    maxThesi = i

print(f"H maxThesi με τον 2ο τρόπο: {maxThesi}")
-->

```python
maxThesi = 0
thesi = 0

lista = [5, 7, 8, 9, 3]

for item in lista:
  if item > lista[maxThesi]:
    maxThesi = thesi
  thesi += 1

print("H maxThesi με τον 1ο τρόπο: %d" % maxThesi)

for i in range(len(lista)):
  if lista[i] > lista[maxThesi]:
    maxThesi = i

print("H maxThesi με τον 2ο τρόπο: %d" % maxThesi)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_4.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_4x.py).

<!--
## [6.7 Έυρεση MAX με θέση I](source/lecture_06/lecture_06_example_5.py)
-->

## [6.7 Έυρεση MAX με θέση I](source/lecture_06/lecture_06_example_5x.py)

---

<!--
lista = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

for i in range(len(lista)):
  if lista[i] == key:
    thesi = i

print(f"Το {key} βρίσκεται στη {thesi} θέση.")
-->

```python
lista = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

for i in range(len(lista)):
  if lista[i] == key:
    thesi = i

print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_5.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_5x.py).

<!--
## [6.8 Έυρεση MAX με θέση II](source/lecture_06/lecture_06_example_6.py)
-->

## [6.8 Έυρεση MAX με θέση II](source/lecture_06/lecture_06_example_6x.py)

---

<!--
lista = [5, 7, 8, 9, 3]

found = False
i = 0

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

while (i < len(lista)) and (not found):
  if lista[i] == key:
    thesi = i
    found = True
  else:
    i += 1

print(f"Το {key} βρίσκεται στη {thesi} θέση.")
-->

```python
lista = [5, 7, 8, 9, 3]

found = False
i = 0

key = int(input("Δώσε στοιχείο που αναζητάς: "))

while (i < len(lista)) and (not found):
  if lista[i] == key:
    thesi = i
    found = True
  else:
    i += 1

print("Το %d βρίσκεται στη θέση %d." % (key, thesi))
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_6.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_6x.py).

<!--
## [6.9 Αναζήτηση στοιχείων I](source/lecture_06/lecture_06_example_7.py)
-->

## [6.9 Αναζήτηση στοιχείων I](source/lecture_06/lecture_06_example_7x.py)

---

<!--
lista = [8, 7, 8, 9, 3]

counter = 0

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

for k in lista:
  if k == key:
    counter += 1

print(f"Ο αριθμός {key} έχει εισαχθεί {counter} φορές.")
-->

```python
lista = [8, 7, 8, 9, 3]

counter = 0

key = int(input("Δώσε στοιχείο που αναζητάς: "))

for k in lista:
  if k == key:
    counter += 1

print("Ο αριθμός %d έχει εισαχθεί %d φορές." % (key, counter))
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_7.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_7x.py).

<!--
## [6.10 Αναζήτηση στοιχείων II](source/lecture_06/lecture_06_example_8.py)
-->

## [6.10 Αναζήτηση στοιχείων II](source/lecture_06/lecture_06_example_8x.py)

---

<!--
lista = [3, 4, 1, 9, 4, 2]

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
lista = [3, 4, 1, 9, 4, 2]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0

while (i < len(lista)) and (not found):
  if lista[i] == key:
    thesi = i
    found = True
  i += 1

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση: %d" % thesi)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_8.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_8x.py).

<!--
## [6.11 Αναζήτηση αριθμού στοιχείων](source/lecture_06/lecture_06_example_9.py)
-->

## [6.11 Αναζήτηση αριθμού στοιχείων](source/lecture_06/lecture_06_example_9x.py)

---

<!--
lista = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]

key = int(input("Δώσε στοιχείο που αναζητάς: ").strip())

counter = 0

for k in lista:
  if k == key:
    counter += 1

print(f"Το στοιχείο που αναζητάς εμφανίζεται {counter} φορές στη λίστα.")
-->

```python
lista = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

counter = 0

for k in lista:
  if k == key:
    counter += 1

print("Το στοιχείο που αναζητάς εμφανίζεται %d φορές στη λίστα." % counter)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_9.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_9x.py).

## 6.12 Ασκήσεις

---

<!--
### [Άσκηση 1](source/lecture_06/lecture_06_exercise_1.py)
-->

### [Άσκηση 1](source/lecture_06/lecture_06_exercise_1x.py)

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθμούς και να τους εμφανίζει ανάποδα από τη σειρά που διαβάστηκαν.

<!--
lista = []

for i in range(100):
  lista.append(int(input("Δώσε αριθμό: ").strip()))

for i in range(99, -1, -1):
  print(lista[i])
-->

```python
lista = []

for i in range(100):
  lista.append(int(input("Δώσε αριθμό: ")))

for i in range(99, -1, -1):
  print(lista[i])
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_1.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_1x.py).

<!--
### [Άσκηση 2](source/lecture_06/lecture_06_exercise_2.py)
-->

### [Άσκηση 2](source/lecture_06/lecture_06_exercise_2x.py)

Ένα σχολείο έχει 200 μαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τους βαθμούς απολυτηρίου των μαθητών και θα εμφανίζει τους μαθητές που ο βαθμός τους είναι µεγαλύτερος από το µέσο όρο των αποφοίτων.

<!--
vath = []
sum = 0

for i in range(200):
  num = int(input("Δώσε βαθμό: ").strip())
  vath.append(num)
  sum += num

mo = sum / 200

for i in range(200):
  if vath[i] > mo:
    print(i)
-->

```python
vath = []
sum = 0

for i in range(200):
  num = int(input("Δώσε βαθμό: "))
  vath.append(num)
  sum += num

mo = sum / 200

for i in range(200):
  if vath[i] > mo:
    print(i)
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_2.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_2x.py).

<!--
### [Άσκηση 3](source/lecture_06/lecture_06_exercise_3.py)
-->

### [Άσκηση 3](source/lecture_06/lecture_06_exercise_3x.py)

Ένας µετεωρολόγος καταγράφει τις θερμοκρασίες των ημερών ενός μήνα 30 ημερών που σημειώθηκαν στο κέντρο µιας πόλης στις 12 το μεσημέρι. Να γίνει πρόγραµµα που θα διαβάζει τις θερμοκρασίες αυτές, θα τις καταχωρεί σε µία λίστα και θα υπολογίζει και να εκτυπώνει την ελάχιστη θερμοκρασία και την ημέρα που σημειώθηκε καθώς και τη µέγιστη θερμοκρασία και την ημέρα που σημειώθηκε.

<!--
temp = []

for i in range(30):
  num = int(input("Δώσε θερμοκρασία: ").strip())
  temp.append(num)

maxThesi = 0
minThesi = 0

for i in range(len(temp)):
  if temp[i] < temp[minThesi]:
    minThesi = i
  if temp[i] > temp[maxThesi]:
    maxThesi = i

print(f"Η max θερμοκρασία είναι {temp[maxThesi]} την ημέρα {maxThesi + 1}")
print(f"Η min θερμοκρασία είναι {temp[minThesi]} την ημέρα {minThesi + 1}")
-->

```python
temp = []

for i in range(30):
  num = int(input("Δώσε θερμοκρασία: "))
  temp.append(num)

maxThesi = 0
minThesi = 0

for i in range(len(temp)):
  if temp[i] < temp[minThesi]:
    minThesi = i
  if temp[i] > temp[maxThesi]:
    maxThesi = i

print("Η max θερμοκρασία είναι %d την ημέρα %d" % (temp[maxThesi], (maxThesi + 1)))
print("Η min θερμοκρασία είναι %d την ημέρα %d" % (temp[minThesi], (minThesi + 1)))
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_3.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_3x.py).

<!--
### [Άσκηση 4](source/lecture_06/lecture_06_exercise_4.py)
-->

### [Άσκηση 4](source/lecture_06/lecture_06_exercise_4x.py)

Σε ένα διαγωνισμό πληροφορικής συµµετέχουν 20 µαθητές. Να γραφεί πρόγραµµα το οποίο θα αποθηκεύει σε µία λίστα τα ονόματα των µαθητών και σε µία λίστα τους βαθμούς που έλαβε ο κάθε µαθητής στο διαγωνισμό. Το πρόγραµµα θα εμφανίζει το όνομα του µαθητή που κέρδισε το διαγωνισμό.

<!--
names = []
marks = []

for i in range(20):
  onoma = input("Δώσε όνομα: ").strip()
  vathmos = int(input("Δώσε βαθμό: ").strip())
  names.append(onoma)
  marks.append(vathmos)

maxThesi = 0

for i in range(len(names)):
  if marks[i] > marks[maxThesi]:
    maxThesi = i

print(names[maxThesi])
-->

```python
names = []
marks = []

for i in range(20):
  onoma = input("Δώσε όνομα: ")
  vathmos = int(input("Δώσε βαθμό: "))
  names.append(onoma)
  marks.append(vathmos)

maxThesi = 0

for i in range(len(names)):
  if marks[i] > marks[maxThesi]:
    maxThesi = i

print(names[maxThesi])
```

<!--
Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_4.py).
-->

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_4x.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
