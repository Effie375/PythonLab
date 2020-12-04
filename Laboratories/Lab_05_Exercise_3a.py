consonants_counter = vowel_counter = letter = 0
list_of_consonants = "bcdfgjklmnpqrstvwxz"
list_of_vowels = "aehyuio"

word = input("Δώσε μια λέξη: ")

while letter < len(word):
    if word[letter] in list_of_vowels:
        vowel_counter += 1
    elif word[letter] in list_of_consonants:
        consonants_counter += 1
    letter += 1

print("Η λέξη %s περιέχει %d φωνήεντα." % (word, vowel_counter))
print("Η λέξη %s περιέχει %d σύμφωνα." % (word, consonants_counter))