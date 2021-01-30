# Δημιουργία συνάρτησης apot
def apot(x):
    # Επιστρέφει το ακέραιο υπόλοιπο της διάιρεσης με το 2
    return x % 2


# Δημιουργία συνάρτησης foo
def foo(n):
    # Πολλαπλασιάζουμε την παράμετρο με το 2
    apot1 = n * 2
    n = apot1 * 2
    # Επιστρέφει το n και το apot1
    return n, apot1


# Ζητάμε από το χρήστη να δώσει αριθμό και το μετατρέπουμε σε ακέραιο
a = int(input("Δώσε αριθμό: ").strip())

# Εάν καλώντας τη συνάρτηση apot το αποτέλεσμα που επιστρέφει είναι ίσο με το 0
if apot(a) == 0:
    # Καλούμε τη συνάρτηση foo
    a, n = foo(a)
    # Εκτύπωση του a και n
    print(a, n)
# Αλλιώς σε οποιαδήποτε άλλη περίπτωση
else:
    # Καλούμε τη συνάρτηση apot και εκτύπωνουμε
    print(apot(a))
