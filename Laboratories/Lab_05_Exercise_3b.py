consonants_counter = vowel_counter = other_counter = letter = 0
list_of_consonants = "bcdfgjklmnpqrstvwxz"
list_of_vowels = "aehyuio"

word = input("Δώσε μια λέξη: ")

while letter < len(word):
    if word[letter] in list_of_vowels:
        vowel_counter += 1
    elif word[letter] in list_of_consonants:
        consonants_counter += 1
    else:
        other_counter += 1
    letter += 1
    
print("Τα φωνήεντα της λέξης είναι %d." % vowel_counter)
print("Τα σύμφωνα της λέξης είναι %d." % consonants_counter)
print("Τα υπόλοιπα σύμβολα ή κεφαλαία γράμματα είναι %d." % other_counter)