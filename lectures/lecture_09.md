# 9 Συναρτήσεις I

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


#-------main--------
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

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_example_1.py)

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

Να γραφεί µια συνάρτηση η οποία θα δέχεται µια λίστα Α µε
αριθµούς και θα την ταξινοµεί.

```python
def sort(A):
  for i in range(1, len(A)):
    for j in range(len(A)-1, i-1, -1):
      if A[j-1] > A[j]:
        temp = A[j-1]
        A[j-1] = A[j]
        A[j] = temp
  return A


list = [1, 6, 2, 5, 3, 7, 4]

print(sort(list[:]))
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_09/lecture_09_exercise_3.py)

[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md) | [Lect 10](lecture_10.md)
