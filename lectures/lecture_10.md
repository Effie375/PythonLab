# 10 Συναρτήσεις II

---

## Περιεχόμενα

---

- 10.1 Παραδείγματα

## 10.1 Παραδείγματα

---

### [Παράδειγμα 1](source/lecture_10/lecture_10_example_1.py)

```python
def search_function(lista_s, key):
  counter = 0
  for i in lista_s:
    if i == key:
      counter += 1
  return counter

lista = [[1, 2, 3, 1], [6, 6, 7, 8], [9, 10, 11, 12], [9, 3, 3, 16]]
search_key = [1, 3, 6, 9]
results = []

for key in search_key:
  s = 0
  for ypolista in lista:
    k = search_function(ypolista, key)
    s = s + k
  results.append(s)

print(results)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_10/lecture_10_example_1.py)

### [Παράδειγμα 2](source/lecture_10/lecture_10_example_2.py)

```python
def athroisma(lista_new):
  A = []
  for item in lista_new:
    item.sort(reverse=True)


lista = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for item in lista:
  print(item)

athroisma(lista)

print("...........")

for item in lista:
  print(item)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_10/lecture_10_example_2.py)

### [Παράδειγμα 3](source/lecture_10/lecture_10_example_3.py)

```python
def showlist(lista_2):
  for i in range(len(lista_2)):
    lista_2[i] = lista_2[i] * 2


lista = [1, 4, 3, 5, 6]

showlist(lista[:])

print(lista)
```

Για να κατεβάσετε τον κώδικα πατήστε [εδώ](source/lecture_10/lecture_10_example_3.py)


[Home](../README.md) | [Lect 1](lecture_01.md) | [Lect 2](lecture_02.md) | [Lect 3](lecture_03.md) | [Lect 4](lecture_04.md) | [Lect 5](lecture_05.md) | [Lect 6](lecture_06.md) | [Lect 7](lecture_07.md) | [Lect 8](lecture_08.md) | [Lect 9](lecture_09.md) | [Lect 10](lecture_10.md)
