# Δημιουργία συνάρτησης eisagogiStoixeion
def eisagogiStoixeion():
    # Δημιουργία κενής λίστας
    onomata = []
    # Για 10 φορές
    for i in range(10):
        # Ζητάμε από το χρήστη να δώσει το όνομά του
        name = input("Δώσε όνομα: ")
        # Αποθηκεύουμε το όνομα στη λίστα onomata
        onomata.append(name)
    # Επιστρέφει τη λίστα onomata
    return onomata


# Δημιουργία συνάρτησης monadikiLista
def monadikiLista(listaP):
    # Δημιουργία κενής λίστας
    neaLista = []
    # Για κάθε στοιχείο της λίστας
    for i in listaP:
        # Eάν το στοιχείο δεν είναι στη neaLista
        if i not in neaLista:
            # Αποθηκεύουμε το στιγμιαίο στοιχείο στη neaLista
            neaLista.append(i)
    # Επιστρέφει τη neaLista
    return neaLista


# Δημιουργία συνάρτησης anazitisi
def anazitisi(key, listaP):
    # Αρχικοποίηση μεταβλητής
    done = True
    # Για κάθε στοιχείο της λίστας
    for i in listaP:
        # Εάν το στιγμιαίο στοιχείο της λίστας είναι ίσο με το key
        if i == key:
            # Το done γίνεται False
            done = False
    # Επιστρέφει το done
    return done


# Καλούμε τη συνάρτηση eisagogiStoixeion
onomata = eisagogiStoixeion()
# Εκτύπωση της μοναδικής λίστας καλώντας τη συνάρτηση
print(monadikiLista(onomata))

# Ζητάμε από το χρήστη να δώσει το όνομα που αναζητά
stoixeio = input("Δώσε όνομα που αναζητάς: ")

# Καλούμε τη συνάρτηση anazitisi
done = anazitisi(stoixeio, onomata)

# Εάν το done είναι ίσο με True
if done == True:
    print("Το όνομα που αναζητάς δεν είναι στη λίστα.")
else:
    print("Το όνομα %s είναι στη λίστα." % stoixeio)
