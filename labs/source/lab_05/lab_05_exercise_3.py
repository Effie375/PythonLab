# Αρχικοποίηση μεταβλητών
vowels = 'aehiouy'
consonants = 'bcdfgjklmnpqrstvwxz'
voCounter = 0
coCounter = 0
i = 0

# Εισαγωγή δεδομένων
lexi = input("Δώσε λέξη: ")

while i < len(lexi):
    if lexi[i] in vowels:
        voCounter += 1
    elif lexi[i] in consonants:
        coCounter += 1
        i += 1
    else:
        pass

# Εκτύπωση αποτελεσμάτων
print("Φωνήεντα: ", voCounter)
print("Σύμφωνα: ", coCounter)
