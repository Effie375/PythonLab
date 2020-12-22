# 9 Αναζήτηση - Ταξινόμηση

---

## Περιεχόμενα

---

- 9.1 Αναζήτηση στοιχείων
- 9.2 Ταξινόμηση
- 9.3 Παράδειγμα ταξινόμησης
- 9.4 Ασκήσεις

## [9.1 Αναζήτηση στοιχείων](source/lab_09/lab_09_example_1.py)

---

```python
key = int(input("Δώσε στοιχείο που αναζητάς: "))

done = True
thesi = 0

for i in list:
  if i == key:
    print(thesi)
    done = False
  thesi += 1

if done == True:
  print("Το στοιχείο που αναζητάς δεν είναι στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_example_1.py).

## [9.2 Ταξινόμηση](source/lab_09/lab_09_example_2.py)

---

```python
# Δημιουργία λίστας
list = [4,8,3,1,7]

for i in range(1,5):
  for j in range(4, i-1, -1):
    if list[j-1] > list[j]:
      temp = list[j-1]
      list[j-1] = list[j]
      list[j] = temp

# Εκτύπωση ταξινομημένης λίστας
print("Η ταξινομημένη λίστα μας είναι:", list)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_example_2.py).

## [9.3 Παράδειγμα ταξινόμησης](source/lab_09/lab_09_example_3.py)

---

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται πέντε αριθμούς, θα τους ταξινομεί σε αύξουσα σειρά και θα τους εμφανίζει.

```python
list = []

for i in range(5):
  num = int(input("Δώσε στοιχείο: "))
  list.append(num)

print(list)

for i in range(1,5):
  for j in range(4, i-1, -1):
    if list[j-1] > list[j]:
      temp = list[j-1]
      list[j-1] = list[j]
      list[j] = temp
      
print(list)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_example_3.py).

## 9.4 Ασκήσεις

---

### [Άσκηση 1](source/lab_09/lab_09_exercise_1.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει 10 ακεραίους αριθμούς και έπειτα θα ζητά έναν ακέραιο τον οποίο θα αναζητά και αν υπάρχει θα εμφανίζει τη θέση του αλλιώς θα εμφανίζει μήνυμα ότι δεν υπάρχει το στοιχείο στον πίνακα.

Η αναζήτηση να πραγματοποιηθεί και με την εντολή for και με την εντολή while.

Οι αριθμοί είναι μοναδικοί στον πίνακα.

```python
list = []

for i in range(10):
  num = int(input("Δώσε στοιχεία: "))
  list.append(num)

key = int(input("Δώσε στοιχείο που αναζητάς: "))

done = True
thesi = 0

for i in list:
  if i == key:
    print(thesi)
    done = False
  thesi += 1

if done == True:
  print("To στοιχείο που αναζητάς δεν είναι στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_exercise_1.py).

### [Άσκηση 2](source/lab_09/lab_09_exercise_2.py)

Έστω ότι δημιουργείτε ένα πρόγραμμα το οποίο κρατά το όνομα επτά παικτών.

Να δημιουργηθεί πίνακας players στον οποίο θα αποθηκεύονται τα ονόματα των 7 παικτών. Θα ταξινομεί τα ονόματα σε φθίνουσα σειρά και θα εμφανίζει τα ονόματα των παικτών ταξινομημένα.

```python
players = []

for i in range(7):
  name = input("Dose onoma paikti: ")
  players.append(name)

for i in range(1,7):
  for j in range(6, i-1, -1):
    if players [j-1] < players [j]:
      temp = players[j-1]
      players[j-1] = players[j]
      players[j] = temp

print("Παίκτες:", players)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_exercise_2.py).

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)
