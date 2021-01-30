# 9 Συναρτήσεις

---

## Περιεχόμενα

---

- 9.1 Παραδείγματα
- 9.2 Ασκήσεις

## 9.1 Παραδείγματα

---

### Παράδειγμα 1

```python
# Δημιουργία συνάρτησης sunolo
def sunolo(x, y):
  # Υπολογίζουμε το άθροισμα των δύο παραμέτρων
  athroisma = x + y
  # Επιστρέφει το άθροισμα
  return athroisma


# Δημιουργία συνάρτησης sayHello
def sayHello():
  # Εκτύπωση Hello
  print("Hello")
# Δεν επιστρέφει κάτι άρα δε χρειάζεται return


# -------main--------
# Αρχικοποίηση μεταβλητών
x = 3
y = 4

# Καλόυμε τη συνάρτηση sunolo
athroisma = sunolo(x, y)
# Εκτύπωση το άθροισμα
print(athroisma)

# Καλόυμε τη συνάρτηση sayHello
sayHello()
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_1.py)

### Παράδειγμα 2

```python
# Δημιουργία συνάρτησης sayHello
def sayHello(onoma="Human"):
  # Εκτύπωση Hello και όνομα
  print("Hello %s" % onoma)


# Δημιουργία συνάρτησης modDiv
def modDiv(x, y):
  # Υπολόγίζουμε το ακέραιο υπόλοιπο της διαίρεσης
  mod = x % y
  # Υπολογίζουμε το ακέραιο πηλίκο της διαίρεσης
  div = x // y
  # Επιστρέφει το mod και το div
  return mod, div


# -------main--------
# Καλούμε τις συναρτήσεις
sayHello()
sayHello("Chris")
a, b = modDiv(10, 3)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_2.py)

### Παράδειγμα 3

```python
# Δημιουργία συνάρτησης searchFunction
def searchFunction(pLista, key):
  # Αρχικοποίηση συνάρτησης
  counter = 0
  # Για κάθε στοιχείο της λίστας
  for i in pLista:
    # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
    if i == key:
      # Αυξάνουμε τον counter κατά 1
      counter += 1
  # Επιστρέφει τον counter
  return counter


# Δημιουργία λιστών
lista = [[1, 2, 3, 1],
         [6, 6, 7, 8],
         [9, 1, 1, 2],
         [9, 3, 3, 6]]
searchKey = [1, 3, 6, 9]
# Δημιουργία κενής λίστας
results = []

# Για κάθε στοιχείο της λίστας searchKey
for key in searchKey:
  # Αρχικοποίηση μεταβλητής
  s = 0
  # Για κάθε υπολίστα της λίστας
  for ypolista in lista:
    # Καλούμε τη συνάρτηση searchFunction
    k = searchFunction(ypolista, key)
    # Αυξάνουμε το s κατά k
    s += k
  # Αποθηκεύουμε το s στη λίστα results
  results.append(s)

# Εκτύπωση της λίστας results
print(results)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_3.py)

### Παράδειγμα 4

```python
# Δημιουργία συνάρτησης athroisma
def athroisma(listaNew):
  # Για κάθε στοιχείο της λίστας
  for item in listaNew:
    item.sort(reverse=True)


# Δημιουργία λίστας
lista = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 1, 1, 2],
         [3, 4, 5, 6]]

# Για κάθε στοιχείο της λίστας
for item in lista:
  # Εκτύπωση το στιγμιαίο στοιχείο της λίστας
  print(item)

# Καλούμε τη συνάρτηση lista
athroisma(lista)

# Εκτύπωση διαχωριστικό ....
print("...........")

# Για κάθε στοιχείο της λίστας
for item in lista:
  # Εκτύπωση το στιγμιαίο στοιχείο της λίστας
  print(item)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_4.py)

### Παράδειγμα 5

```python
# Δημιουργία συνάρτησης showList
def showList(lista2):
  # Για όσο είναι το μήκος της λίστας
  for i in range(len(lista2)):
    # Πολλαπλασιάζουμε το στιγμιαίο στοιχείο της λίστας κατά 2
    lista2[i] = lista2[i] * 2


# Δημιουργία λίστας
lista = [1, 4, 3, 5, 6]

# Καλούμε τη συνάρτηση showList
showList(lista[:])

# Εκτύπωση λίστας
print(lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_5.py)

## 9.2 Ασκήσεις

---

### Άσκηση 1

<!--
# Δημιουργία συνάρτησης foo
def foo(x):
  # Επιστρέφει τη διάιρεση της παραμέτρου με το 5
  return x / 5


# Ζητάμε από το χρήστη να δώσει αριθμό για διαίρεση με το 5
x = int(input("Δώσε αριθμό για διαίρεση με το 5: ").strip())

# Καλούμε τη συνάρτηση foo και εκτύπωνουμε
print(foo(x))
-->

```python
# Δημιουργία συνάρτησης foo
def foo(x):
  # Επιστρέφει τη διάιρεση της παραμέτρου με το 5
  return x / 5


# Ζητάμε από το χρήστη να δώσει αριθμό για διαίρεση με το 5
x = int(input("Δώσε αριθμό για διαίρεση με το 5: "))

# Καλούμε τη συνάρτηση foo και εκτύπωνουμε
print(foo(x))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_exercise_1.py)

### Άσκηση 2

Τι θα εµφανιστεί αν δώσουµε ως τιµή εισόδου στο πρόγραµµα την τιµή 5 και τι την τιµή 10.

<!--
# Δημιουργία συνάρτησης apot
def apot(x):
  # Επιστρέφει το ακέραιο υπόλοιπο της διάιρεσης με το 2
  return x % 2


# Δημιουργία συνάρτησης foo
def foo(n):
  # Πολλαπλασιάζουμε την παράμετρο με το 2
  apot1 = n * 2
  n = apot1 * 2
  # Επιστρέφει το n και το apot1
  return n, apot1


# Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
a = int(input("Δώσε αριθμό: ").strip())

# Εάν καλώντας τη συνάρτηση apot το αποτέλεσμα που επιστρέφει είναι ίσο με το 0
if apot(a) == 0:
  # Καλούμε τη συνάρτηση foo
  a, n = foo(a)
  # Εκτύπωση του a και n
  print(a, n)
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Καλούμε τη συνάρτηση apot και εκτύπωνουμε
  print(apot(a))
-->

```python
# Δημιουργία συνάρτησης apot
def apot(x):
    # Επιστρέφει το ακέραιο υπόλοιπο της διάιρεσης με το 2
    return x % 2


# Δημιουργία συνάρτησης foo
def foo(n):
  # Πολλαπλασιάζουμε την παράμετρο με το 2
  apot1 = n * 2
  n = apot1 * 2
  # Επιστρέφει το n και το apot1
  return n, apot1


# Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
a = int(input("Δώσε αριθμό: "))

# Εάν καλώντας τη συνάρτηση apot το αποτέλεσμα που επιστρέφει είναι ίσο με το 0
if apot(a) == 0:
  # Καλούμε τη συνάρτηση foo
  a, n = foo(a)
  # Εκτύπωση του a και n
  print(a, n)
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
  # Καλούμε τη συνάρτηση apot και εκτύπωνουμε
  print(apot(a))
```

Για α = 5 θα εµφανιστεί στην οθόνη η τιµή 1 και για α = 10 θα εµφανιστούν οι τιµές 40, 20.

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_exercise_2.py)

### Άσκηση 3

Να γραφεί µια συνάρτηση η οποία θα δέχεται µια λίστα µε αριθµούς και θα την ταξινοµεί.

```python
# Δημιουργία συνάρτησης sort
def sort(listaP):
  for i in range(1, len(listaP)):
    for j in range(len(listaP) - 1, i - 1, -1):
      if listaP[j - 1] > listaP[j]:
        # Swap listaP
        temp = listaP[j - 1]
        listaP[j - 1] = listaP[j]
        listaP[j] = temp
  # Επιστρέφει τη listaP
  return listaP


# Δημιουργία λίστας
lista = [1, 6, 2, 5, 3, 7, 4]

# Καλούμε τη συνάρτηση sort και εκτύπωνουμε
print(sort(lista[:]))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_exercise_3.py)

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
