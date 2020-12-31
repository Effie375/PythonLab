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

## [6.3 Αποθήκευση στοιχείων](source/lecture_06/lecture_06_example_1.py)

---

```python
list = []
for n in range(5):
  num = int(input("Δώσε στοιχείο για την θέση %d: " % n))
  list.append(num)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_1.py).

## [6.4 Άθροισμα στοιχείων](source/lecture_06/lecture_06_example_2.py)

---

```python
list = [1, 5, 6, 3]
sum = 0

for item in list:
  sum += item

print("Άθροισμα:", sum)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_2.py).

## [6.5 Έυρεση MAX](source/lecture_06/lecture_06_example_3.py)

---

```python
list = [1, 4, 6, 9, 7, 2]
megisto = list[0]

for item in list:
  if item > megisto:
    megisto = item

print("Μέγιστο:", megisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_3.py).

[![Video 2](../images/Video_1.PNG)](https://www.youtube.com/watch?v=fWRJpy46Taw&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=17)

## [6.6 Έυρεση MIN](source/lecture_06/lecture_06_example_4.py)

---

```python
list = [1, 4, 6, 9, 7, 2]
elaxisto = list[0]

for item in list:
  if item < elaxisto:
    elaxisto = item

print("Ελάχιστο:", elaxisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_4.py).

[![Video 2](../images/Video_1.PNG)](https://www.youtube.com/watch?v=tvqc83gCffg&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=18&t=35s)

## [6.7 Έυρεση MAX με θέση I](source/lecture_06/lecture_06_example_5.py)

---

```python
list = [3, 4, 1, 9, 4, 2]
maxThesi = 0
thesi = 0

for item in list:
  if item > list[maxThesi]:
    maxThesi = thesi
  thesi += 1

print("Μέγιστη θέση:", maxThesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_5.py).

## [6.8 Έυρεση MAX με θέση II](source/lecture_06/lecture_06_example_6.py)

---

```python
list = [3, 4, 1, 9, 4, 2]
maxThesi = 0

for i in range(len(list)):
  if list[i] > list[maxThesi]:
    maxThesi = i

print("Μέγιστη θέση:", maxThesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_6.py).

## [6.9 Αναζήτηση στοιχείων I](source/lecture_06/lecture_06_example_7.py)

---

```python
list = [3, 4, 1, 9, 4, 2]
key = int(input(("Δώσε στοιχείο που αναζητάς: "))

for i in range(len(list)):
  if list[i] == key:
    thesi = i

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_7.py).

## [6.10 Αναζήτηση στοιχείων II](source/lecture_06/lecture_06_example_8.py)

---

```python
list = [3, 4, 1, 9, 4, 2]
key = int(input(("Δώσε στοιχείο που αναζητάς: "))
found = False
i = 0

while (i < len(list)) and (not found):
  if list[i] == key:
    thesi = i
    found = True
  i+=1

print("Το στοιχείο που αναζητάς βρίσκεται στη θέση:", thesi)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_8.py).

## [6.11 Αναζήτηση αριθμού στοιχείων](source/lecture_06/lecture_06_example_9.py)

---

```python
list = [3, 4, 1, 9, 7, 2, 1, 4, 5, 1]
key = int(input(("Δώσε στοιχείο που αναζητάς: "))
counter = 0

for k in list:
  if k == key:
    counter += 1

print("Το στοιχείο που αναζητάς εμφανίζεται", counter, "φορές στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_example_9.py).

## 6.12 Ασκήσεις

---

### [Άσκηση 1](source/lecture_06/lecture_06_exercise_1.py)

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθμούς και να τους εμφανίζει ανάποδα από τη σειρά που διαβάστηκαν.

```python
list = []

for i in range(100):
  list.append(int(input("Δώσε αριθμό: ")))

for i in range(99, -1, -1):
  print(list[i])
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_1.py).

### [Άσκηση 2](source/lecture_06/lecture_06_exercise_2.py)

Ένα σχολείο έχει 200 μαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τους βαθμούς απολυτηρίου των μαθητών και θα εμφανίζει τους μαθητές που ο βαθμός τους είναι µεγαλύτερος από το µέσο όρο των αποφοίτων.

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

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_2.py).

### [Άσκηση 3](source/lecture_06/lecture_06_exercise_3.py)

Ένας µετεωρολόγος καταγράφει τις θερμοκρασίες των ημερών ενός μήνα 30 ημερών που σημειώθηκαν στο κέντρο µιας πόλης στις 12 το μεσημέρι. Να γίνει πρόγραµµα που θα διαβάζει τις θερμοκρασίες αυτές, θα τις καταχωρεί σε µία λίστα και θα υπολογίζει και να εκτυπώνει την ελάχιστη θερμοκρασία και την ημέρα που σημειώθηκε καθώς και τη µέγιστη θερμοκρασία και την ημέρα που σημειώθηκε.

```python
temp = []

for i in range(30):
  num = int(input("Δώσε θερμοκρασία: "))
  temp.append(num)

maxThesi = 0
minThesi = 0

for i in range(len(temp)):
  if temp[i]< temp[minThesi]:
    minThesi = i
  if temp[i]> temp[maxThesi]:
    maxThesi = i

print("Η μέγιστη θερμοκρασία είναι ", temp[maxThesi], "την ημέρα", maxThesi + 1)
print("Η ελάχιστη θερμοκρασία είναι ", temp[minThesi], "την ημέρα", minThesi + 1)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_3.py).

### [Άσκηση 4](source/lecture_06/lecture_06_exercise_4.py)

Σε ένα διαγωνισμό πληροφορικής συµµετέχουν 20 µαθητές. Να γραφεί πρόγραµµα το οποίο θα αποθηκεύει σε µία λίστα τα ονόματα των µαθητών και σε µία λίστα τους βαθμούς που έλαβε ο κάθε µαθητής στο διαγωνισμό. Το πρόγραµµα θα εμφανίζει το όνομα του µαθητή που κέρδισε το διαγωνισμό.

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

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_06/lecture_06_exercise_4.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
