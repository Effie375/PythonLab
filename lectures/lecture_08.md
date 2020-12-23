# 8 Μονοδιάστατες λίστες - Αναζήτηση - Ταξινόμηση

---

## Περιεχόμενα

---

- 8.1 Αναζήτηση στοιχείων I
- 8.2 Αναζήτηση στοιχείων II
- 8.3 Αναζήτηση στοιχείων III
- 8.4 Ταξινόμηση - Bubble Sort
- 8.5 Ταξινόμηση - Διπλή αντιμετάθεση
- 8.6 Διπλή ταξινόμηση
- 8.7 Ασκήσεις

## [Αναζήτηση στοιχείων I](source/lecture_08/lecture_08_example_1.py)

---

```python
list = [9,7,8,9,3]

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

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_1.py).

## [Αναζήτηση στοιχείων II](source/lecture_08/lecture_08_example_2.py)

---

```python
list = [5, 7, 8, 9, 3]

key = int(input("Δώσε στοιχείο που αναζητάς: ")

counter = 0

for i in list: 
  if i == key:
    counter += 1

print("Το %d έχει εισαχθεί %d φορές." % (key, counter))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_2.py).

## [Αναζήτηση στοιχείων III](source/lecture_08/lecture_08_example_3.py)

---

```python
key = int(input("Δώσε στοιχείο που αναζητάς: ")

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

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_3.py).

## [8.4 Ταξινόμηση - Bubble Sort](source/lecture_08/lecture_08_example_4.py)

---

```python
A = [5, 7, 8, 9, 3]

print("Η λίστα μας πριν τη ταξινόμηση είναι: %s" % A)

for i in range(len(A)):
  for j in range(len(A)-1,i,-1):
    if A[j-1] > A[j]:
      temp = A[j-1]
      A[j-1] = A[j]
      A[j] = temp

print("Η λίστα μας μετά τη ταξινόμηση είναι: %s" %A)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_4.py).

## [8.5 Ταξινόμηση - Διπλή αντιμετάθεση](source/lecture_08/lecture_08_example_5.py)

---

```python
Names = ["Γεωργίου", "Πέτρου", "Παπαδόπουλος", "Αθανασίου", "Τσακογιάννης"]
Grades = [1, 2, 5, 7, 9]


for i in range(1, 5):
  for j in range(4, i-1, -1):
    if Grades[j-1] > Grades[j]:
      temp=Grades[j-1]
      Grades[j-1]=Grades[j]
      Grades[j]=temp
      temp2=Names[j-1]
      Names[j-1]=Names[j]
      Names[j]=temp2

print(Names)
print(Grades)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_5.py).

## [8.6 Διπλή ταξινόμηση](source/lecture_08/lecture_08_example_6.py)

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

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_6.py).

## 8.7 Ασκήσεις

---

## [Άσκηση 1](source/lecture_08/lecture_08_exercise_1.py)

Να γραφεί πρόγραµµα που να διαβάζει 100 ακεραίους αριθµούς και να εµφανίζει τον µέγιστο και τον ελάχιστο µε χρήση ταξινόµησης.

```python
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_exercise_1.py).

## [Άσκηση 2](source/lecture_08/lecture_08_exercise_2.py)

Ένα σχολείο έχει 200 µαθητές στην Γ’ τάξη λυκείου. Να γίνει πρόγραµµα το οποίο θα διαβάζει τα ονόµατα και τους βαθµούς απολυτηρίου των µαθητών και θα εµφανίζει τα ονόµατα των τριών καλύτερων µαθητών.

```python
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_exercise_2.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
