[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FEffie375%2FTPTE_PLR&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# 9 Υποπρογράμματα

---

## Περιεχόμενα

---

- 9.1 Παραδείγματα

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

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
