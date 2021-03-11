[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FEffie375%2FTPTE_PLR&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# 8.1 Λυμένα Παραδείγματα

---

Εδώ θα βρείτε ένα σύνολο με έτοιμα παραδείγματα που βασίζονται στην ύλη του κεφαλαίου και αναδεικνύουν τις ιδιαιτερότητες του. Ο κώδικας όλων των παραδειγμάτων βρίσκεται ακριβώς κάτω από κάθε εκφωνήση.

## 8.1.1 Παράδειγμα 1

---

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

## 8.1.2 Παράδειγμα 2

---

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
