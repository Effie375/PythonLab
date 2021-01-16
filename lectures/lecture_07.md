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

## [Αναζήτηση στοιχείων I](source/lecture_07/lecture_07_example_1.py)

---

```python
list = [9, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

thesi = 0

for i in list:
  if i == key:
     print(thesi)
  thesi += 1

k = 0

for i in list: 
  if i == key:
    k += 1

print("Το %d έχει εισαχθεί %d φορές." % (key, k))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_1.py).

## [Αναζήτηση στοιχείων II](source/lecture_07/lecture_07_example_2.py)

---

```python
list = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: "))

counter = 0

for i in list: 
  if i == key:
    counter += 1

print("Το %d έχει εισαχθεί %d φορές." % (key, counter))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_2.py).

## [Αναζήτηση στοιχείων III](source/lecture_07/lecture_07_example_3.py)

---

```python
key = int(input("Δώσε στοιχείο που αναζητάς: "))

found = False
i = 0

while (i < 5) and (found == False):
  if list[i] == key:
    thesi = i
    found = True
  i += 1

if found == True:
  print("Το %d βρίσκεται στη %d θέση." % (key, thesi))
else:
  print("Το %d δε βρίσκεται στη λίστα %s." % (key, list))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_3.py).

## [7.4 Ταξινόμηση - Bubble Sort](source/lecture_07/lecture_07_example_4.py)

---

```python
A = [5, 7, 8, 9, 3]

print("Η λίστα μας πριν τη ταξινόμηση είναι: %s" % A)

for i in range(len(A)):
  for j in range(len(A)-1, i, -1):
    if A[j-1] > A[j]:
      temp = A[j-1]
      A[j-1] = A[j]
      A[j] = temp

print("Η λίστα μας μετά τη ταξινόμηση είναι: %s" %A)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_4.py).

## [7.5 Ταξινόμηση - Διπλή αντιμετάθεση](source/lecture_07/lecture_07_example_5.py)

---

```python
Names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
Grades = [1, 2, 5, 7, 9]


for i in range(1, 5):
  for j in range(4, i-1, -1):
    if Grades[j-1] > Grades[j]:
      temp = Grades[j-1]
      Grades[j-1] = Grades[j]
      Grades[j] = temp
      temp2 = Names[j-1]
      Names[j-1] = Names[j]
      Names[j] = temp2

print(Names)
print(Grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_5.py).

## [7.6 Διπλή ταξινόμηση](source/lecture_07/lecture_07_example_6.py)

---

```python
for i in range(1, 5):
  for j in range(4, i-1, -1):
    if Grades[j-1] > Grades[j]:
      temp=Grades[j-1]
      Grades[j-1]=Grades[j]
      Grades[j]=temp
      temp2=Names[j-1]
      Names[j-1]=Names[j]
      Names[j]=temp2
    if Grades[j-1] == Grades[j]:
      if Names[j-1] > Names[j]:
        temp3=Names[j-1]
        Names[j-1]=Names[j]
        Names[j]=temp3

print(Names)
print(Grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_example_6.py).

## 7.7 Ασκήσεις

---

## [Άσκηση 1](source/lecture_07/lecture_07_exercise_1.py)

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθµούς και να εµφανίζει τον µέγιστο και τον ελάχιστο µε χρήση ταξινόµησης.

```python
MAX_NUMBERS = 100
list = []

for i in range(MAX_NUMBERS):
  num = int(input("Δώσε αριθμό: "))
  list.append(num)


for index in range(len(list)-1):
  for j in range(len(list)-1, index, -1):
    if list[j-1] > list[j]:
      temp = list[j-1]
      list[j-1] = list[j]
      list[j] = temp


print("\nΟ μεγαλύτερος αριθμός είναι το", list[len(list)-1])
print("Ο μικρότερος αριθμός είναι το", list[0])
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_exercise_1.py).

## [Άσκηση 2](source/lecture_07/lecture_07_exercise_2.py)

Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τα ονόµατα και τους βαθµούς απολυτηρίου των µαθητών και θα εµφανίζει τα ονόµατα των τριών καλύτερων µαθητών.

```python
# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 200
BEST_FOITITES = 3
counter = 0
vathmoi = []
names = []

while counter < MAX_ELEMENTS:
  name = input("Δώσε όνομα μαθητή: ")
  vathmos = int(input("Δώσε βαθμό: "))
  # Εισαγωγή στοιχείων στη λίστα των φοιτητών και των βαθμών
  names.append(name)
  vathmoi.append(vathmos)
  counter += 1


for i in range(len(vathmoi)-1):
  for j in range(len(vathmoi)-1, i,-1):
    if vathmoi[j-1] < vathmoi[j]:
      # Swap vathmous
      temp1 = vathmoi[j-1]
      vathmoi[j-1] = vathmoi[j]
      vathmoi[j] = temp1
      # Swap names
      temp2 = names[j-1]
      names[j-1] = names[j]
      names[j] = temp2

for i in range(BEST_FOITITES):
  print("Ο %dος καλύτερος είναι ο/η %s." % (i+1, names[i]))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_07/lecture_07_exercise_2.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md) | [Lect 10](lecture_10.md)
