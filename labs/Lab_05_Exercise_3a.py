#list_according_to=["b","c","d","f","g","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
#list_of_vowels=["a","e","h","y","u","i","o"]

list_according_to = "bcdfgjklmnpqrstvwxz"
list_of_vowels = "aehyuio"

i = 0
vow = 0
agr = 0

word = input("Enter a word: ")

while i < len(word):
    if word[i] in list_of_vowels:
        vow += 1
    elif word[i] in list_according_to:
        agr += 1
    i += 1
    
    
print("The vowels are:", vow)
print("The agreements are:",agr)
print("Τhe symbols and the blanks are", bal)

