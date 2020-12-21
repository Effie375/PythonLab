# 3 Εντολές επιλογής

---

## Περιεχόμενα

---

- 3.1 Εντολές
- 3.2 Παράδειγμα if
- 3.3 Ασκήσεις

## 3.1 Εντολές

---

- Συνάρτησεις ελέγχου `var1`
    - var1.isdigit(): Επιστρέφει `True`, αν η `var1` αποτελείται μόνο από νούμερα.
    - var1.isalpha(): Επιστρέφει `True`,αν η `var1` αποτελείται μόνο από γράμματα.
- Μετατροπή str σε αριθμό
    - Ακέραιο(int): `var1 = int(var1)`
    - Πραγματικό(float): `f = float(f)`
- Εντολή Επιλογής
    - `if a==b or (a<5andb>4):`

Σύμβολα: `==`, `<`, `>`, `<=`, `>=`, `!=`, `not`, `and`, `or`.

**ΠΡΟΣΟΧΗ:** Οι εντολές if και else τελείωνουν με τον τερματικό χαρακτήρα `:` αλλιώς θα προκύψει **syntaxerror**.

## 3.2 Παράδειγμα if

---

```python
number = input("Dwse enan ari8mo: ")

if number.isdigit() == True:
    number = int(number)
    if number == 0:
        print("Mhden")
    else:
        print("Allos arithmos")
```

## 3.3 Ασκήσεις

---

### [3.3.1 Άσκηση 1](source/lab_03/lab_03_exercise_1.py)

Ένας φοιτητής για να επιτύχει στο μάθημα «Εισαγωγή στον Προγραμματισμό» πρέπει να δώσει μία πρόοδο και να συμμετάσχει στις γραπτές εξετάσεις στο τέλος του εξαμήνου. Ο υπολογισμός του τελικού βαθμού βασίζεται στον εξής τύπο:

`Τελικός Βαθμός = Πρόοδος * 20% + Γραπτά * 80%`

Να γραφεί πρόγραμμα το οποίο θα διαβάζει το όνομα και τους βαθμούς ενός φοιτητή και στο τέλος να εμφανίζεται το μήνυμα «Πέρασες» αν ο βαθμός του είναι μεγαλύτερος ή ίσος με 5, και «Απέτυχες» στην αντίθετη περίπτωση.

```python
# Diavasma apotelesmatwn
onoma = input("Dwse onoma foithth: ")
proodos = int(input("Vathmos ergasias: "))
grapto = int(input("Vathmos graptou: "))

# Ypologismos telikou vathmou
telikosVathmos = proodos * 0.2 + grapto * 0.8

# Elegxos an einai panw apo 5
if telikosVathmos >= 5:
    print(onoma, "Perases")
else:
    print(onoma, "Apetyxes")
```

### [3.3.2 Άσκηση 2](source/lab_03/lab_03_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο:

1) Θα διαβάζει έναν αριθμό.
2) Θα ελέγχει αν ο χρήστης εισήγαγε νούμερα, αλλιώς θα βγάζει μήνυμα λάθους και θα τερματίζει.
3) Αν ο αριθμός είναι από το 5 έως το 10, θα τυπώνει «Πέρασες το μάθημα!»
4) Αλλιώς θα τυπώνει «Κόπηκες, προσπάθησε ξανά!»

```python
# Diavasma apotelesmatwn
number = input("Dwse arithmo: ")

# Elegxos an einai arithmos
if number.isdigit():
    # Afou kseroume oti einai arithmos:
    number = int(number)
    # Elegxoume oti o arithmos einai metaksi 5-10
    if number >= 5 and number <= 10:
        print("Perases to mathima!")
    else:
        print("Kopikes. Prospathise ksana!")
# Termatizei me minima lathous
else:
    print("Auto den einai arithmos!")
```

### [3.3.3 Άσκηση 3](source/lab_03/lab_03_exercise_3.py)

Ένα σετ αγώνα βόλει τερματίζει, όταν μια από τις δυο ομάδες συγκεντρώσει 25 πόντους.

Να γραφεί πρόγραμμα που :

1) θα διαβάζει τους πόντους των δυο ομάδων.
2) θα ελέγχει αν δόθηκε αριθμός, αλλιώς θα ζητά να διαβάσει ξανά αριθμό.
3) Θα ελέγχει αν η πρώτη ομάδα συγκέντρωσε 25 βαθμούς και θα τυπώνει «Η ομάδα 1 κέρδισε!»
4) Αλλιώς θα εμφανίζει «Η ομάδα 2 κέρδισε!»

```python
# Diavasma apotelesmatwn
team_a = input("Dwse tous pontous tis prwtis omadas: ")
team_b = input ("Dwse tous pontous tis deuteris omadas: ")

# Elegxos an einai arithmos
if not(team_a.isdigit() and team_b.isdigit()):
    # Zita ksana na diavasoume arithmo
    team_a = input("Eipa dwse pontous gia omada 1: ")
    team_b = input ("Eipa dwse pontous gia omada 2: ")

# Afou kseroume oti einai arithmos:
team_a = int(team_a)
team_b = int(team_b)

# Elegxoume oti h omada 1 sygkentrwse 25 vathmous
if team_a == 25:
    print("H omada 1 kerdise!")
else:
    print("H omada 2 kerdise!")
```
