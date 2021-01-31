# 4 Εντολή επιλογής - επανάληψης

---

## Περιεχόμενα

---

- 4.1 Παράδειγμα
- 4.2 Εντολή επανάληψης while
- 4.3 While παράδειγμα
- 4.4 Έλεγχος ορθότητας
- 4.5 Ασκήσεις

## 4.1 If Παράδειγμα

---

<!--
```python
# Διαβάζουμε από το χρήστη έναν αριθμό
number = input("Δώσε έναν αριθμό (int): ").strip()

# Ελέγχουμε αν είναι ακέραιος αριθμός
if number.isdigit():
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  number = int(number)
  # Εάν ο αριθμός είναι 0
  if number == 0:
    print("Ο αριθμός είναι μηδέν.")
  # Αλλίως εάν ο αριθμός είναι άρτιος
  elif(number % 2) == 0:
    print("Ο αριθμός είναι άρτιος.")
  # Αλλίως είναι περιττός
  else:
    print("Ο αριθμός είναι περιττός.")
```
-->

```python
# Διαβάζουμε από το χρήστη έναν αριθμό
number = input("Δώσε έναν αριθμό (int): ")

# Ελέγχουμε αν είναι ακέραιος αριθμός
if number.isdigit():
  # Μετατρέπουμε την αλφαριθμητική τιμή σε ακέραια
  number = int(number)
  # Εάν ο αριθμός είναι 0
  if number == 0:
    print("Ο αριθμός είναι μηδέν.")
  # Αλλιώς εάν ο αριθμός είναι άρτιος
  elif(number % 2) == 0:
    print("Ο αριθμός είναι άρτιος.")
  # Αλλιώς είναι περιττός
  else:
    print("Ο αριθμός είναι περιττός.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_1.py)

## 4.2 Εντολή επανάληψης while

---

**ΠΡΟΣΟΧΗ!** Ένα while πρέπει **ΠΑΝΤΑ** να μεταβάλλει τουλάχιστον μία από τις μεταβλητές που ανήκουν στο *CONDITION*, αλλιώς θα δημιουργηθεί ένας ατέρμων βρόγχος (*infinite loop*).Δηλαδή το πρόγραμμα θα κολλήσει μέσα στον βρόγχο επ’ άπειρων.

## 4.3 While παράδειγμα

---

Να γραφεί ένα πρόγραμμα το οποίο διαβάζει 10 αριθμούς και τυπώνει το άθροισμα τους.

<!--
```python
# Αρχικοποιούμε τις μεταβλητές
i = 0
synolo = 0

# Όσο το i είναι μικρότερο του 10
while i < 10:
  # Ζητάμε από το χρήστη να δώσει έναν αριθμό
  # Μετατρέπουμε τον αριθμό σε ακέραιο
  number = int(input("Δώσε αριθμό (int): ").strip())
  # Προσθέτουμε στην μεταβλητή synolo τον αριθμό
  synolo = synolo + number
  # Αυξάνουμε την μεταβλητή i κατά 1
  i = i + 1

# Εκτυπώνουμε το αποτέλεσμα
print(f"Το σύνολο είναι: {synolo}")
```
-->

```python
# Αρχικοποιούμε τις μεταβλητές
i = 0
synolo = 0

# Όσο το i είναι μικρότερο του 10
while i < 10:
  # Ζητάμε από το χρήστη να δώσει έναν αριθμό
  # Μετατρέπουμε τον αριθμό σε ακέραιο
  number = int(input("Δώσε αριθμό (int): "))
  # Προσθέτουμε στην μεταβλητή synolo τον αριθμό
  synolo = synolo + number
  # Αυξάνουμε την μεταβλητή i κατά 1
  i = i + 1

# Εκτυπώνουμε το αποτέλεσμα
print("Το σύνολο είναι: %d" % synolo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_2.py)

## 4.4 Έλεγχος ορθότητας

---

Να γραφεί ένα πρόγραμμα το οποίο διαβάζει 10 αριθμούς και τυπώνει το άθροισμα τους. Εάν ο χρήστης δεν εισάγει αριθμό, να επαναλαμβάνεται η ερώτηση.

<!--
```python
# Αρχικοποιούμε τις μεταβλητές
i = 0
synolo = 0

# Όσο το i είναι μικρότερο του 10
while i < 10:
  # Ζητάμε από το χρήστη να δώσει έναν αριθμό
  number = input("Δώσε αριθμό (int): ").strip()
  # Κάνουμε έλεγχο ορθότητας
  while not number.isdigit():
    # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
    number = input("Είπα δώσε ακέραιο αριθμό: ").strip()
  # Μετατρέπουμε τον αριθμό σε ακέραιο
  number = int(number)
  # Προσθέτουμε στην μεταβλητή synolo τον αριθμό
  synolo = synolo + number
  # Αυξάνουμε την μεταβλητή i κατά 1
  i = i + 1

# Εκτυπώνουμε το αποτέλεσμα
print(f"Το σύνολο είναι: {synolo}")
```
-->

```python
# Αρχικοποιούμε τις μεταβλητές
i = 0
synolo = 0

# Όσο το i είναι μικρότερο του 10
while i < 10:
  # Ζητάμε από το χρήστη να δώσει έναν αριθμό
  number = input("Δώσε αριθμό (int): ")
  # Κάνουμε έλεγχο ορθότητας
  while not number.isdigit():
    # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
    number = input("Είπα δώσε ακέραιο αριθμό: ")
  # Μετατρέπουμε τον αριθμό σε ακέραιο
  number = int(number)
  # Προσθέτουμε στην μεταβλητή synolo τον αριθμό
  synolo = synolo + number
  # Αυξάνουμε την μεταβλητή i κατά 1
  i = i + 1

# Εκτυπώνουμε το αποτέλεσμα
print("Το σύνολο είναι: %d" % synolo)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_example_3.py)

## 4.5 Ασκήσεις

---

Συνιστάται να τρέξετε όλα τα προγράμματα των ασκήσεων. Όταν κάνετε επικόλληση σε κάποιον editor προσέξτε ότι συχνά τα προγράμματα από ορισμένα αρχεία δεν μεταφέρονται πάντα σωστά.

### Άσκηση 1

Να γραφεί πρόγραμμα το οποίο:

1. Θα διαβάζει το αποτέλεσμα 2 ζαριών.
2. Θα ελέγχει αν ο χρήστης εισήγαγε σωστά νούμερα (1-6), αλλιώς θα εμφανίζει μήνυμα λάθους και θα τερματίζει.
3. Αν τα ζάρια ήταν τεσσάρια, θα τυπώνει «Ντορτια».
4. Αν τα ζάρια ήταν 1 και 2, θα τυπώνει «Ασσόδυο».
5. Αν τα ζάρια ήταν διπλά, θα τυπώνει «Διπλές» και το αποτέλεσμα.
6. Αλλιώς θα τυπώνει το αποτέλεσμα της ζαριάς.

<!--
```python
# Διαβάζουμε από το χρήστη να μας δώσει την 1η ζαριά
dice1 = input("Δώσε 1η ζαριά: ").strip()

# Διαβάζουμε από το χρήστη να μας δώσει την 2η ζαριά
dice2 = input("Δώσε 2η ζαριά: ").strip()

# Ελέγχουμε αν αυτό που έγραψε o χρήστης είναι νούμερα
if dice1.isdigit() and dice2.isdigit():
  # Μετατρέπουμε τις ζαρίες σε αριθμό
  dice1 = int(dice1)
  dice2 = int(dice2)
  # Ελέγχουμε αν τα νούμερα των ζαριών είναι μεταξύ 1 - 6
  if (dice1 >= 1 and dice1 <= 6) and (dice2 >= 1 and dice2 <= 6):
    # Εάν οι ζαρίες είναι 4 και 2
    if ((dice1 == 4) and (dice2 == 4)):
      print("Ντόρτια.")
    # Αλλιώς εάν οι ζαριές είναι 1 και 2 ή 2 και 1
    elif (dice1 == 1 and dice2 == 2) or (dice1 == 2 and dice2 == 1):
      print("Ασσόδυο.")
    # Αλλιώς εάν οι ζαριές είναι ίδιες
    elif dice1 == dice2:
      print("Διπλές.")
    # Αλλιώς σε οποιαδήποτε άλλη περίπτωση εμφάνισε τις ζαρίες
    else:
      print(f"Πρώτο ζάρι {dice1}.")
      print(f"Δεύτερο ζάρι {dice2}.")
  # Αλλιώς εάν οι ζαριές είναι εκτός ορίων
  else:
    print("Γιατί οι ζαριές είναι εκτός ορίων 1 και 6;")
# Αλλιώς εάν ο χρήστης δεν έδωσε αριθμόυς
else:
  print("Γιατί έγραψες λέξη;")
```
-->

```python
# Διαβάζουμε από το χρήστη να μας δώσει την 1η ζαριά
dice1 = input("Δώσε 1η ζαριά: ")

# Διαβάζουμε από το χρήστη να μας δώσει την 2η ζαριά
dice2 = input("Δώσε 2η ζαριά: ")

# Ελέγχουμε αν αυτό που έγραψε o χρήστης είναι νούμερα
if dice1.isdigit() and dice2.isdigit():
  # Μετατρέπουμε τις ζαριές σε αριθμό
  dice1 = int(dice1)
  dice2 = int(dice2)
  # Ελέγχουμε αν τα νούμερα των ζαριών είναι μεταξύ 1 - 6
  if (dice1 >= 1 and dice1 <= 6) and (dice2 >= 1 and dice2 <= 6):
    # Εάν οι ζαρίες είναι 4 και 2
    if ((dice1 == 4) and (dice2 == 4)):
      print("Ντόρτια.")
    # Αλλιώς εάν οι ζαριές είναι 1 και 2 ή 2 και 1
    elif (dice1 == 1 and dice2 == 2) or (dice1 == 2 and dice2 == 1):
      print("Ασσόδυο.")
    # Αλλιώς εάν οι ζαριές είναι ίδιες
    elif dice1 == dice2:
      print("Διπλές.")
    # Αλλιώς σε οποιαδήποτε άλλη περίπτωση εμφάνισε τις ζαριές
    else:
      print("Πρώτο ζάρι %d." % dice1)
      print("Δεύτερο ζάρι %d." % dice2)
  # Αλλιώς εάν οι ζαριές είναι εκτός ορίων
  else:
    print("Γιατί οι ζαριές είναι εκτός ορίων 1 και 6;")
# Αλλιώς εάν ο χρήστης δεν έδωσε αριθμόυς
else:
  print("Γιατί έγραψες λέξη;")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_1.py)

### Άσκηση 2

Ένας φοιτητής πρέπει να περάσει 6 μαθήματα σε ένα εξάμηνο. Να γραφεί πρόγραμμα που να διαβάζει τους βαθμούς του φοιτητή και να υπολογίζει το μέσο όρο της βαθμολογίας του για το συγκεκριμένο εξάμηνο. Ανάλογα με το μέσο όρο να εμφανίζεται το μήνυμα «Άριστα» (8,5-10), «Λίαν Καλώς» (6,5-8,49) και «Καλώς» (5-6,49).

<!--
```python
# Αρχικοποιούμε τις μεταβλητές
total = 0
i = 0

# Όσο το i είναι μικρότερο του  6
while i < 6:
  # Ζητάμε από το χρήστη να δώσει έναν βαθμό
  vathmos = input("Δώσε βαθμό (int): ").strip()
  while not vathmos.isdigit():
    # Ζητάμε από το χρήστη να δώσει έναν σωστό βαθμό
    vathmos = input("Δώσε έναν ακέραιο βαθμό: ").strip()
  # Μετατρέπουμε τον βαθμό σε πραγματική τιμή
  vathmos = float(vathmos)
  # Προσθέτουμε στην μεταβλητή total τον βαθμό
  total += vathmos
  # Αυξάνουμε την μεταβλητή i κατά 1
  i += 1

# Υπολογίζουμε το μέσο όρο
mo = total / 6

# Εάν ο μέσος όρος είναι μεγαλύτερος του 10
if mo > 10:
  print("Κάτι δεν πάει καλά...")
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 8.5
# και μικρότερος ή ίσος του 10
elif mo >= 8.5:
  print(f"Άριστα με μέσο όρο {mo:.1f}!")
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 6.5
# και μικρότερος του 8.5
elif mo >= 6.5:
  print(f"Λίαν Καλώς με μέσο όρο {mo:.1f}")
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 5
# και μικρότερος του 6.5
elif mo >= 5:
  print(f"Καλώς με μέσο όρο {mo:.1f}")
# Αλλιώς εμφάνισε μήνυμα ότι ο χρήστης κόπηκε
else:
  print("Kόπηκες")
```
-->

```python
# Αρχικοποιούμε τις μεταβλητές
total = 0
i = 0

# Όσο το i είναι μικρότερο του  6
while i < 6:
  # Ζητάμε από το χρήστη να δώσει έναν βαθμό
  vathmos = input("Δώσε βαθμό (int): ")
  while not vathmos.isdigit():
    # Ζητάμε από το χρήστη να δώσει έναν σωστό βαθμό
    vathmos = input("Δώσε έναν ακέραιο βαθμό: ")
  # Μετατρέπουμε τον βαθμό σε πραγματική τιμή
  vathmos = float(vathmos)
  # Προσθέτουμε στην μεταβλητή total τον βαθμό
  total += vathmos
  # Αυξάνουμε την μεταβλητή i κατά 1
  i += 1

# Υπολογίζουμε το μέσο όρο
mo = total / 6

# Εάν ο μέσος όρος είναι μεγαλύτερος του 10
if mo > 10:
  print("Κάτι δεν πάει καλά...")
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 8.5
# και μικρότερος ή ίσος του 10
elif mo >= 8.5:
  print("Άριστα με μέσο όρο %.1f!" % mo)
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 6.5
# και μικρότερος του 8.5
elif mo >= 6.5:
  print("Λίαν Καλώς με μέσο όρο %.1f" % mo)
# Αλλιώς εάν ο μέσος όρος είναι μεγαλύτερος ή ίσος του 5
# και μικρότερος του 6.5
elif mo >= 5:
  print("Καλώς με μέσο όρο %.1f" % mo)
# Αλλιώς εμφάνισε μήνυμα ότι ο χρήστης κόπηκε
else:
  print("Kόπηκες")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_2.py)

### Άσκηση 3

Μία χρονιά έχει 365 μέρες. Όμως, ο χρόνος που χρειάζεται η γη για να περιστραφεί γύρω από τον ήλιο είναι λίγο μεγαλύτερος. Για αυτό, μερικές χρονιές χρειάζεται να προσθέτουμε την 29η Φεβρουαρίου για να διορθωθεί αυτό το σφάλμα. Αυτά τα έτη, που ονομάζονται δίσεκτα
υπολογίζονται ως εξής:

1. Αν ένα έτος διαιρείται με το 4, είναι δίσεκτο.
2. Αν όμως διαιρείται με το 100, δεν είναι. Εκτός αν διαιρείται με το 400.

Για παράδειγμα:

- το έτος 2016 ήταν δίσεκτο, επειδή διαιρείται με το 4.
- το έτος 1900 δεν ήταν δίσεκτο, επειδή διαιρείται με το 100.
- το έτος 2000 ήταν δίσεκτο, καθώς παρόλο που διαιρείται με το 100, διαιρείται και με το 400.

Να γραφεί πρόγραμμα το οποίο θα δέχεται ένα έτος και θα εμφανίζει μήνυμα αναφέροντας αν ήταν δίσεκτο ή όχι.

**1ος τρόπος:**

<!--
```python
# Διαβάζουμε το έτος που εισάγει ο χρήστης
etos = int(input("Δώσε έτος: ").strip())

# Αν διαιρείται με 4 είναι δίσεκτο
if etos % 4 == 0:
  # Εκτός και αν διαιρείται και με 100
  if etos % 100 == 0:
    # Aλλα και σε αυτήν την περίπτωση αν διαιρείται με 400 είναι δίσεκτο
    if etos % 400 == 0:
      disekto = True
    else:
      disekto = False
  else:
    disekto = True
else:
  disekto = False

# Eκτύπωση αποτελέσματος
if disekto:
  print(f"Το {etos} είναι δίσεκτο έτος.")
else:
  print(f"Το {etos} δεν είναι δίσεκτο έτος.")
```
-->

```python
# Διαβάζουμε το έτος που εισάγει ο χρήστης
etos = int(input("Δώσε έτος: "))

# Αν διαιρείται με 4 είναι δίσεκτο
if etos % 4 == 0:
  # Εκτός και αν διαιρείται και με 100
  if etos % 100 == 0:
    # Aλλα και σε αυτήν την περίπτωση αν διαιρείται με 400 είναι δίσεκτο
    if etos % 400 == 0:
      disekto = True
    else:
      disekto = False
  else:
    disekto = True
else:
  disekto = False

# Eκτύπωση αποτελέσματος
if disekto:
  print("Το %d είναι δίσεκτο έτος." % etos)
else:
  print("Το %d δεν είναι δίσεκτο έτος." % etos)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_3a.py)

**2ος τρόπος:**

<!--
```python
# Διαβάζουμε το έτος που εισάγει ο χρήστης
etos = int(input("Δώσε έτος: ").strip())

# Ελέγχουμε εάν το έτος αυτό είναι δίσεκτο
if (etos % 4 == 0) and (etos % 100 != 0) or (etos % 400 == 0):
  print(f"Το {etos} είναι δίσεκτο έτος.")
else:
  print(f"Το {etos} δεν είναι δίσεκτο έτος.")
```
-->

```python
# Διαβάζουμε το έτος που εισάγει ο χρήστης
etos = int(input("Δώσε έτος: "))

# Ελέγχουμε εάν το έτος αυτό είναι δίσεκτο
if (etos % 4 == 0) and (etos % 100 != 0) or (etos % 400 == 0):
  print("Το %d είναι δίσεκτο έτος." % etos)
else:
  print("Το %d δεν είναι δίσεκτο έτος." % etos)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_3b.py)

### Άσκηση 4

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από το χρήστη αριθμούς και θα υπολογίζει το γινόμενό τους. Το πρόγραμμα θα τερματίζει όταν ο χρήστης εισάγει τον αριθμό 0. Να γίνεται έλεγχος ορθότητας.

<!--
```python
# Αρχικοποίηση μεταβλητών
flag = False
ginomeno = 0
number = 1

# Όσο ο αριθμός είναι διάφορος του μηδενός
while number != 0:
  # Ζητάμε από το χρήστη να δώσει έναν αριθμό
  number = input("Δώσε αριθμό (int): ").strip()
  # Κάνουμε έλεγχο ορθότητας
  while not number.isdigit():
    # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
    number = input("Δώσε σωστά ακέραιο αριθμό: ").strip()
  # Μετατρέπουμε τον αριθμό σε ακέραιο
  number = int(number)
  # Μόνο τη πρώτη φορά είναι η συνθήκη true στη περίπτωση που ο αριθμός δεν είναι μηδέν
  if (flag == False) and (number != 0):
    ginomeno = 1
    # Αλλαγή του flag από False σε True
    flag = True
  # Εάν ο αριθμός είναι διάφορος του μηδενός
  if number != 0:
    # Υπολογίζει κάθε φορά το γίνομενο
    ginomeno *= number

# Eκτύπωση αποτελέσματος
print(f"Γινόμενο: {ginomeno}")
```
-->

```python
# Αρχικοποίηση μεταβλητών
flag = False
ginomeno = 0
number = 1

# Όσο ο αριθμός είναι διάφορος του μηδενός
while number != 0:
  # Ζητάμε από το χρήστη να δώσει έναν αριθμό
  number = input("Δώσε αριθμό (int): ")
  # Κάνουμε έλεγχο ορθότητας
  while not number.isdigit():
    # Ζητάμε από το χρήστη να δώσει σωστά τον αριθμό
    number = input("Δώσε σωστά ακέραιο αριθμό: ")
  # Μετατρέπουμε τον αριθμό σε ακέραιο
  number = int(number)
  # Μόνο τη πρώτη φορά είναι η συνθήκη true στη περίπτωση που ο αριθμός δεν είναι μηδέν
  if (flag == False) and (number != 0):
    ginomeno = 1
    # Αλλαγή του flag από False σε True
    flag = True
  # Εάν ο αριθμός είναι διάφορος του μηδενός
  if number != 0:
    # Υπολογίζει κάθε φορά το γίνομενο
    ginomeno *= number

# Eκτύπωση αποτελέσματος
print("Γινόμενο: %d" % ginomeno)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_4.py)

### Άσκηση 5

Να γραφεί ένα πρόγραμμα το οποίο θα δέχεται από το χρήστη έναν αριθμό και θα τυπώνει το άθροισμα των ψηφίων του.

<!--
```python
# Αρχικοποίηση μεταβλητών
athroisma = 0

# Διαβάζουμε από τον χρήστη έναν αριθμό και τον μετατρέπουμε σε ακέραιο
number = int(input("Δώσε έναν αριθμό: ").strip())

while number:
  # Παίρνουμε το τελευταίο ψηφίο του αριθμού
  telPshfio = number % 10
  # Παίρνουμε τον αριθμό που απομένει (εκτός του τελευταίου ψηφίου)
  number //= 10
  # Προσθέτουμε κάθε φορά στο athroisma το τελευταίο ψηφίο του αριθμού
  athroisma += telPshfio

# Eκτύπωση αποτελέσματος
print(f"Το άθροισμα των ψηφίων είναι {athroisma}.")
```
-->

```python
# Αρχικοποίηση μεταβλητών
athroisma = 0

# Διαβάζουμε από το χρήστη έναν αριθμό και το μετατρέπουμε σε ακέραιο
number = int(input("Δώσε έναν αριθμό: "))

while number:
  # Παίρνουμε το τελευταίο ψηφίο του αριθμού
  telPshfio = number % 10
  # Παίρνουμε τον αριθμό που απομένει (εκτός του τελευταίου ψηφίου)
  number //= 10
  # Προσθέτουμε κάθε φορά στο athroisma το τελευταίο ψηφίο του αριθμού
  athroisma += telPshfio

# Eκτύπωση αποτελέσματος
print("Το άθροισμα των ψηφίων είναι %d." % athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_5.py)

### Άσκηση 6

Το παρακάτω πρόγραμμα χρησιμοποιεί την δομή της επανάληψης while. Εφόσον ο αριθμός που βάλει ο χρήστης είναι διάφορος του μηδέν, τυπώνει τον διπλάσιο του και ζητάει άλλον αριθμό. Η επανάληψη σταματάει όταν ο χρήστης βάλει την τιμή 0.

<!--
```python
# Διαβάζουμε από το χρήστη έναν αριθμό
num = int(input("Γράψε έναν ακέραιο αριθμό: ").strip())

# Όσο ο αριθμός είναι διάφορος του 0
while(num != 0):
  # Εκτύπωσε το διπλάσιο του
  print(2 * num)
  # Ξαναζήτα απο το χρήστη για αριθμό
  num = int(input("Γράψε έναν ακέραιο αριθμό: ").strip())

print("Τέλος")
```
-->

```python
# Διαβάζουμε από το χρήστη έναν αριθμό
num = int(input("Γράψε έναν ακέραιο αριθμό: "))

# Όσο ο αριθμός είναι διάφορος του 0
while(num != 0):
  # Εκτύπωσε το διπλάσιο του
  print(2 * num)
  # Ξαναζήτα απο το χρήστη για αριθμό
  num = int(input("Γράψε έναν ακέραιο αριθμό: "))

print("Τέλος")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_04/lab_04_exercise_6.py)

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)