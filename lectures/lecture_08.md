[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FEffie375%2FTPTE_PLR&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# 8 Δομές Δεδομένων - Πολυδιάστατες Λίστες

---

## Περιεχόμενα

---

- 8.1 Πολυδιάστατες Λίστες
- 8.2 Αποθήκευση στοιχείων
- 8.3 Άθροισμα στοιχείων
- 8.4 Έυρεση MAX
- 8.5 Έυρεση MAX με θέση
- 8.6 Άθροισμα στοιχείων κατά γραμμή
- 8.7 Άθροισμα στοιχείων κατά στήλη
- 8.8 Έυρεση μέγιστου κατά γραμμή
- 8.9 Έυρεση μέγιστου κατά στήλη
- 8.10 Αναζήτηση στοιχείων I
- 8.11 Αναζήτηση στοιχείων II
- 8.12 Ταξινόμηση στοιχείων ανά γραμμή
- 8.13 Ταξινόμηση στοιχείων ανά στήλη
- 8.14 Τετραγωνικός πίνακας
- 8.15 Παραδείγματα

## 8.1 Πολυδιάστατες Λίστες

---

## 8.2 Αποθήκευση στοιχείων

---

```python
# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 5
lista = []

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Δημιουργία κενής λίστας
  ypolista = []
  # Για MAX_ELEMENTS - 1
  for j in range(MAX_ELEMENTS - 1):
    # Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
    newNum = int(input("Δώσε αριθμό: "))
    # Αποθηκεύουμε τον αριθμό στην υπολίστα
    ypolista.append(newNum)
  # Αποθηκεύουμε την υπολίστα στη λίστα
  lista.append(ypolista)

# Εκτύπωση της λίστας
print(lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_1.py).

## 8.3 Άθροισμα στοιχείων

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Αρχικοποίηση μεταβλητής
athroisma = 0

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
  # Για κάθε στοιχείο της υπολίστας
  for i in ypolista:
    # Αυξάνουμε το άθροισμα κατά i
    athroisma += i

# Εκτύπωση του αθροίσματος
print(athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_2.py).

## 8.4 Έυρεση MAX

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Έστω ότι το μέγιστο βρίσκεται στην υπολίστα με τη θέση μηδέν και είναι το στοιχείο που βρίσκεται στη θέση 0
megisto = lista[0][0]

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
  # Για κάθε στοιχείο της υπολίστας
  for item in ypolista:
    # Εάν το στιγμιαίο στοιχείο της υπολίστας είναι μεγαλύτερο από το μέγιστο
    if item > megisto:
      # Εκχωρούμε στο μέγιστο το στιγμιαίο στοιχείο
      megisto = item

# Εκτύπωση μεγίστου
print(megisto)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_3.py).

## 8.5 Έυρεση MAX με θέση

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Αρχικοποίηση μεταβλητών
megistoX = 0
megistoY = 0

# Για όσο είναι το μήκος της λίστας
for x in range(len(lista)):
  # Για όσο είναι το μήκος της υπολίστας
  for y in range(len(lista[x])):
    if lista[x][y] > lista[megistoX][megistoY]:
      megistoX = x
      megistoY = y

# Εκτύπωση το megistoX
print(megistoX)
# Εκτύπωση το megistoY
print(megistoY)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_4.py).

## 8.6 Άθροισμα στοιχείων κατά γραμμή

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
  # Αρχικοποίηση μεταβλητής
  sumGrammhs = 0
  # Για κάθε στοιχείο της υπολίστας
  for item in ypolista:
    # Αυξάνουμε το sumGrammhs κατά το item
    sumGrammhs += item

    # Εκτύπωση το άθροισμα γραμμής
    print("Άθροισμα γραμμής: %d" % sumGrammhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_5.py).

## 8.7 Άθροισμα στοιχείων κατά στήλη

---

```python
# Αρχικοποίηση μεταβλητών
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]
MAX_ELEMENTS = 4

# Για MAX_ELEMENTS
for j in range(MAX_ELEMENTS):
  # Αρχικοποίηση μεταβλητής
  sumSthlhs = 0
  # Για MAX_ELEMENTS + 1
  for i in range(MAX_ELEMENTS + 1):
    sumSthlhs += lista[i][j]
  
  # Εκτύπωση το άθροισμα στήλης
  print("Άθροισμα στήλης: %d" % sumSthlhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_6.py).

## 8.8 Έυρεση μέγιστου κατά γραμμή

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
  # Έστω ότι το μέγιστο γραμμής είναι το στοιχείο της υπολίστας που βρίσκεται στη θέση 0
  megistoGrammhs = ypolista[0]
  # Για κάθε στοιχείο της υπολίστας
  for i in ypolista:
    # Εάν το μέγιστο γραμμής είναι μικρότερο από το στιγμιαίο στοιχείο της υπολίστας
    if megistoGrammhs < i:
      # Εκχωρούμε στο megistoGrammhs το i
      megistoGrammhs = i
  
  # Εκτύπωση το μέγιστο γραμμής
  print("Μέγιστο γραμμής: %d" % megistoGrammhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_7.py).

## 8.9 Έυρεση μέγιστου κατά στήλη

---

```python
# Αρχικοποίηση μεταβλητών
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]
MAX_ELEMENTS = 4

# Για MAX_ELEMENTS
for j in range(MAX_ELEMENTS):
  megistoSthlhs = lista[0][j]
  # Για MAX_ELEMENTS + 1
  for i in range(MAX_ELEMENTS + 1):
    if megistoSthlhs < lista[i][j]:
      megistoSthlhs = lista[i][j]

  # Εκτύπωση το μέγιστο στήλης
  print("Μέγιστο στήλης: %d" % megistoSthlhs)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_8.py).

## 8.10 Αναζήτηση στοιχείων I

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 5
keyCounter = 0

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Για MAX_ELEMENTS - 1
  for j in range(MAX_ELEMENTS - 1):
    if key == lista[i][j]:
      # Εκτύπωση σε ποιο σημείο βρίσκεται το στοιχείο που αναζητά ο χρήστης
      print("Βρίσκεται στην %d υπολίστα στην %d θέση" % (i, j))
      # Αυξάνουμε τον keyCounter κατά 1
      keyCounter += 1

# Εκτύπωση το πόσες φορές βρέθηκε το στοιχείο που αναζητά ο χρήστης
print("Βρέθηκε %d φορές." % keyCounter)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_9.py).

## 8.11 Αναζήτηση στοιχείων II

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 3, 3, 9],
         [6, 5, 5, 8],
         [1, 9, 4, 1],
         [0, 4, 7, 4]]

# Ζητάμε από το χρήστη να δώσει στοιχείο που αναζητά και το μετατρέπουμε σε ακέραιο
key = int(input("Δώσε στοιχείο που αναζητάς: "))

# Αρχικοποίηση μεταβλητών
found = False
i = 0
j = 0

# Για όσο το i είναι μικρότερο του 5 και ταυτόχρονα το found δεν ειναι False
while i < 5 and not found:
  # Για όσο το i είναι μικρότερο του 4 και ταυτόχρονα το found δεν ειναι False
  while j < 4 and not found:
    if key == lista[i][j]:
      # Εκτύπωση σε ποιο σημείο βρίσκεται το στοιχείο που αναζητά ο χρήστης
      print("Βρίσκεται στην %d υπολίστα στην %d θέση" % (i, j))
      # Το found γίνεται True
      found = True
    # Αυξάνουμε το j κατά 1
    j += 1
  # Μηδενίζουμε το j
  j = 0
  # Αυξάνουμε το i κατά 1
  i += 1
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_10.py).

## 8.12 Ταξινόμηση στοιχείων ανά γραμμή

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 8, 9, 2],
         [6, 5, 1, 8],
         [1, 2, 4, 3],
         [0, 4, 7, 5]]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print("Η λίστα πριν την ταξινόμηση είναι: %s" % lista)

for k in range(5):
  for i in range(1, 4):
    for j in range(3, i - 1, -1):
      if lista[k][j - 1] > lista[k][j]:
        # Swap lista
        temp = lista[k][j - 1]
        lista[k][j - 1] = lista[k][j]
        lista[k][j] = temp

# Εκτύπωση της λίστας μετά την ταξινόμηση
print("Η λίστα μετά την ταξινόμηση: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_11.py).

## 8.13 Ταξινόμηση στοιχείων ανά στήλη

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 8, 9, 2],
         [6, 5, 1, 8],
         [1, 2, 4, 3],
         [0, 4, 7, 5]]

# Εκτύπωση της λίστας πριν την ταξινόμηση
print("Η λίστα πριν την ταξινόμηση είναι: %s" % lista)

for k in range(4):
  for i in range(1, 5):
    for j in range(4, i - 1, -1):
      if lista[j - 1][k] > lista[j][k]:
        # Swap lista
        temp = lista[j - 1][k]
        lista[j - 1][k] = lista[j][k]
        lista[j][k] = temp

# Εκτύπωση της λίστας μετά την ταξινόμηση
print("Η λίστα μετά την ταξινόμηση: %s" % lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_12.py).

## 8.14 Τετραγωνικός πίνακας

---

```python
# Δημιουργία λίστας
lista = [[2, 3, 4, 1],
         [7, 8, 9, 2],
         [6, 5, 1, 8],
         [1, 2, 4, 3],
         [0, 4, 7, 5]]

# Αρχικοποίηση μεταβλητών
MAX_ELEMENTS = 4
sum1 = 0
sum2 = 0

# Για MAX_ELEMENTS
for i in range(MAX_ELEMENTS):
  # Για MAX_ELEMENTS
  for j in range(MAX_ELEMENTS):
    # Εάν το στιγμιαίο i είναι ίσο με το στιγμιαίο j
    if i == j:
      sum1 += lista[i][j]
      # Εάν το άθροισμα το i και j είναι ίσο με 3
    if i + j == 3:
      sum2 += lista[i][j]

# Εκτύπωση του sum1 και sum2
print(sum1, sum2)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_13.py).

## 8.15 Παραδείγματα

---

### Παράδειγμα 1

```python
# Δημιουργία κενής λίστας
lista = []

# Για κάθε υπολίστα της λίστας
for ypolista in lista:
  # Αρχικοποίηση μεταβλητής
  sum = 0
  # Για κάθε στοιχείο της υπολίστας
  for i in ypolista:
    # Αυξάνουμε το sum κατά i
    sum += i

# Αποθηκεύουμε το sum στη λίστα
lista.append(sum)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_14.py).

### Παράδειγμα 2

```python
# Δημιουργία λιστών
lista1 = [[1, 2, 3],
          [1, 1, 1],
          [2, 3, 4]]
lista2 = [1, 2, 5]
# Δημιούργια κενής λίστας
lista3 = []

# Για κάθε στοιχείο της lista2
for key in lista2:
  # Αρχικοποίηση μεταβλητής
  counter = 0
  # Για κάθε υπολίστας της lista1
  for ypolista in lista1:
    # Για κάθε στοιχείο της υπολίστας
    for i in ypolista:
      # Εάν το στιγμιαίο στοιχείο της υπολίστας είναι ίσο με το key
      if i == key:
        # Αυξάνουμε τον counter κατά 1
        counter += 1
  # Αποθηκεύουμε τον counter στη lista3
  lista3.append(counter)

# Eκτυπώση της lista3
print(lista3)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_08/lecture_08_example_15.py).

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
