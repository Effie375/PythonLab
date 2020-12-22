# 7 Εντολή επανάληψης - for

---

## Περιεχόμενα

---

- 7.1 Εντολή επανάληψης - for
- 7.2 Παραδείγματα
- 7.3 Ασκήσεις

## 7.1 Εντολή επανάληψης - for

---

```python
for i in list:
    ...E1
    ...E2
```

Η μεταβλητή i, σε κάθε επανάληψη, θα παίρνει την επομένη τιμήτης λίστας list.

```python
for i in range([start], stop, [step]):
    ...E1
    ...E2
```

- start, ο αριθμός εκκίνησης (Προαιρετικό,ΑρχικήΤιμή = 0)
- stop, δημιούργησε αριθμούς μέχρι (αλλά χωρίς) τον stop
- step, η διαφορά μεταξύ δύο αριθμών (Προαιρετικό, Αρχική Τιμή = 1)

## 7.2 Παραδείγματα

---

### [7.2.1 Παράδειγμα 1](source/lab_07/lab_07_example_1.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται έναν αριθμό και θα τυπώνει το άθροισμα όλων των ακεραίων μέχρι και αυτόν τον αριθμό.

```python
athroisma = 0

number = int(input("Δώσε αριθμό: "))

for i in range(number + 1):
  athroisma = athroisma + i

print(athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_example_1.py)

### [7.2.2 Παράδειγμα 2](source/lab_07/lab_07_example_2.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται έναν αριθμό και θα ελέγχει εάν είναι πρώτος.(Πρώτος είναι ένας αριθμός που διαιρείται μόνο από το 1 και τον εαυτό του).

```python
prime = True

number = int(input("Δώσε αριθμό: "))

for i in range(2, number // 2 + 1):
  if number % i == 0:
    prime = False

print(prime)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_example_2.py)

### [7.2.3 Παράδειγμα 3](source/lab_07/lab_07_example_3.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται μία λέξη και θα μετράει πόσες φορές περιέχει το γράμμα 'e'.

```python
e_counter = 0

word = input("Δώσε λέξη: ")

for i in word:
  if i == 'e':
    e_counter += 1

print(e_counter)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_example_3.py)

## 7.3 Ασκήσεις

---

### [Άσκηση 1](source/lab_07/lab_07_exercise_1.py)

Μία αθλήτρια του στίβου αγωνίστηκε στο έπταθλο. Να γραφεί πρόγραμμα που θα διαβάζει τη βαθμολογία σε κάθε ένα από τα 7 αθλήματα που συμμετείχε (ο βαθμός είναι ακέραιος αριθμός μεταξύ 0- 20). Για να βγει η τελική βαθμολογία κάθε αθλήματος, η βαθμολογία του πρώτου αθλήματος πολλαπλασιάζεται με το 5, του δεύτερου αθλήματος με το 10, του τρίτου με το 15, του τετάρτου με το 20, του πέμπτου με το 25, του έκτου με το 30 και του έβδομου με το 35. Ο τελικός βαθμός είναι ο μέσος όρος της τελικής βαθμολογίας των επτά αθλημάτων. Το πρόγραμμα να εμφανίζει τον τελικό βαθμό.

```python
sum = 0
l = []

for i in range(7):
  vathmos=int(input("Δώσε βαθμό: "))
  l.append(vathmos)

k = 1 

for i in l: 
  i = i * 5 * k 
  k = k + 1 
  um = sum + i 
mo = sum / 7

print("Ο μέσος όρος είναι", mo)

# Εναλλακτικά k = 5
# for i in l:
  # i = i * k
  # k = k + 5
  # sum = sum + i
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_exercise_1.py)

### [Άσκηση 2](source/lab_07/lab_07_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει 10 αριθμούς. Μετά θα δέχεται έναν αριθμό και θα εμφανίζει στον χρήστη ποιοι από τους αριθμούς που εισήχθησαν διαιρούνται από αυτόν.

```python
arithmoi = []

for i in range(10):
  arithmoi.append(int(input("Δώσε αριθμό: ")))

num = int(input("Δώσε αριθμό για έλεγχο διαιρετέων: "))

for i in arithmoi:
  if i % num == 0:
    print(i)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_exercise_2.py)

### [Άσκηση 3](source/lab_07/lab_07_exercise_3.py)

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από τον χρήστη έναν αριθμό ν και θα εμφανίζει τους πρώτους αριθμούς μεταξύ 1 – ν.

```python
limit = int(input("Δώσε αριθμό: "))

for i in range(1,limit+1):
  prime = True
  for j in range(2, i//2+1):
    if i % j == 0:
      prime = False
    if prime:
      print(i)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_exercise_3.py)

### [Άσκηση 4](source/lab_07/lab_07_exercise_4.py)

Να γραφεί ένα πρόγραμμα που θα δέχεται από τον χρήστη μια λέξη και θα εμφανίζει πόσες φορές εμφανίστηκε το κάθε γράμμα.

```python
leksi = input("Δώσε λέξη: ")

leksi = leksi.lower()

grammata = "abcdefghijklmnopqrstuvwxyz"

for letter in grammata:
  counter = 0
  for grammaLeksis in leksi:
    if grammaLeksis == letter:
      counter += 1
  print("To γράμμα %s εμφανίστηκε %d φορές." % (letter, counter))
 counter = 0
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_exercise_4.py)

### [Άσκηση 5](source/lab_07/lab_07_exercise_5.py)

Να γραφεί ένα πρόγραμμα που θα δέχεται έναν αριθμό Ν και θα επιστρέφει τον Ν-οστο αριθμό Fibonacci. Στον παρακάτω πίνακα μπορείτε να δείτε τον αριθμό που επιστρέφει η ακολουθία Fibonacci ανάλογα τον αριθμό που δίνουμε.

![Fibonacci 1](../images/fibonacci_1.PNG)

Ένας αριθμός Fibonacci υπολογίζεται από τον τύπο:

![Fibonacci 2](../images/fibonacci_2.PNG)

```python
fib_no = (input("Δώσε αριθμό Fibonacci:"))
while not fib_no.isdigit():
  fib_no = (input("Είπα δώσε αριθμό Fibonacci:"))

fib_no = int(fib_no)

fib_minus_2 = 0
fib_minus_1 = 1

if fib_no == 1:
  fib = 1
elif fib_no == 0:
  fib = 0
else:
  for i in range(fib_no-1):
    fib = fib_minus_1 + fib_minus_2
    fib_minus_2 = fib_minus_1
    fib_minus_1 = fib

print(fib)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_07/lab_07_exercise_5.py)

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)
