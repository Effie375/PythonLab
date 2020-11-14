num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
num_3 = int(input("Enter a number: "))

sum = num_1 + num_2 

if sum % 2 == 0:
    print(sum * (num_2 // num_3))
else: 
    mod = num_3 % sum
    print("To upoloipo tis dieresis tou %d me to athroisma tou %d kai tou %d einai to %d." % (num_3, num_1, num_2, mod))
