# 9 Συναρτήσεις

---

## Περιεχόμενα

---

- 9.1 Παραδείγματα
- 9.2 Ασκήσεις

## 9.1 Παραδείγματα

---

### [Παράδειγμα 1](source/lecture_09/lecture_09_example_1.py)

```python
def sunolo(x, y):
  athroisma = x + y
  return athroisma


def sayHello():
  print("Hello")
# Δεν επιστρέφει κάτι άρα δε χρειάζεται return


# -------main--------
x = 3
y = 4

athroisma = sunolo(x, y)

sayHello()
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_1.py)

### [Παράδειγμα 2](source/lecture_09/lecture_09_example_2.py)

```python
def sayHello(onoma="Human"):
  print("Hello", onoma)


def modDiv(x, y):
  mod = x % y
  div = x // y
  return mod, div


#-------main--------
sayHello()
sayHello("Chris")
a, b = modDiv(10, 3)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_2.py)

### [Παράδειγμα 3](source/lecture_09/lecture_09_example_3.py)

```python
def searchFunction(listaS, key):
  counter = 0
  for i in listaS:
    if i == key:
      counter += 1
  return counter

lista = [[1, 2, 3, 1], 
  [6, 6, 7, 8], 
  [9, 10, 11, 12], 
  [9, 3, 3, 16]]
searchKey = [1, 3, 6, 9]
results = []

for key in searchKey:
  s = 0
  for ypolista in lista:
    k = searchFunction(ypolista, key)
    s = s + k
  results.append(s)

print(results)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_3.py)

### [Παράδειγμα 4](source/lecture_09/lecture_09_example_4.py)

```python
def athroisma(listaNew):
  A = []
  for item in listaNew:
    item.sort(reverse=True)


lista = [[1, 2, 3, 4], 
  [5, 6, 7, 8], 
  [9, 10, 11, 12], 
  [13, 14, 15, 16]]

for item in lista:
  print(item)

athroisma(lista)

print("...........")

for item in lista:
  print(item)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_4.py)

### [Παράδειγμα 5](source/lecture_09/lecture_09_example_5.py)

```python
def showList(lista2):
  for i in range(len(lista2)):
    lista2[i] = lista2[i] * 2


lista = [1, 4, 3, 5, 6]

showList(lista[:])

print(lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_5.py)

## 9.2 Ασκήσεις

---

### [Άσκηση 1](source/lecture_09/lecture_09_exercise_1.py)

```python
def foo(x):
  return x/5


x = int(input("Δώσε αριθμό για διαίρεση: "))
print(foo(x))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_exercise_1.py)

### [Άσκηση 2](source/lecture_09/lecture_09_exercise_2.py)

Τι θα εµφανιστεί αν δώσουµε ως τιµή εισόδου στο πρόγραµµα την τιµή 5 και τι την τιµή 10.

```python
def apot(x):
  return x % 2


def foo(n):
  apot1 = n * 2
  n = apot1 * 2
  return n, apot1


a = int(input("Δώσε αριθμό: "))

if apot(a) == 0:
  a, n = foo(a)
  print(a, n)
else:
  print(apot(a))
```

Για α = 5 θα εµφανιστεί στην οθόνη η τιµή 1 και για α = 10 θα εµφανιστούν οι τιµές 40, 20.

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_exercise_2.py)

### [Άσκηση 3](source/lecture_09/lecture_09_exercise_3.py)

Να γραφεί µια συνάρτηση η οποία θα δέχεται µια λίστα µε
αριθµούς και θα την ταξινοµεί.

```python
def sort(listaP):
  for i in range(1, len(listaP)):
    for j in range(len(listaP)-1, i-1, -1):
      if listaP[j-1] > listaP[j]:
        temp = listaP[j-1]
        listaP[j-1] = listaP[j]
        listaP[j] = temp
  return listaP


list = [1, 6, 2, 5, 3, 7, 4]

print(sort(list[:]))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_exercise_3.py)

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md)
