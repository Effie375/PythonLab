consonants_counter = vowel_counter = other_counter = letter = 0
list_of_consonants = "bcdfgjklmnpqrstvwxzBCDFGJKLMNPQRSTVXZ"
list_of_vowels = "aehyuioAEHYUIO"

word = input("Δώσε μια λέξη: ").strip()

while letter < len(word):
    if word[letter] in list_of_vowels:
        vowel_counter += 1
    elif word[letter] in list_of_consonants:
        consonants_counter += 1
    else:
        other_counter += 1
    letter += 1
    
print(f"Τα φωνήεντα είναι {vowel_counter}.")
print(f"Τα σύμφωνα είναι {consonants_counter}.")
print(f"Τα σύμβολα είναι {other_counter}.")
