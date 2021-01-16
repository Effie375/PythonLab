# 12 Συναρτήσεις II

---

## Περιεχόμενα

- 12.1 Ασκήσεις

## 12.1 Ασκήσεις

---

### [Άσκηση 1](source/lab_12/lab_12_exercise_1.py)

Να γραφεί πρόγραμμα το οποίο:

- Θα έχει μια συνάρτηση η οποία θα παίρνει έναν αριθμό και θα
επιστρέφει το τετράγωνό του.
- Η συνάρτηση θα χρησιμοποιείτε σε ένα for loop για να υπολογίσει το άθροισμα των τετράγωνων όλων των αριθμών μέχρι και αυτόν που δώσατε.

```python
def square(n):
  n = n*n

 return n


athroisma = 0
number = int(input("Δώσε αριθμό: "))

for i in range (number + 1):
  athroisma += square(i)
print("Το άθροισμα των αριθμών είναι:", athroisma)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_12/lab_12_exercise_1.py).

### [Άσκηση 2](source/lab_12/lab_12_exercise_2.py)

Να γραφεί πρόγραμμα το οποίο:

- Με τη χρήση συνάρτησης θα διαβάζει και αποθηκεύει τα ονόματα δέκα
μαθητριών (ένα όνομα μπορεί να επαναλαμβάνεται πολλές φορές).
- Στη συνέχεια με μία νέα συνάρτηση θα δέχεται τη λίστα των ονομάτων και θα επιστρέφει μία νέα λίστα η οποία θα περιέχει μοναδικά στοιχεία (το κάθε όνομα μία μόνο φορά).
- Στο κυρίως πρόγραμμα θα εμφανίζεται η λίστα με τα μοναδικά στοιχεία και στη συνέχεια ο χρήστης θα διαβάζει ένα τυχαίο όνομα.
- Με τη χρήση νέας συνάρτησης θα αναζητά αν το τυχαίο όνομα που δόθηκε περιλαμβάνεται μέσα στη λίστα. Στην περίπτωση που δεν υπάρχει θα εκτυπώνει μήνυμα «Το όνομα που αναζητάς δεν είναι στη λίστα», σε οποιαδήποτε άλλη περίπτωση το μήνυμα θα είναι «Το όνομα ??? είναι στη λίστα».

```python
def eisagogiStoixeion():
  onomata = []
  for i in range (10):
    name = input("Δώσε όνομα: ")
    onomata.append(name)

  return onomata


def monadikiLista(lista):
  neaLista = []
  for i in lista:
    if i not in neaLista:
      neaLista.append(i)

  return neaLista


def anazitisi(key, lista):
  done = True
  for i in lista:
    if i == key:
      done = False

  return done

onomata = eisagogiStoixeion()

print(monadikiLista(onomata))

stoixeio = input("Δώσε όνομα που αναζητάς: ")

done = anazitisi(stoixeio, onomata)

if done == True:
  print("Το όνομα που αναζητάς δεν είναι στη λίστα.")
else:
  print("Το όνομα", stoixeio, "είναι στη λίστα.")
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lab_12/lab_12_exercise_2.py).

[Home](../README.md) | [Lab 1](lab_01.md) | [Lab 2](lab_02.md) | [Lab 3](lab_03.md) | [Lab 4](lab_04.md) | [Lab 5](lab_05.md) | [Lab 6](lab_06.md) | [Lab 7](lab_07.md) | [Lab 8](lab_08.md) | [Lab 9](lab_09.md) | [Lab 10](lab_10.md)| [Lab 11](lab_11.md)| [Lab 12](lab_12.md)
