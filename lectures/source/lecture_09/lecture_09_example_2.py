# Δημιουργία συνάρτησης sayHello
def sayHello(onoma="Human"):
    # Εκτύπωση Hello και όνομα
    print("Hello %s" % onoma)


# Δημιουργία συνάρτησης modDiv
def modDiv(x, y):
    # Υπολόγίζουμε το ακέραιο υπόλοιπο της διαίρεσης
    mod = x % y
    # Υπολογίζουμε το ακέραιο πηλίκο της διαίρεσης
    div = x // y
    # Επιστρέφει το mod και το div
    return mod, div


# -------main--------
# Καλούμε τις συναρτήσεις
sayHello()
sayHello("Chris")
a, b = modDiv(10, 3)
