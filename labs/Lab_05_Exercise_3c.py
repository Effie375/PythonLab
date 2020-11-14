#list_of_consonants = ["b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
#list_of_vowels = ["a","e","h","y","u","i","o"]

list_of_consonants = "bcdfgjklmnpqrstvwxzBCDFGJKLMNPQRSTVXZ"
list_of_vowels = "aehyuioAEHYUIO"

consonants_counter = 0
vowel_counter = 0
other_counter = 0
letter = 0

word = input("Enter a word: ")

while letter < len(word):
    if word[letter] in list_of_vowels:
        vowel_counter += 1
    elif word[letter] in list_of_consonants:
        consonants_counter += 1
    else:
        other_counter += 1
    letter += 1
    
print("\nThe vowels are %d." % vowel_counter)
print("The consonants are %d." % consonants_counter)
print("The other letters are %d." % other_counter)