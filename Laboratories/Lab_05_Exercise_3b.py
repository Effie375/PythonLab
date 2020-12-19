consonants_counter = vowel_counter = other_counter = letter = 0
list_of_consonants = "bcdfgjklmnpqrstvwxz"
list_of_vowels = "aehyuio"

word = input("Δώσε μια λέξη: ").strip()

while letter < len(word):
    if word[letter] in list_of_vowels:
        vowel_counter += 1
    elif word[letter] in list_of_consonants:
        consonants_counter += 1
    else:
        other_counter += 1
    letter += 1
    
print(f"Τα φωνήεντα της λέξης είναι {vowel_counter}.")
print(f"Τα σύμφωνα της λέξης είναι {consonants_counter}.")
print(f"Τα υπόλοιπα σύμβολα ή κεφαλαία γράμματα είναι {other_counter}.")