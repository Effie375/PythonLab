consonants_counter = vowel_counter = letter = 0
list_of_consonants = "bcdfgjklmnpqrstvwxz"
list_of_vowels = "aehyuio"

word = input("Δώσε μια λέξη: ").strip()

while letter < len(word):
    if word[letter] in list_of_vowels:
        vowel_counter += 1
    elif word[letter] in list_of_consonants:
        consonants_counter += 1
    letter += 1

print(f"Η λέξη {word} περιέχει {vowel_counter} φωνήεντα.")
print(f"Η λέξη {word} περιέχει {consonants_counter} σύμφωνα.")
