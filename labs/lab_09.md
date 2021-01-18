# 9 Πολυδιάστατες λίστες

---

## Περιεχόμενα

---

- 9.1 Εντολές για λίστες
- 9.2 Παράδειγμα
- 9.3 Ασκήσεις

## 9.1 Εντολές για λίστες

---

- Προσπέλαση Πολυδιάστατης Λίστας
  - `a = my_list[x][y][z]...`
  - `my_list[x][y] = var1`
- Πρόσθεση στοιχείων
  - `my_list[x].append(a)`. Εισάγει την τιμή της μεταβλητής a στο τέλοςτης λίστας που βρίσκεται στη θέση «x» της λίστας my_list.

## [9.2 Παράδειγμα](source/lab_09/lab_09_example_1.py)

---

Να γραφεί ένα πρόγραμμα, το οποίο θα διαβάζει 5 λίστες από 10 θετικούς ακεραίους αριθμούς και θα τυπώνει τη λίστα με το μεγαλύτερο άθροισμα.

```python
# Αρχικοποίηση μεταβλητών
lista = []

for i in range(5):
  ypolista = []
  for j in range(10):
    # Εισαγωγή δεδομένων
    n = int(input("Δώσε αριθμό: "))
    ypolista.append(n)
  lista.append(ypolista)

# Αρχικοποίηση μεταβλητών
meg_athroisma = 0

for ypolista in lista:
  athroisma = 0
  for i in ypolista:
    athroisma += i
  if athroisma > meg_athroisma:
    meg_athroisma = athroisma
    meg_lista = ypolista

# Εκτύπωση αποτελέσματος
print(meg_lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_example_1.py).

## 9.3 Ασκήσεις

---

### [Άσκηση 1](source/lab_09/lab_09_exercise_1.py)

Ένας φοιτητής για να φοιτήσει στο Τ.Π.Τ.Ε. πρέπει να ολοκληρώσει 8 εξάμηνα. Κάθε εξάμηνο αποτελείται από 6 μαθήματα.

Να γραφεί πρόγραμμα, το οποίο:

- Για κάθε εξάμηνο φοίτησης, διαβάζει τους βαθμούς ενός φοιτητή και για κάθε εξάμηνο τους τοποθετεί σε νέα λίστα.
- Διαβάζει από το χρήστη τον αριθμό ενός εξαμήνου.
- Υπολογίζει και εμφανίζει πόσα μαθήματα πέρασε και τι μέσο όρο είχε σε αυτό το εξάμηνο.

```python
# Αρχικοποίηση μεταβλητών
eksamina = []

for i in range(8):
  vathmoi = []
  for j in range(6):
    # Εισαγωγή δεδομένων
    vathmos = float(input("Δώσε βαθμό: "))
    vathmoi.append(vathmos)
eksamina.append(vathmoi)

# Εισαγωγή δεδομένων
ar_eksaminou = int(input("Ποιο εξάμηνο θες να δείς;"))

# Aφαιρούμε 1 γιατί ο χρήστης θα δώσει π.χ. 1 για το πρώτο εξάμηνο
# ενώ αυτό είναι στη θέση 0.
eksamino = eksamina[ar_eksaminou-1]

# Αρχικοποίηση μεταβλητών
souma = 0
perasmena = 0

for mathima in eksamino:
  souma += mathima
  if mathima >= 5:
    perasmena += 1

# Εκτύπωση αποτελεσμάτων
print("Ο μέσος όρος είναι: ", souma/len(eksamino))
print("Πέρασες: ", perasmena)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_exercise_1.py).

### [Άσκηση 2](source/lab_09/lab_09_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο:

- θα διαβάζει τον αριθμό κύκλων και επεισοδίων ανά κύκλο μιας τηλεοπτικής σειράς,
- θα διαβάζει την τηλεθέαση κάθε επεισοδίου,
- θα εμφανίζει το επεισοδίο με την μικρότερη και μεγαλύτερη τηλεθέαση,
- θα εμφανίζει τον κύκλο με την μεγαλύτερη μέση τηλεθέαση.

```python
# Εισαγωγή δεδομένων
seasons = int(input("Δώσε κύκλους: "))
episodes = int(input("Δώσε επεισόδια άνα κύκλο: "))

# Αρχικοποίηση μεταβλητών
thle8eash = []

for i in range(seasons):
  thl_season = []
  for j in range(episodes):
    # Εισαγωγή δεδομένων
    thl = float(input("Δώσε τηλεθέαση %dx%d: " % (i+1, j+1)))
    thl_season.append(thl)
  thle8eash.append(thl_season)

# Αρχικοποίηση μεταβλητών
maxThlSeason = 0
maxThlEpi = 0
minThlSeason = 0
minThlEpi = 0
maxMO = 0

for i in range(seasons):
  soumaSeason = 0
  for j in range(episodes):
    if thle8eash[i][j] > thle8eash[maxThlSeason][maxThlEpi]:
      maxThlSeason = i
      maxThlEpi = j
      if thle8eash[i][j] < thle8eash[minThlSeason][maxThlEpi]:
        minThlSeason = i
        minThlEpi = j
  soumaSeason += thle8eash[i][j]

if maxMO < soumaSeason:
  maxMO = soumaSeason
  maxMOSeason = i

# Εκτύπωση αποτελεσμάτων
print("Eπεισόδιο με μέγιστη τηλεθέαση: %dx%d" % (maxThlSeason+1, maxThlEpi+1))
print("Eπεισόδιο με ελάχιστη τηλεθέαση: %dx%d" % (minThlSeason+1, minThlEpi+1))
print("Σεζόν με μεγαλύτερο μέσο όρο τηλεθέασης:", maxMOSeason+1)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_exercise_2.py).

### [Άσκηση 3](source/lab_09/lab_09_exercise_3.py)

Ένας φοιτητής πρέπει να παρακολουθήσει 2 εξάμηνα για ένα σεμινάριο. Σε κάθε εξάμηνο θα πρέπει να εξεταστεί σε δυο μαθήματα. (Οι βαθμοί μπορούν να είναι από 0-10)

Να γραφεί πρόγραμμα, το οποίο:

- Για κάθε εξάμηνο να διαβάζει και να τυπώνει τους βαθμούς των μαθημάτων του φοιτητή.
- Να υπολογίζει και να εμφανίζει το μεγαλύτερο βαθμό που συγκέντρωσε ο φοιτητής από όλα τα μαθήματα.

```python
# Διάβασμα βαθμών
eksamino = []

for i in range(2):
  mathima = []
  for j in range(2):
    # Εισαγωγή δεδομένων
    vathmos = input("Βαθμός εξαμήνου %d και %d μάθημα: " % (i + 1, j + 1))
    vathmos = float(vathmos)
    mathima.append(vathmos)
    eksamino.append(mathima)

# Εμφάνιση βαθμών ανά εξάμηνο
print("Οι βαθμοί του φοιτητή είναι:", eksamino)

# Υπολογισμός μέγιστου με βάση το κάθε μάθημα
meg_vathmos = mathima[0]

for mathima in eksamino:
  for i in mathima:
    if meg_vathmos < i:
      meg_vathmos = i

# Εκτύπωση αποτελέσματος
print("O μέγιστος βαθμός είναι:", meg_vathmos)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_exercise_3.py).

### [Άσκηση 4](source/lab_09/lab_09_exercise_4.py)

Ένας αθλητής πρέπει να αγωνιστεί σε 4 αθλήματα επιτυχώς για να κερδίσει ένα μετάλλιο. Κάθε άθλημα έχει 3 προσπάθειες. (Οι βαθμοί μπορούν να είναι από 0-10)

Να γραφεί πρόγραμμα, το οποίο:

- Να διαβάζει τις προσπάθειες του αθλητή σε κάθε άθλημα.
- Να υπολογίζει και εμφανίζει το άθλημα με τους μεγαλύτερους βαθμούς καθώς και το άθροισμά των βαθμών στο συγκεκριμένο άθλημα.
- Να βρίσκει και να εμφανίζει το μέγιστο βαθμό από όλες τις προσπάθειες και να αναζητά πόσες φορές συγκεντρώθηκε αυτός ο βαθμός στο σύνολο των βαθμών.

```python
# Διάβασμα προσπαθειών
athlimata = []

for i in range(3):
  vathmoi = []
  for j in range(3):
    # Εισαγωγή δεδομένων
    vathmos = input("Βαθμός αθλήματος %d & προσπάθεια %d: " % (i+1, j+1))
    # Μετατροπή από str σε float
    vathmos = float(vathmos)
    vathmoi.append(vathmos)
  athlimata.append(vathmoi)

# Υπολογισμός και εμφάνιση αθλήματος με μεγαλύτερους βαθμούς
maxsum = 0

for vathmoi in athlimata:
  sum = 0
  for i in vathmoi:
    sum += i
    if sum > maxsum:
      maxsum = sum
      maxathlima = vathmoi

# Εκτύπωση αποτελέσματος
print("Ο max βαθμός είναι:", maxathlima, "και το άθροισμα είναι:", maxsum)

# Υπολογισμός μέγιστου βαθμού σε κάθε άθλημα
meg_vathmos = athlimata[0][0]

for vathmoi in athlimata:
  for i in vathmoi:
    if i > meg_vathmos:
      meg_vathmos = i

# Εκτύπωση αποτελέσματος
print("Ο μέγιστος βαθμός του αθλητή είναι:", meg_vathmos)

# Αναζήτηση φορών μέγιστου βαθμού σε κάθε άθλημα
vathmos_counter = 0

for vathmoi in athlimata:
  for i in vathmoi:
    if i == meg_vathmos:
      vathmos_counter += 1

# Εκτύπωση αποτελέσματος
print("O μέγιστος βαθμός βρέθηκε %d φορές." % (vathmos_counter))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_09/lab_09_exercise_4.py).

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)
