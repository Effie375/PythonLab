# Αρχικοποίηση μεταβλητών
vowels = 'aehiouy'
consonants = 'bcdfgjklmnpqrstvwxz'
v_counter = 0
c_counter = 0
i = 0

# Εισαγωγή δεδομένων
lexi = input("Δώσε λέξη: ")

while i < len(lexi):
    if lexi[i] in vowels:
        v_counter += 1
    elif lexi[i] in consonants:
        c_counter += 1
        i += 1
    else:
        pass

# Εκτύπωση αποτελεσμάτων
print("Φωνήεντα: ", v_counter)
print("Σύμφωνα: ", c_counter)
