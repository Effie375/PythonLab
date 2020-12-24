lexi = input("Δώσε λέξη: ")

vowels = 'aehiouy'
consonants = 'bcdfgjklmnpqrstvwxz'

v_counter = 0
c_counter = 0
i = 0

while i < len(lexi):
    if lexi[i] in vowels:
        v_counter += 1
 # Μπορεί να έχει και άλλους χαρακτήρες όπως " h /, αυτά δε θέλουμε να τα μετρήσουμε.
    elif lexi[i] in consonants:
        c_counter += 1
        i += 1

print("Φωνήεντα: ", v_counter)
print("Σύμφωνα: ", c_counter)
