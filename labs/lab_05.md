# 5 Λίστες (μέρος Ι)

---

## Περιεχόμενα

---

- 5.1 Εντολές για λίστες
- 5.2 Παράδειγμα
- 5.3 Ασκήσεις

## 5.1 Εντολές για λίστες

---

- Δημιουργία λίστας
  - `new_list = []`
  - `new_list = [1, 2, "skylos"]`
- Προσπέλαση
  - `a = my_list[n]`
  - `my_list[n] = var1`
- Πρόσθεση στοιχείων
  - `my_list.append(a)`. *Εισάγει την τιμή της μεταβλητής a στο τέλος.*
  - `my_list.extend(new_list)`. *Εισάγει ένα-ένα τα στοιχεία της λίστας new_list στο τέλος.*
    - `my_list.insert(n, var1)`. *Εισάγει την τιμή της μεταβλητής var1 στη θέση n.*
- Αφαίρεση στοιχείων
  - `my_list.remove(x)`. *Αφαιρεί το πρώτο στοιχείο με τιμή x της λίστας.*
- Έλεγχος για στοιχεία
  - `a in my_list`. *Επιστρέφει True αν το στοιχείο a υπάρχει στην λίστα.*
  - `my_list.index(a)`. *Επιστρέφει τη θέση της πρώτης εμφάνισης του a στη λίστα.*
  - `my_list.count(a)`. *Επιστρέφει το πλήθος των στοιχείων με τιμή a στη λίστα.*
- Λοιπές
  - `len(my_list)`. *Επιστρέφει το πλήθος των στοιχείωντης λίστας.*
  - `max(my_list)`. *Επιστρέφει το μέγιστο στοιχείο της λίστας.*
  - `min(my_list)`. *Επιστρέφει το ελάχιστο στοιχείο της λίστας.*

## [5.2 Παράδειγμα](source/lab_05/lab_05_example_1.py)

---

Να γραφεί ένα πρόγραμμα που διαβάζει 10 νούμερα και τυπώνει την λίστα με ανάποδη σειρά.

```python
list = []
i = 0

while i < 10:
  number = int(input("Δώσε νούμερο: "))
  list.append(number)
  i += 1

print(list)

new_list = []

j = 9

while j >= 0:
  new_list.append(list[j])
  j -= 1

print(new_list)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_05/lab_05_example_1.py)

[![Video 1](../images/Video_1.PNG)](https://www.youtube.com/watch?v=CpFO-bNoKh0&list=PLlRCU8UBnRzRipr_LhWiF3YCoEkHUleLK&index=14)

## 5.3 Ασκήσεις

---

### [Άσκηση 1](source/lab_05/lab_05_exercise_1.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει 10 ακεραίους αριθμούς και θα τους αποθηκεύει σε μία λίστα. Έπειτα θα υπολογίζει και θα εμφανίζει:

- Το άθροισμα των στοιχείων της λίστας.
- Το πλήθος των άρτιων στοιχείων της λίστας.
- Το πλήθος των περιττών στοιχείων της λίστας.
- Τη διαφορά του μέγιστου από το ελάχιστο στοιχείο της λίστας.

```python
lista = []
i = 0

# Δίαβασμα πίνακα
while i < 10:
  number = int(input("Δώσε αριθμό: "))
  lista.append(number)
  i= i + 1

# Αρχικοποίηση μεταβλητών
j = 0
k = 0
l = 0
athroisma = 0
artios = 0
perittos = 0
megistos = lista[0]
elaxistos = lista[0]

# Yπολογισμός ζητούμενων
while j < 10:
  athroisma=athroisma+lista[j]
  j = j + 1

print("Το άθροισμα είναι: ", athroisma)

while k < 10:
  if lista[k] % 2 == 0:
    artios += 1
  else:
    perittos += 1
  k += 1

print("To πλήθος των άρτιων είναι: ", artios, " Tο πλήθος των περιττών είναι: ", perittos)

while l < 10:
  if megistos < lista[l]:
    megistos = lista[l]
  if elaxistos > lista[l]:
    elaxistos = lista[l]
  l += 1
    
print("Η διαφορά είναι: ", megistos-elaxistos)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_05/lab_05_exercise_1.py)

### [Άσκηση 2](source/lab_05/lab_05_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο θα διαβάζει μία λέξη και έναν αριθμό χ. Θα τοποθετεί την λέξη στη θέση χ της λίστας, αν η θέση είναι εσφαλμένη να εμφανίζει κατάλληλο μήνυμα. Θα τερματίζει άμα δωθεί ως χ αρνητικός αριθμός. Στο τέλος θα τυπώνει την λίστα.
Να μην γίνει χρήση της μεθόδου count().

```python
cont=True
l = []

while cont:
  leksi = (input("Δώσε λέξη: "))
  thesi = int(input("Δώσε θέση: "))
  if thesi >= 0 and thesi <= len(l):
    l.insert(thesi, leksi)
  else:
    cont = False
    print("Τέλος εισαγωγής δεδομένων.")

print(l)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_05/lab_05_exercise_2.py)

### [Άσκηση 3](source/lab_05/lab_05_exercise_3.py)

Να γραφεί ένα πρόγραμμα το οποίο θα διαβάζει μία λέξη και θα επιστρέφει πόσα φωνήεντα (a,e,h,y,u,i,o) και πόσα σύμφωνα είχε (b,c,d,f,g,j,k,l,m,n,p,q,r,s,t,v,w,x,z).

```python
lexi = input("Δώσε λέξη: ")

vowels = 'aehiouy'
consonants = 'bcdfgjklmnpqrstvwxz'

v_counter=0
c_counter=0
i=0

while i < len(lexi):
  if lexi[i] in vowels:
    v_counter+=1
  # Μπορεί να έχει και άλλους χαρακτήρες όπως " h /, αυτά δε θέλουμε να τα μετρήσουμε.
  elif lexi[i] in consonants:
    c_counter+=1
    i += 1

print("Φωνήεντα: ",v_counter)
print("Σύμφωνα: ",c_counter)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_05/lab_05_exercise_3.py)

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)
